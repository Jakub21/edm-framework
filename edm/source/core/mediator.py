"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Mediator class.
"""

from multiprocessing.connection import PipeConnection

from ..kernel import ProcessBlocker
from ..kernel.communication import BackendType, ServerGateway


class Mediator:
    def __init__(self, mp_connection: PipeConnection):
        """
        Initializer.
        """
        self.blocker = ProcessBlocker()
        self.server = ServerGateway(BackendType.MPQueue, mp_connection)

    def start(self):
        """
        Starts the communication backend and blocks the process.
        """
        self.blocker.run(self.update)

    def update(self):
        """
        Method executed in a loop by the process runner.
        """
