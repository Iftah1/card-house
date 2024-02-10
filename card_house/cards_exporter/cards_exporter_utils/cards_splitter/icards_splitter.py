from abc import ABC, abstractmethod
from typing import List
from card_house.cards_exporter.cards_exporter_entities.printed_card import Page
from card_house.infrastructure.entities.card import Card


class ICardsSplitter(ABC):
    @abstractmethod
    def split_cards(self, cards: List[Card]) -> List[Page]:
        raise NotImplementedError
