import json
import os.path
from typing import List, Dict, Any
from card_house.cards_exporter.cards_exporter.cards_pdf_exporter import CardsPdfExporter
from card_house.cards_exporter.cards_exporter.icards_exporter import ICardsExporter
from card_house.cards_exporter.cards_exporter_io.cards_file_writer.html_to_pdf_cards_file_writer import \
    HtmlToPdfCardsFileWriter
from card_house.cards_exporter.cards_exporter_io.cards_file_writer.icards_file_writer import ICardsFileWriter
from card_house.cards_exporter.cards_exporter_utils.cards_renderer.cards_html_renderer import CardsHtmlRenderer
from card_house.cards_exporter.cards_exporter_utils.cards_renderer.icards_renderer import ICardsRenderer
from card_house.cards_exporter.cards_exporter_utils.cards_splitter.cards_splitter import CardsSplitter
from card_house.cards_exporter.cards_exporter_utils.cards_splitter.icards_splitter import ICardsSplitter
from card_house.cards_exporter.cards_exporter_utils.printed_cards_creator.iprinted_cards_creator import \
    IPrintedCardsCreator
from card_house.cards_exporter.cards_exporter_utils.printed_cards_creator.printed_cards_creator import \
    PrintedCardsCreator
from card_house.infrastructure.entities.card import Card
from card_house.infrastructure.entities.card_type import CardType


def create_card_type_from_index(index: int) -> CardType:
    return CardType.QUESTION if index % 2 == 0 else CardType.ANSWER


def create_cards_list(file_path: str) -> List[Card]:
    with open(file_path) as f:
        return [Card(line, create_card_type_from_index(index)) for (index, line) in enumerate(f.readlines())]


def create_configuration(config_path: str) -> Dict[str, Any]:
    with open(config_path) as f:
        return json.load(f)


def create_exporter(config_path: str) -> ICardsExporter:
    configuration: Dict[str, Any] = create_configuration(config_path)
    printed_cards_creator: IPrintedCardsCreator = PrintedCardsCreator(configuration)
    cards_splitter: ICardsSplitter = CardsSplitter(configuration, printed_cards_creator)
    cards_renderer: ICardsRenderer = CardsHtmlRenderer(configuration)
    cards_file_writer: ICardsFileWriter = HtmlToPdfCardsFileWriter(configuration)
    return CardsPdfExporter(cards_splitter, cards_renderer, cards_file_writer)


def main():
    text_path = "tests/cards_exporter_tests/cards_text.txt"
    configuration_path = "card_house/cards_exporter/cards_exporter_configuration/appsettings.json"
    output_path = "tests/cards_exporter_tests/output.pdf"
    cards: List[Card] = create_cards_list(text_path)
    cards_exporter: ICardsExporter = create_exporter(configuration_path)
    cards_exporter.export_cards(cards, output_path)


if __name__ == '__main__':
    os.chdir("../../")
    main()
