from dataclasses import dataclass
from typing import List, Dict, Any

Row = List["PrintedCard"]
Page = List[Row]


@dataclass
class PrintedCard:
    content: str
    title: str
    sign: str
    design_id: str

    def __init__(self, content: str, design_properties: Dict[str, Any]):
        self.content = content
        self.title = design_properties["title"]
        self.sign = design_properties["sign"]
        self.design_id = design_properties["design_id"]