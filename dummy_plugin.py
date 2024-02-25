"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Example plugin used for development.
"""

from datetime import datetime
from edm.plugin import Plugin


class Dummy(Plugin):
    def initialize(self):
        print('Plugin start', datetime.now().time())
        self.runner.limiter.set_target_rate(3)

    def iteration(self):
        print('Plugin iter', datetime.now().time())

    def shutdown(self):
        print('Graceful shutdown', datetime.now().time())
