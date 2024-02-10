import json
import os
from typing import Dict, Any

from flask import Flask

from card_house.cards_exporter.cards_exporter.cards_pdf_exporter import CardsPdfExporter
from card_house.cards_exporter.cards_exporter.icards_exporter import ICardsExporter
from card_house.cards_exporter.cards_exporter_io.cards_file_writer.html_to_pdf_cards_file_writer import \
    HtmlToPdfCardsFileWriter
from card_house.cards_exporter.cards_exporter_io.cards_file_writer.icards_file_writer import ICardsFileWriter
from card_house.cards_exporter.cards_exporter_utils.cards_renderer.cards_html_renderer import CardsHtmlRenderer
from card_house.cards_exporter.cards_exporter_utils.cards_renderer.icards_renderer import ICardsRenderer
from card_house.cards_exporter.cards_exporter_utils.cards_splitter.cards_splitter import CardsSplitter
from card_house.cards_exporter.cards_exporter_utils.cards_splitter.icards_splitter import ICardsSplitter
from card_house.infrastructure.cards_creators.db_cards_creator import DBCardsCreator
from card_house.controller import Controller
from card_house.db.client_db import CardsDB
from card_house.infrastructure.cards_creators.icards_creator import ICardsCreator
from card_house.infrastructure.cards_creators.json_to_cards_creator import JsonToCardsCreator
from card_house.infrastructure.cards_creators.printed_cards_creator import PrintedCardsCreator


def create_configuration(config_path: str) -> Dict[str, Any]:
    with open(config_path) as f:
        return json.load(f)


def create_exporter(config_path: str) -> ICardsExporter:
    configuration: Dict[str, Any] = create_configuration(config_path)
    printed_cards_creator: ICardsCreator = PrintedCardsCreator(configuration)
    cards_splitter: ICardsSplitter = CardsSplitter(configuration, printed_cards_creator)
    cards_renderer: ICardsRenderer = CardsHtmlRenderer(configuration)
    cards_file_writer: ICardsFileWriter = HtmlToPdfCardsFileWriter(configuration)
    return CardsPdfExporter(cards_splitter, cards_renderer, cards_file_writer)


text_path = "tests/cards_exporter_tests/cards_text.txt"
configuration_path = "..\\..\\..\\card_house\\cards_exporter\\cards_exporter_configuration\\appsettings.json"
output_path = "tests/cards_exporter_tests/output.pdf"
cards_exporter: ICardsExporter = create_exporter(configuration_path)


controller = Controller(
    client_db=CardsDB(
        db_name="cards.db"
    ),
    app=Flask(__name__),
    db_cards_creator=DBCardsCreator(),
    cards_exporter=create_exporter(configuration_path),
    cards_creator=JsonToCardsCreator(),
    download_path=os.getcwd()
)

controller.run()
