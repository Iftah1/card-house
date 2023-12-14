from abc import ABC, abstractmethod
from typing import List, NoReturn
from entities.card import Card


class ICardExporter(ABC):
    @abstractmethod
    def export_cards(self, cards: List[Card], output_path: str) -> NoReturn:
        raise NotImplementedError
