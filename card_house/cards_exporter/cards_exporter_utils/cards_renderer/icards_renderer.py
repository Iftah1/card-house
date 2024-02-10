from abc import ABC, abstractmethod
from typing import List
from card_house.cards_exporter.cards_exporter_entities.printed_card import Page


class ICardsRenderer(ABC):
    @abstractmethod
    def render_cards(self, cards_in_pages: List[Page]) -> str:
        raise NotImplementedError
