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
# from ..kernel.communication import BackendType
from ..kernel.communication.mp_pipe import MPQueueClient  # TODO: to be replaced with a gateway


class Plugin:
    def __init__(self, mp_connection: PipeConnection):
        """
        Initializer.
        """
        self.runner = ProcessRunner()
        self.client = MPQueueClient(mp_connection)
        self.client.listen('stop', self._stop)
        self.initialize()

    def update(self):
        self.client.update()
        if self.runner.stopped:
            return
        self.iteration()

    def _stop(self):
        self.runner.stop()
        self.shutdown()

    @abstractmethod
    def initialize(self):
        """
        Executed once when the plugin starts.
        """

    @abstractmethod
    def iteration(self):
        """
        Executed in a loop while the plugin is active.
        """

    @abstractmethod
    def shutdown(self):
        """
        Executed once just before the plugin stops.
        """
