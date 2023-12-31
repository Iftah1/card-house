from abc import ABC, abstractmethod
from typing import List, NoReturn

from card_house.infrastructure.entities.card import Card


class ICardsExporter(ABC):
    @abstractmethod
    def export_cards(self, cards: List[Card], path: str) -> NoReturn:
        raise NotImplementedError
    
