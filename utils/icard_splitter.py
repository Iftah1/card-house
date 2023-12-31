from abc import ABC, abstractmethod
from typing import List
from entities.card import Card

Row = List[Card]
Page = List[Row]


class ICardsSplitter(ABC):
    @abstractmethod
    def split_cards(self, cards: List[Card]) -> List[Page]:
        raise NotImplementedError
