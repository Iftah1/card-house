from typing import List, Dict

from iclient_db import IClientDB
from entities.card import Card
from entities.card_proprties import CardProperties
from entities.status import Status

from flask import Flask, request


CARDS_SERIALIZED = Dict[str, List[Dict[str, str]]]


class Controller:
    def __init__(self, client_db: IClientDB):
        self.app = Flask(__name__)
        self.client_db = client_db
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/add_card", methods=["POST"])(self.add_card)
        self.app.route("/remove_card", methods=["POST"])(self.remove_card)
        self.app.route("/filter_cards", methods=["POST"])(self.filter_cards)

    def run(self):
        self.app.run(debug=True)

    def add_card(self) -> Status:
        card = Card.generate_card(request)
        status = self.client_db.add_card(card)
        return status

    def remove_card(self) -> Status:
        card = Card.generate_card(request)
        status = self.client_db.remove_card(card)
        return status

    def filter_cards(self) -> CARDS_SERIALIZED:
        card_properties = CardProperties.generate_card_properties(request)
        filtered_cards = self.client_db.get_cards(card_properties)
        cards_serialized = Card.cards_to_dict(filtered_cards)
        return cards_serialized
