import json
from typing import List
from entities.card import Card
from entities.card_type import CardType, CardDesignProperties
from cards_exporter.cards_pdf_exporter import CardPdfExporter
from cards_exporter.icardexporter import ICardExporter


def load_configurations() -> dict:
    with open("appsettings.json") as f:
        return json.load(f)


def generate_cards_exporter(config: dict) -> ICardExporter:
    return CardPdfExporter(config)


def get_cards_list(config: dict) -> List[Card]:
    question = config[CardType.QUESTION.GetDesignPropertiesKey()]
    answer = config[CardType.ANSWER.GetDesignPropertiesKey()]
    return [
        Card("Hello Mr. Kotler, how are you?", CardDesignProperties(question)),
        Card("I wanted to tell you something", CardDesignProperties(answer)),
        Card("It's really important so I want you to listen very carefully", CardDesignProperties(question)),
        Card("And it's top secret so you can't tell it to anyone", CardDesignProperties(answer)),
        Card("I'm not joking it means a lot to me", CardDesignProperties(question)),
        Card("So in order to tell you this", CardDesignProperties(answer)),
        Card("I created this PDF convertor", CardDesignProperties(question)),
        Card("It creates PDF from cards", CardDesignProperties(answer)),
        Card("Just like the one we need for House of Cards but who really cares?", CardDesignProperties(answer)),
        Card("And I think it works very well and it's really cool", CardDesignProperties(question)),
        Card("BTW if you don't think so you can bite me", CardDesignProperties(answer)),
        Card("So now that it's ready I can finally tell you what I need properly", CardDesignProperties(question)),
        Card("This is the way. Couldn't do it in any other way", CardDesignProperties(answer)),
        Card("Are you ready for it?", CardDesignProperties(question)),
        Card("I'm sure you want to hear it already", CardDesignProperties(answer)),
        Card("So here it comes", CardDesignProperties(question)),
        Card("I'M BATMANNNNNNNNNNNNNNNN", CardDesignProperties(answer))
    ]


if __name__ == '__main__':
    configuration = load_configurations()
    output_path = "output.pdf"
    cards = get_cards_list(configuration)
    exporter = generate_cards_exporter(configuration)
    exporter.export_cards(cards=cards, output_path=output_path)
