"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Spawns a child process.
"""

import multiprocessing as mp


class ProcessSpawner:
    child: mp.Process
    connection: mp.connection.PipeConnection

    def __init__(self, target_cls):
        """
        Initializer.
        """
        self.target_cls = target_cls

    def spawn(self):
        def target(connection):
            """
            Simple standardized function used to run a new process.
            """
            obj = self.target_cls(connection)
            obj.start()

        self.connection, child_connection = mp.Pipe()
        self.child = mp.Process(target=target, args=(child_connection,))
        self.child.start()

    def is_alive(self):
        return self.child.is_alive()
