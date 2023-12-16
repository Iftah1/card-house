from typing import List

from entities.card import Card
from entities.card_proprties import CardProperties
from entities.status import Status
from iclient_db import IClientDB


class ClientDB(IClientDB):
    def add_card(self, card: Card) -> Status:
        return Status.SUCCESS

    def remove_card(self, card: Card) -> Status:
        return Status.SUCCESS

    def get_cards(self, card_properties: CardProperties) -> List[Card]:
        return []
