from dataclasses import dataclass

from flask import Request

from entities.card_design_properties import CardDesignProperties
from typing import Dict, List
from entities.card_proprties import CardProperties

CARDS_SERIALIZED = Dict[str, List[Dict[str, str]]]


@dataclass
class Card:
    card_properties: CardProperties
    design_properties: CardDesignProperties

    def card_to_dict(self) -> Dict[str, str]:
        serialized_card = {
            "content": self.card_properties.content,
            "card_type": self.card_properties.type.value,
            "date": str(self.card_properties.date),
            "version": self.card_properties.version,
            "id": self.card_properties.id
        }
        for key, value in serialized_card.items():
            if value is None:
                serialized_card[key] = "null"

        return serialized_card

    @staticmethod
    def cards_to_dict(cards: List['Card']) -> CARDS_SERIALIZED:
        cards_dict = {
            "cards": []
        }
        for card in cards:
            cards_dict["cards"].append(card.card_to_dict())
        return cards_dict

    @staticmethod
    def generate_card(request: Request) -> 'Card':
        card_properties = CardProperties.generate_card_properties(request)
        return Card(card_properties=card_properties, design_properties=None)
