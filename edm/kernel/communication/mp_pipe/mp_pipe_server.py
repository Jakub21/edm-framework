"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Communication server implementation based on native multiprocessing pipe.
"""

from multiprocessing.connection import PipeConnection

from ..backend_type import BackendType
from ..server_base import ServerBase
from .. import Event


class MPQueueServer(ServerBase):
    TYPE = BackendType.MPQueue

    def __init__(self):
        self.remotes = {}
        self.queue = []

    def initialize_via_pipe(self, remote_name, mp_connection):
        self.remotes[remote_name] = mp_connection

    def update(self):
        for remote_name, connection in self.remotes.items():
            if not connection.poll():
                continue
            data = connection.recv()
            if not data:
                continue
            event = Event.FromSerialData(data)
            self.queue.append(event)
        while self.queue:
            event = self.queue.pop()
            self.broadcast(event)

    def broadcast(self, event: Event):
        serialized = event.serialize()
        for remote_name, connection in self.remotes.items():
            connection.send(serialized)
