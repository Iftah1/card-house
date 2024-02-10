from typing import List, Dict, Any

from card_house.db.error import CardExists
from card_house.infrastructure.cards_creators.db_cards_creator import DBCardsCreator
from card_house.infrastructure.entities.db_card import DBCard, DBCardKeys
from card_house.db.iclient_db import IClientDB

from flask import Flask, request


CARDS_SERIALIZED = Dict[str, List[Dict[str, str]]]


class Controller:
    def __init__(
            self,
            client_db: IClientDB,
            db_cards_creator: DBCardsCreator,
            app: Flask
    ):
        self.app = app
        self.db_card_creator = db_cards_creator
        self.client_db = client_db
        self._setup_routes()

    def _setup_routes(self):
        self.app.route("/add_card", methods=["POST"])(self.add_card)
        self.app.route("/remove_card", methods=["DELETE"])(self.remove_card)
        self.app.route("/filter_cards", methods=["POST"])(self.filter_cards)

    def run(self):
        self.app.run(debug=True)

    def add_card(self) -> str:
        card = self.db_card_creator.create_card(request)
        card_with_same_properties = self.client_db.get_cards(
            card_properties={
                DBCardKeys.TYPE: card.type.value,
                DBCardKeys.CONTENT: card.content,
            }
        )

        if len(card_with_same_properties) != 0:
            raise CardExists

        card_id = self.client_db.add_card(card)
        return card_id

    def remove_card(self) -> str:
        card_id = request.json.get(DBCardKeys.CARD_ID)
        status = self.client_db.remove_card(card_id)
        return "removed" if status else "failed"

    def filter_cards(self) -> Dict[str, Any]:
        filtered_cards = self.client_db.get_cards(request.json)
        cards_serialized = DBCard.cards_list_to_dict(filtered_cards)
        return cards_serialized
