"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Process blocker ensures the process does not exit prematurely.
"""

from .rate_limiter import RateLimiter


class ProcessRunner:
    def __init__(self):
        """
        Initializer.
        """
        self.limiter = RateLimiter()
        self.stopped = False

    def start(self, method):
        """
        Run.
        """
        while not self.stopped:
            self.limiter.tick()
            method()

    def stop(self):
        """
        Stop.
        """
        self.stopped = True
