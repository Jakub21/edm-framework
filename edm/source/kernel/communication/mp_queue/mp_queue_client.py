"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Communication client implementation based on native multiprocessing queue.
"""

from ..backend_type import BackendType
from ..client_base import ClientBase


class MPQueueClient(ClientBase):
    TYPE = BackendType.MPQueue
