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
    def __init__(self):
        """
        Initializer.
        """

    # @abstractmethod
    # def connect_pipe(self, name: str, mp_connection: PipeConnection):
    #     """
    #     ?
    #     """
    #
    # @abstractmethod
    # def fetch(self):
    #     """
    #     Fetches all pending events.
    #     """
    #
    # @abstractmethod
    # def broadcast(self, event):
    #     """
    #     ?
    #     """
