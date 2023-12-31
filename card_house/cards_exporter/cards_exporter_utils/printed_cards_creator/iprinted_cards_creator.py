from abc import ABC, abstractmethod
from typing import List
from card_house.cards_exporter.cards_exporter_entities.printed_card import PrintedCard
from card_house.infrastructure.entities.card import Card


class IPrintedCardsCreator(ABC):
    @abstractmethod
    def create_printed_cards_from_cards(self, cards: List[Card]) -> List[PrintedCard]:
        raise NotImplementedError
