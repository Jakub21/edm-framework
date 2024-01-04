"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Limits the rate at which looped code can run.
"""


class RateLimiter:
    def __init__(self, rate: int = 140):
        """
        Initializer.
        rate: Maximum rate at which the loop will execute [Hz].
        """
        self.rate = rate

    def tick(self):
        """
        Call this method in loop, and it will automatically limit the rate.
        """
