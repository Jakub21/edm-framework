"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Limits the rate at which looped code can run.
"""

from datetime import datetime, timedelta
from time import sleep


class RateLimiter:
    def __init__(self, target_rate: float, max_drift: float):
        """
        Initializer.
        target_rate: Maximum rate at which the loop will execute [Hz].
        """
        self.target_rate = 30 if target_rate is None else target_rate
        self.max_drift = timedelta(seconds=1 if max_drift is None else max_drift)
        self.target_delta = timedelta(microseconds=1e6 / self.target_rate)
        self.last_tick = datetime.now()
        self.drift = timedelta(0)

    def tick(self):
        """
        Call this method in a loop, and it will automatically limit the rate.
        """
        now = datetime.now()
        elapsed = now - self.last_tick
        self.drift += min(self.target_delta - elapsed, self.max_drift)
        if self.drift > timedelta(0):
            sleep(self.drift.total_seconds())
        self.last_tick = now
