from dataclasses import dataclass

from flask import Request

from entities.card_type import CardType
from entities.card_design_properties import CardDesignProperties
from datetime import datetime
from uuid import UUID, uuid4
from typing import Dict
from card_type import CardType
from entities.card_proprties import CardProperties


@dataclass
class Card:
    card_properties: CardProperties
    design_properties: CardDesignProperties

    def serialize_card(self) -> Dict[str, str]:
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
    def generate_card(request: Request) -> 'Card':
        card_properties = CardProperties.generate_card_properties(request)
        return Card(card_properties=card_properties, design_properties=None)
