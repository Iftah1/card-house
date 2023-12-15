from abc import ABC, abstractmethod
from typing import List, NoReturn

from entities.card import Card

from entities.status import Status


class IClientDB(ABC):
    @abstractmethod
    def add_card(self, card: Card) -> Status:
        raise NotImplementedError

    @abstractmethod
    def remove_card(self, card: Card) -> Status:
        raise NotImplementedError

    @abstractmethod
    def get_cards(self) -> Status:
        raise NotImplementedError



