"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Client class is responsible for communicating with the mediator.
Used by the owner and plugins.
"""

from multiprocessing.connection import PipeConnection
from typing import List

from abc import ABC, abstractmethod


class ClientBase(ABC):
    @abstractmethod
    def __init__(self, mp_connection: PipeConnection):
        """
        Initializer.
        mp_connection: Multiprocessing pipe connection. Can be used directly or only to retrieve parameters for another
            connection mode.
        """

    @abstractmethod
    def update(self) -> List:
        """
        Fetches events from the server.
        """

    @abstractmethod
    def send(self, event):
        """
        Fetches events from the server.
        event: Event to broadcast.
        """
