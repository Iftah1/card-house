from typing import Dict, Any

from card_house.cards_exporter.cards_exporter.icards_exporter import ICardsExporter
from card_house.db.error import CardExistsException
from card_house.infrastructure.cards_creators.db_cards_creator import DBCardsCreator
from card_house.infrastructure.entities.db_card import DBCard, CardKeys
from card_house.db.iclient_db import IClientDB

from flask import Flask, request


class Controller:
    def __init__(
            self,
            download_path: str,
            client_db: IClientDB,
            db_cards_creator: DBCardsCreator,
            cards_exporter: ICardsExporter,
            app: Flask
    ):
        self.download_path = download_path
        self.app = app
        self.cards_exporter = cards_exporter
        self.db_card_creator = db_cards_creator
        self.client_db = client_db
        self._setup_routes()

    def _setup_routes(self):
        self.app.route("/add_card", methods=["POST", "OPTIONS"])(self.add_card)
        self.app.route("/remove_card", methods=["DELETE"])(self.remove_card)
        self.app.route("/export_cards", methods=["POST"])(self.export_cards)
        self.app.route("/filter_cards", methods=["POST"])(self.filter_cards)

    def run(self):
        self.app.run(debug=True)

    def add_card(self) -> str:
        db_card = self.db_card_creator.create_card(request)
        if self.client_db.is_card_exists(db_card):
            raise CardExistsException

        card_id = self.client_db.add_card(db_card)
        return card_id

    def remove_card(self) -> str:
        card_id = request.json.get(CardKeys.CARD_ID)
        status = self.client_db.remove_card(card_id)
        return "removed" if status else "failed"

    def filter_cards(self) -> Dict[str, Any]:
        filtered_cards = self.client_db.get_cards(request.json)
        cards_serialized = DBCard.cards_list_to_dict(filtered_cards)
        return cards_serialized

    def export_cards(self) -> str:
        cards = self.client_db.get_all_cards()
        self.cards_exporter.export_cards(cards, self.download_path)
        return "success"
