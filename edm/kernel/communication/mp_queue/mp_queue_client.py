"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Communication client implementation based on native multiprocessing queue.
"""

from multiprocessing.connection import PipeConnection
from typing import List

from ..backend_type import BackendType
from ..client_base import ClientBase


class MPQueueClient(ClientBase):
    TYPE = BackendType.MPQueue

    def __init__(self, mp_connection: PipeConnection):
        pass

    def update(self) -> List:
        pass

    def send(self, event):
        pass
