from dataclasses import dataclass
from entities.card_type import CardType
from utils.configuration_keys import ConfigurationKeys


@dataclass
class CardDesignProperties:
    title: str
    sign: str
    design_id: str

    def __init__(self, json_dict: dict):
        self.title = json_dict["title"]
        self.sign = json_dict["sign"]
        self.design_id = json_dict["design_id"]

    @staticmethod
    def GetDesignPropertiesConfigurationKey(card_type: CardType) -> str:
        return ConfigurationKeys.QUESTION_DESIGN_PROPERTIES_KEY if card_type == CardType.QUESTION \
            else ConfigurationKeys.ANSWER_DESIGN_PROPERTIES_KEY
