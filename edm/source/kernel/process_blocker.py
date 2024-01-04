"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Process blocker ensures the process does not exit prematurely.
"""

from .rate_limiter import RateLimiter


class ProcessBlocker:
    def __init__(self):
        """
        Initializer.
        """
        self.limiter = RateLimiter()
        self.stopped = False

    def run(self, method):
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
