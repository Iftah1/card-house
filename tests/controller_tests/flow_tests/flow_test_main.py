from flask import Flask

from card_house.infrastructure.cards_creators.db_cards_creator import DBCardsCreator
from card_house.controller import Controller
from card_house.db.client_db import CardsDB

controller = Controller(

    client_db=CardsDB(
        db_name="cards.db"
    ),
    app=Flask(__name__),
    db_cards_creator=DBCardsCreator(),
)

controller.run()
