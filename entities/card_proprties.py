from dataclasses import dataclass
from datetime import datetime
from typing import Dict
from uuid import UUID

from flask import Request

from entities.card_type import CardType


@dataclass
class CardProperties:
    content: str
    version: str
    type: CardType
    date: datetime
    id: UUID

    @staticmethod
    def generate_card_properties(request: Request) -> 'CardProperties':
        card_json = request.json
        return CardProperties.generate_card_from_json(card_json)

    @staticmethod
    def generate_card_from_json(card_json: Dict[str, str]) -> 'CardProperties':
        content = card_json["content"]
        request_card_type = card_json["card_type"]
        if request_card_type == CardType.ANSWER.value:
            card_type = CardType.ANSWER
        else:
            card_type = CardType.QUESTION
        date = datetime.strptime(card_json["date"], "%Y-%m-%d %H:%M:%S")
        version = card_json["version"]
        id = card_json["id"]
        return CardProperties(
                content=content,
                version=version,
                date=date,
                id=UUID(id),
                type=card_type
        )
