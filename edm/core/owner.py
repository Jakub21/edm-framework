"""
[ EDM Framework ]
Jakub21, 2023/12
MIT License
--------------------------------
Owner class.
"""

from time import sleep
from pathlib import Path

from .mediator import Mediator
from ..kernel import ProcessRunner, ProcessSpawner
# from ..kernel.communication import BackendType
from ..kernel.communication.mp_pipe import MPQueueClient  # TODO: to be replaced with a gateway
from ..kernel.communication.event import Event


class Owner:
    client: MPQueueClient

    def __init__(self, configuration: Path):
        """
        Initializer. Loads the configuration and prepares the framework.
        configuration: Path to the configuration file.
        """
        self.mediator_ref = ProcessSpawner(Mediator)
        self.runner = ProcessRunner()

    def start(self, blocking: bool = True):
        """
        Spawns all other processes and triggers the initialization procedure.
        blocking: Blocking mode, if set to true this method will not return until the framework exits.
        """
        self.mediator_ref.start()
        self.client = MPQueueClient(self.mediator_ref.connection)
        if blocking:
            self.runner.start(self.update)

    def stop(self):
        """
        Stops all other processes, breaks the execution loop and unblocks the execution.
        """
        self.client.send(Event('owner', 'stop', {}))
        sleep(1)
        self.runner.stop()
        self.mediator_ref.stop()

    def update(self):
        """
        Method executed in a loop by the process runner.
        """
        self.client.update()
