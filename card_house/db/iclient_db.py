from abc import ABC, abstractmethod
from typing import List, Any, Dict

from card_house.infrastructure.entities.db_card import DBCard


class IClientDB(ABC):
    @abstractmethod
    def add_card(self, card: DBCard) -> str:
        raise NotImplementedError

    @abstractmethod
    def remove_card(self, card: DBCard) -> bool:
        raise NotImplementedError

    @abstractmethod
    def get_cards(self, card_properties: Dict[str, Any]) -> List[DBCard]:
        raise NotImplementedError

    @abstractmethod
    def get_all_cards(self):
        raise NotImplementedError

    @abstractmethod
    def is_card_exists(self, card: DBCard):
        raise NotImplementedError
