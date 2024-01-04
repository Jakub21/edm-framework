"""
[ EDM Framework ]
Jakub21, 2024/01
MIT License
--------------------------------
Server class is responsible for handling communication for the mediator.
"""

from multiprocessing.connection import PipeConnection

from abc import ABC, abstractmethod


class ServerBase(ABC):
    @abstractmethod
    def __init__(self, mp_connection: PipeConnection):
        """
        Initializer.
        mp_connection: Multiprocessing pipe connection. Can be used directly or only to send parameters for another
            connection mode.
        """

    @abstractmethod
    def update(self):
        """
        Fetches all received events and broadcasts them.
        """
