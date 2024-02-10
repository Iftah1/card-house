from datetime import datetime
from typing import List
from uuid import uuid4

from flask import Request

from card_house.infrastructure.cards_creators.icards_creator import ICardsCreator
from card_house.infrastructure.entities.card_type import CardType
from card_house.infrastructure.entities.db_card import DBCard


class DBCardsCreator(ICardsCreator):
    def create_card(self, card: Request) -> DBCard:
        card_json = card.json
        card_type = CardType(card_json["type"])
        content = card_json["content"]
        return DBCard(
            content=content,
            type=card_type,
            version="v1",
            creation_time=datetime.now(),
            card_id=str(uuid4())
        )

    def create_cards(self, cards: Request) -> List[DBCard]:
        cards_jsons = cards.json
        resulted_cards = []
        for card in cards_jsons["cards"]:
            resulted_cards.append(self.create_card(card))
        return resulted_cards
