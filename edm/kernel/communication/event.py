"""
[ EDM Framework ]
Jakub21, 2024/02
MIT License
--------------------------------
Backend-agnostic serializable communication event implementation.
"""

from typing import Any
import json


class Event:
    def __init__(self, emitter: str, key: str, data: dict[str: Any]):
        self.emitter = emitter
        self.key = key
        self.data = data

    def serialize(self) -> str:
        sanitized = {
            'emitter': self.emitter,
            'key': self.key,
            'data': self.data,
        }
        data = json.dumps(sanitized)
        return data

    @classmethod
    def FromSerialData(cls, serial_data: str) -> 'Event':
        data = json.loads(serial_data)
        obj = cls(data['emitter'], data['key'], data['data'])
        return obj
