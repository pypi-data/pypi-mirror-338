# Copyright (C) 2024  The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

import logging
from time import monotonic
from typing import List, Optional

from google.protobuf.field_mask_pb2 import FieldMask
import grpc

from swh.graph.grpc.swhgraph_pb2 import GraphDirection, NodeFilter, TraversalRequest
from swh.graph.grpc.swhgraph_pb2_grpc import TraversalServiceStub
from swh.model.swhids import CoreSWHID
from swh.model.swhids import ObjectType as SWHIDType
from swh.model.swhids import QualifiedSWHID

logger = logging.getLogger(__name__)


class GraphProvenance:
    def __init__(self, url, max_edges=10000):
        """Provenance instance using a swh-graph GRPC backend

        Args:
            url: the location of the GRPC server; should be of the form: "<host>:<port>"
            max_edges: maximum number of edges that can be fetched by a traversal query;
              for more details, see:
              https://docs.softwareheritage.org/devel/swh-graph/grpc-api.html#limiting-the-traversal
        """
        self.graph_url = url
        self._channel = grpc.insecure_channel(self.graph_url)
        self._stub = TraversalServiceStub(self._channel)
        self._max_edges = max_edges

    def check_config(self) -> bool:
        return True

    def _get_anchor(self, swhid: CoreSWHID, leaf_type) -> Optional[CoreSWHID]:
        """Find some top level object that contains the argument

        The search focus on `leaf_type`, that can be either "rel" or "rev".
        However if you pass a `shwid` for an higher level object, you will get
        it back as is.

        Return a SWHID or None is nothing of the requested type is found.
        """
        if swhid.object_type in (SWHIDType.RELEASE, SWHIDType.SNAPSHOT):
            # We won't find anything better than the object already passed
            return swhid
        if swhid.object_type == SWHIDType.REVISION and leaf_type == "rev":
            # We are requesting a revision but we already have a revision, so
            # return that.
            return swhid

        src = [str(swhid)]

        if leaf_type == "rel":
            edges = "dir:dir,cnt:dir,dir:rev,rev:rel,dir:rel,cnt:rel"
        elif leaf_type == "rev":
            edges = "dir:dir,cnt:dir,dir:rev"
        else:
            raise ValueError(leaf_type)

        anchor_search = TraversalRequest(
            src=src,
            edges=edges,
            direction=GraphDirection.BACKWARD,
            max_edges=self._max_edges,
            return_nodes=NodeFilter(types=leaf_type),
            mask=FieldMask(paths=["swhid"]),
            max_matching_nodes=1,
        )
        try:
            t0 = monotonic()
            resp = list(self._stub.Traverse(anchor_search))
        except grpc.RpcError as exc:
            if exc.code() == grpc.StatusCode.NOT_FOUND:
                logger.debug("SWHID %s anchor: not found", swhid)
                return None
            d = exc.details()
            if (
                exc.code() == grpc.StatusCode.INVALID_ARGUMENT
                and d is not None
                and d.startswith("Unknown SWHID:")
            ):
                # for java…
                return None
            logger.debug("SWHID %s anchor: GRPC error %s", swhid, exc)
            raise
        finally:
            logger.debug(
                "SWHID %s anchor query took %.2fms", swhid, (monotonic() - t0) * 1000.0
            )

        if resp:
            assert len(resp) == 1
            node = resp[0]
            logger.debug("SWHID %s anchor: %s", swhid, resp[0])
            return CoreSWHID.from_string(node.swhid)
        logger.debug("SWHID %s anchor: no result", swhid)
        return None

    def _get_origin(self, anchor_swhid: CoreSWHID) -> Optional[str]:
        """Find the url of an origin associated with an anchor object.

        If no origin is found, return None."""
        if anchor_swhid.object_type not in (
            SWHIDType.REVISION,
            SWHIDType.RELEASE,
            SWHIDType.SNAPSHOT,
        ):
            # we need a revision, or higher
            raise ValueError(anchor_swhid.object_type)
        src = [str(anchor_swhid)]
        origin_search = TraversalRequest(
            src=src,
            edges="rev:rev,rev:rel,*:snp,*:ori",
            direction=GraphDirection.BACKWARD,
            max_edges=self._max_edges,
            return_nodes=NodeFilter(types="ori"),
            max_matching_nodes=1,
        )
        try:
            t0 = monotonic()
            resp = list(self._stub.Traverse(origin_search))
        except grpc.RpcError as exc:
            if exc.code() == grpc.StatusCode.NOT_FOUND:
                logger.debug("SWHID %s origin: not found", anchor_swhid)
                return None
            d = exc.details()
            if (
                exc.code() == grpc.StatusCode.INVALID_ARGUMENT
                and d is not None
                and d.startswith("Unknown SWHID:")
            ):
                # for java…
                return None
            logger.debug("SWHID %s origin: GRPC error %s", anchor_swhid, exc)
            raise
        finally:
            logger.debug(
                "SWHID %s origin query took %.2fms",
                anchor_swhid,
                (monotonic() - t0) * 1000.0,
            )

        if resp:
            assert len(resp) == 1
            logger.debug("SWHID %s origin: %s", anchor_swhid, resp[0].ori.url)
            return resp[0].ori.url
        logger.debug("SWHID %s origin: no result", anchor_swhid)
        return None

    def whereis(self, *, swhid: CoreSWHID) -> Optional[QualifiedSWHID]:
        """Given a SWHID return a QualifiedSWHID with some provenance info:

        - the release or revision containing that content or directory
        - the url of the origin containing that content or directory

        This can also be called for revision, release or snapshot to retrieve
        origin url information if any. When using a revision, the anchor will
        be an association release if any.
        """
        anchor = self._get_anchor(swhid, "rel")
        if anchor is None:
            anchor = self._get_anchor(swhid, "rev")

        if anchor is None:
            return None
        else:
            origin = self._get_origin(anchor)
            if anchor == swhid:
                # don't anchor releases (and revisions) on themselves
                anchor = None
            return QualifiedSWHID(
                object_type=swhid.object_type,
                object_id=swhid.object_id,
                anchor=anchor,
                origin=origin,
            )

    def whereare(self, *, swhids: List[CoreSWHID]) -> List[Optional[QualifiedSWHID]]:
        """Given a SWHID list return a list of provenance info:

        See `whereis` documentation for details on the provenance info.
        """
        return [self.whereis(swhid=si) for si in swhids]
