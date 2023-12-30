from abc import ABC, abstractmethod
from typing import List
from code.cards_exporter.cards_exporter_entities.printed_card import PrintedCard
from code.infrastructure.entities.card import Card


class IPrintedCardsCreator(ABC):
    @abstractmethod
    def create_printed_cards_from_cards(self, cards: List[Card]) -> List[PrintedCard]:
        raise NotImplementedError
