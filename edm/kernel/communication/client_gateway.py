"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Communication gateway class.
"""

from multiprocessing.connection import PipeConnection

from .backend_type import BackendType
from .client_base import ClientBase
from .mp_queue.mp_queue_client import MPQueueClient


class ClientGateway:
    def __init__(self, backend_type: BackendType, mp_connection: PipeConnection):
        """
        Initializer.
        """
        backend_class = self.get_client_class(backend_type)
        # noinspection PyCallingNonCallable
        self.backend = backend_class(mp_connection)

    @staticmethod
    def get_client_class(backend_type: BackendType) -> ClientBase:
        """
        Returns client implementation for a given backend type.
        """
        return {
            BackendType.MPQueue: MPQueueClient,
        }[backend_type]

    # Client API (check client_base.py for details)

    def update(self):
        return self.backend.update()

    def send(self, event):
        return self.backend.send(event)
