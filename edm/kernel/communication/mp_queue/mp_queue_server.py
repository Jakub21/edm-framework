"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Communication server implementation based on native multiprocessing queue.
"""

from multiprocessing.connection import PipeConnection

from ..backend_type import BackendType
from ..server_base import ServerBase


class MPQueueServer(ServerBase):
    TYPE = BackendType.MPQueue

    def __init__(self):
        pass

    def update(self):
        pass
