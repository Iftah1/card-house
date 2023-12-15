from typing import List

from iclient_db import IClientDB
from entities.card import Card
from entities.card_proprties import CardProperties
from entities.status import Status

from flask import Flask, request, Request


class Controller:
    def __init__(self):
        self.app = Flask(__name__)
        self.client_db = IClientDB()
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

    def filter_cards(self) -> List[Card]:
        card_properties = CardProperties.generate_card_properties(request)
        filtered_cards = self.client_db.get_cards(card_properties)
        return filtered_cards
