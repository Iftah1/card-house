from datetime import datetime
from typing import List
from uuid import uuid4

from flask import Request

from card_house.infrastructure.cards_creators.icards_creator import ICardsCreator
from card_house.infrastructure.entities.card import Card
from card_house.infrastructure.entities.card_type import CardType
from card_house.infrastructure.entities.db_card import CardKeys


class JsonToCardsCreator(ICardsCreator):
    def create_card(self, card: Request) -> Card:
        card_json = card.json
        card_type = CardType(card_json[CardKeys.TYPE])
        content = card_json[CardKeys.CONTENT]
        return Card(
            content=content,
            type=card_type,
        )

    def create_cards(self, cards: Request) -> List[Card]:
        cards_jsons = cards.json
        resulted_cards = []
        for card in cards_jsons[CardKeys.CARDS]:
            resulted_cards.append(self.create_card(card))
        return resulted_cards
