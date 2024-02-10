from typing import List, Dict

from card_house.infrastructure.cards_creators.cards_properties_creator import CardsPropertiesCreator
from card_house.infrastructure.cards_creators.db_cards_creator import DBCardsCreator
from card_house.infrastructure.entities.db_card import DBCard
from db.iclient_db import IClientDB

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
        self.app.route("/remove_card", methods=["POST"])(self.remove_card)
        self.app.route("/filter_cards", methods=["POST"])(self.filter_cards)

    def run(self):
        self.app.run(debug=True)

    def add_card(self) -> str:
        card = self.db_card_creator.create_card(request)
        card_id = self.client_db.add_card(card)
        return card_id

    def remove_card(self) -> str:
        card_id = request.json.get("card_id")
        status = self.client_db.remove_card(card_id)
        return "removed" if status else "not removed"

    def filter_cards(self) -> dict:
        filtered_cards = self.client_db.get_cards(request.json)
        cards_serialized = DBCard.cards_list_to_dict(filtered_cards)
        return cards_serialized
