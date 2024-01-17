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
    target_rate: float  # target Ticks Per Second [Hz]
    target_delta: timedelta  # target duration of a single loop, calculated from TPS
    last_tick: datetime  # time of the last tick
    max_drift: timedelta  # maximum drift that will be compensated for
    drift: timedelta  # current drift (increases when loop take too long to keep up)

    def __init__(self, target_rate: float = 1, max_drift: float = 1):
        """
        Initializer.
        target_rate: Maximum rate at which the loop will execute [Hz].
        max_drift: Maximum drift that will be compensated for [seconds].
        """
        self.target_rate = target_rate
        self.max_drift = timedelta(seconds=max_drift)
        self.recalculate()

    def recalculate(self):
        self.target_delta = timedelta(microseconds=1e6 / self.target_rate)
        self.last_tick = datetime.now()
        self.drift = timedelta(0)

    def set_max_drift(self, max_drift: float):
        """
        Sets a new maximum drift that will be compensated for [seconds].
        """
        self.max_drift = timedelta(seconds=max_drift)
        self.recalculate()

    def set_target_rate(self, target_rate: float):
        """
        Sets a new target rate (ticks per second) [Hz].
        """
        self.target_rate = target_rate
        self.recalculate()

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
