from abc import ABC, abstractmethod
from typing import List, NoReturn

from card import Card


class ICardExporter(ABC):
    @abstractmethod
    def convert(self, cards: List[Card], path: str) -> NoReturn:
        raise NotImplementedError
    
