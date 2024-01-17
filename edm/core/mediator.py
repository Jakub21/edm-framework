"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Mediator class.
"""

from pathlib import Path
from multiprocessing.connection import PipeConnection

from ..kernel import ProcessRunner, ProcessSpawner
from ..kernel.communication import BackendType, ServerGateway


class Mediator:
    def __init__(self, mp_connection: PipeConnection):
        """
        Initializer.
        """
        self.runner = ProcessRunner()
        self.server = ServerGateway(BackendType.MPQueue)
        # self.server.initialize_via_pipe(mp_connection)
        self.plugins = []
        self.start_plugins()

    def start_plugins(self):
        """
        Starts plugin processes according to the configuration.
        """
        path = Path(__file__).parent.parent.parent / 'dummy_plugin.py'
        plugin = ProcessSpawner.FromPath(path, 'Dummy')
        plugin.start()
        self.plugins += [plugin]
        # self.server.initialize_via_pipe(plugin.connection)

    def update(self):
        """
        Method executed in a loop by the process runner.
        """
        self.server.update()
