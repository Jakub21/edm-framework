"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Spawns a child process.
"""

import multiprocessing as mp
from pathlib import Path

from ..kernel import import_module


def target(target_cls, connection):
    """
    Simple standardized function used to run a new process.
    """
    obj = target_cls(connection)
    obj.runner.start(obj.update)


class ProcessSpawner:
    child: mp.Process
    connection: mp.connection.PipeConnection

    def __init__(self, target_cls):
        """
        Initializer.
        """
        self.target_cls = target_cls

    @classmethod
    def FromPath(cls, path: Path, cls_name: str) -> 'ProcessSpawner':
        target_module = import_module(path)
        target_cls = getattr(target_module, cls_name)
        return ProcessSpawner(target_cls)

    def start(self):
        """
        Starts the child process and creates a pipe connection.
        """
        self.connection, child_connection = mp.Pipe()
        self.child = mp.Process(target=target, args=(self.target_cls, child_connection,))
        self.child.start()

    def is_alive(self):
        """
        Checks if the child process is still alive.
        """
        return self.child.is_alive()

    def stop(self):
        """
        Terminates and joins the child process.
        """
        self.child.terminate()
        self.child.join()
