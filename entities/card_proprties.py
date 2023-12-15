from dataclasses import dataclass
from datetime import datetime
from typing import Dict
from uuid import UUID

from flask import Request

from entities.card_type import CardType
from consts import *


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
        content = card_json[CONTENT]
        request_card_type = card_json[CARD_TYPE]
        if request_card_type == CardType.ANSWER.value:
            card_type = CardType.ANSWER
        else:
            card_type = CardType.QUESTION
        date = datetime.strptime(card_json[DATE], TIME_FORMAT)
        version = card_json[VERSION]
        id = card_json[ID]
        return CardProperties(
                content=content,
                version=version,
                date=date,
                id=UUID(id),
                type=card_type
        )
