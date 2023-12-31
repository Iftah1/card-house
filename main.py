import json
from typing import List, Dict, Any
from entities.card import Card
from entities.card_type import CardType
from entities.card_design_properties import CardDesignProperties
from cards_exporter.cards_pdf_exporter import CardPdfExporter
from cards_exporter.icardexporter import ICardExporter


def load_configurations() -> Dict[str, Any]:
    with open("appsettings.json") as f:
        return json.load(f)


def generate_cards_exporter(config: Dict[str, Any]) -> ICardExporter:
    return CardPdfExporter(config)


def get_cards_list(config: Dict[str, Any]) -> List[Card]:

    question = config[CardDesignProperties.GetDesignPropertiesConfigurationKey(CardType.QUESTION)]
    answer = config[CardDesignProperties.GetDesignPropertiesConfigurationKey(CardType.ANSWER)]
    return [
        Card("Hello Mr. Kotler, how are you?", CardType.QUESTION, CardDesignProperties(question)),
        Card("I wanted to tell you something", CardType.ANSWER, CardDesignProperties(answer)),
        Card("It's really important so I want you to listen very carefully", CardType.QUESTION,
             CardDesignProperties(question)),
        Card("And it's top secret so you can't tell it to anyone", CardType.ANSWER, CardDesignProperties(answer)),
        Card("I'm not joking it means a lot to me", CardType.QUESTION, CardDesignProperties(question)),
        Card("So in order to tell you this", CardType.ANSWER, CardDesignProperties(answer)),
        Card("I created this PDF convertor", CardType.QUESTION, CardDesignProperties(question)),
        Card("It creates PDF from cards", CardType.ANSWER, CardDesignProperties(answer)),
        Card("Just like the one we need for House of Cards but who really cares?", CardType.QUESTION,
             CardDesignProperties(answer)),
        Card("And I think it works very well and it's really cool", CardType.ANSWER, CardDesignProperties(question)),
        Card("BTW if you don't think so you can bite me", CardType.QUESTION, CardDesignProperties(answer)),
        Card("So now that it's ready I can finally tell you what I need properly", CardType.ANSWER,
             CardDesignProperties(question)),
        Card("This is the way. Couldn't do it in any other way", CardType.QUESTION, CardDesignProperties(answer)),
        Card("Are you ready for it?", CardType.QUESTION, CardDesignProperties(question)),
        Card("I'm sure you want to hear it already", CardType.ANSWER, CardDesignProperties(answer)),
        Card("So here it comes", CardType.QUESTION, CardDesignProperties(question)),
        Card("I'M BATMANNNNNNNNNNNNNNNN", CardType.ANSWER, CardDesignProperties(answer))
    ]


if __name__ == '__main__':
    configuration = load_configurations()
    output_path = "output.pdf"
    cards = get_cards_list(configuration)
    exporter = generate_cards_exporter(configuration)
    exporter.export_cards(cards=cards, output_path=output_path)
