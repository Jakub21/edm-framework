"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Plugin class.
"""

from abc import abstractmethod
from multiprocessing.connection import PipeConnection

from ..kernel import ProcessRunner
from ..kernel.communication import BackendType, ClientGateway


class Plugin:
    def __init__(self, mp_connection: PipeConnection):
        """
        Initializer.
        """
        self.runner = ProcessRunner()
        self.client = ClientGateway(BackendType.MPQueue, mp_connection)
        self.initialize()

    @abstractmethod
    def initialize(self):
        """
        Executed once when the plugin starts.
        """

    @abstractmethod
    def update(self):
        """
        Executed in a loop while the plugin is active.
        """

    @abstractmethod
    def shutdown(self):
        """
        Executed once just before the plugin stops.
        """
