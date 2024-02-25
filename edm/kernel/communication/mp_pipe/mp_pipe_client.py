"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Communication client implementation based on native multiprocessing pipe.
"""

from multiprocessing.connection import PipeConnection
from typing import Callable, List, TYPE_CHECKING

from ..backend_type import BackendType
from ..client_base import ClientBase
from .. import Event


class MPQueueClient(ClientBase):
    TYPE = BackendType.MPQueue

    def __init__(self, mp_connection: PipeConnection):
        self.mp_connection = mp_connection
        self.callbacks = {}

    def listen(self, key: str, callback: Callable):
        self.callbacks[key] = callback

    def update(self) -> List:
        if not self.mp_connection.poll():
            return
        data = self.mp_connection.recv()
        if not data:
            return
        event = Event.FromSerialData(data)
        if event.key not in self.callbacks.keys():
            return
        self.callbacks[event.key]()

    def send(self, event: Event):
        self.mp_connection.send(event.serialize())
