from db.iclient_db import IClientDB
from entities.card import Card
from entities.status import Status

from flask import Flask, request, Request


class Controller:
    def __init__(self):
        self.app = Flask(__name__)
        self.client_db = IClientDB()
        self.setup_routes()

    def setup_routes(self):
        self.app.route("/add_card", methods=["POST"])(self.add_card)

    def run(self):
        self.app.run(debug=True)

    def add_card(self) -> Status:
        card = self.parse_card_from_message()
        status = self.client_db.add_card(card)
        return status

    def remove_card(self) -> Status:
        card = self.parse_card_from_message()
        status = self.client_db.remove_card(card)
        return status

    def filter_cards(self, ):

    @staticmethod
    def parse_card_from_message() -> Card:
        message_content = request.json
        card = Card.generate_card(message_content)
        return card
