"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Process blocker ensures the process does not exit prematurely.
"""

from .rate_limiter import RateLimiter


class ProcessRunner:
    def __init__(self, target_rate=None, max_drift=None):
        """
        Initializer.
        target_rate: only passed to RateLimiter.
        max_drift: only passed to RateLimiter.
        """
        self.limiter = RateLimiter(target_rate, max_drift)
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
