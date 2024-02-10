from typing import List, Any

from flask import Request

from card_house.infrastructure.cards_creators.icards_creator import ICardsCreator
from card_house.infrastructure.entities.card_type import CardType
from card_house.infrastructure.entities.db_card import DBCard


class CardsPropertiesCreator(ICardsCreator):
    def create_card(self, card: Request) -> DBCard:
        json_card = card.json
        return DBCard(
            card_id=json_card.get("card_id"),
            creation_time=json_card.get("creation_time"),
            content=json_card.get("content"),
            version=json_card.get("version"),
            type=CardType(json_card.get("card_type"))
        )

    def create_cards(self, cards: Request) -> List[DBCard]:
        resulted_cards = []
        for card in cards.json:
            resulted_cards.append(self.create_card(card))
        return resulted_cards
