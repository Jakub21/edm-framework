"""
[ EDM Framework ]
Jakub21, 2024/02
MIT License
--------------------------------
Event transmission modes.
"""

from enum import Enum, auto


class EventMode(Enum):
    Broadcast = auto()
    Targeted = auto()
