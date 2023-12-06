from dataclasses import dataclass


@dataclass
class CardDesignProperties:
    title: str
    sign: str
    design_id: str

    def __init__(self, json_dict: dict):
        self.title = json_dict["title"]
        self.sign = json_dict["sign"]
        self.design_id = json_dict["design_id"]
