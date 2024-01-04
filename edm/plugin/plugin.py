"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Plugin class.
"""

from ..kernel import ProcessBlocker


class Plugin:
    def __init__(self):
        """
        Initializer.
        """
        self.blocker = ProcessBlocker()
