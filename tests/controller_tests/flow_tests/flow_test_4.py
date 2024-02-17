import json
from requests import post, delete
from flask import Flask

from card_house.cards_exporter.cards_exporter.cards_pdf_exporter import CardsPdfExporter
from card_house.cards_exporter.cards_exporter_io.cards_file_writer.html_to_pdf_cards_file_writer import \
    HtmlToPdfCardsFileWriter
from card_house.cards_exporter.cards_exporter_utils.cards_renderer.cards_html_renderer import CardsHtmlRenderer
from card_house.cards_exporter.cards_exporter_utils.cards_splitter.cards_splitter import CardsSplitter
from card_house.infrastructure.cards_creators.db_cards_creator import DBCardsCreator
from card_house.controller import Controller
from card_house.db.client_db import CardsDB
from threading import Thread

from card_house.infrastructure.cards_creators.printed_cards_creator import PrintedCardsCreator

controller = Controller(
    client_db=CardsDB(
        db_name="cards.db"
    ),
    app=Flask(__name__),
    db_cards_creator=DBCardsCreator(),
    cards_exporter=CardsPdfExporter(
        cards_splitter=CardsSplitter(
            configuration={},
            printed_cards_creator=PrintedCardsCreator(
                configuration={}
            ),
        ),
        cards_renderer=CardsHtmlRenderer(
            configuration={}
        ),
        cards_file_writer=HtmlToPdfCardsFileWriter(
            configuration={}
        ),
    ),
    download_path=""
)

controller_thread = Thread(target=controller.run)

add_card_json = {
    "content": "hello world",
    "type": "answer",
}

remove_card_json = {

}

get_cards_json = {
    "type": "answer",
}


add_response = post(url="http://127.0.0.1:5000/add_card", json=add_card_json)
card_id = add_response.text

add_response = post(url="http://127.0.0.1:5000/add_card", json=add_card_json)

first_get_response = post(url="http://127.0.0.1:5000/filter_cards", json=get_cards_json)
cards_first_get_response = json.loads(first_get_response.text)

assert len(cards_first_get_response["cards"]) == 1

remove_card_json["card_id"] = card_id
remove_response = delete(url="http://127.0.0.1:5000/remove_card", json=remove_card_json)


print("tests has been run successfully")
