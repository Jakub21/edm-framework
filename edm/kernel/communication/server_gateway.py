"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Communication gateway class.
"""

from multiprocessing.connection import PipeConnection

from .backend_type import BackendType
from .server_base import ServerBase
from .mp_queue.mp_queue_server import MPQueueServer


class ServerGateway:
    def __init__(self, backend_type: BackendType, mp_connection: PipeConnection):
        """
        Initializer.
        """
        backend_class = self.get_server_class(backend_type)
        # noinspection PyCallingNonCallable
        self.backend = backend_class(mp_connection)

    @staticmethod
    def get_server_class(backend_type: BackendType) -> ServerBase:
        """
        Returns server implementation for a given backend type.
        """
        return {
            BackendType.MPQueue: MPQueueServer,
        }[backend_type]

    # Server API (check server_base.py for details)

    pass
