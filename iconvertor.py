from abc import ABC, abstractmethod
from typing import List, NoReturn

from card import Card


class IConvertor(ABC):
    @abstractmethod
    def convert(self, cards: List[Card], path: str) -> NoReturn:
        raise NotImplementedError
    
