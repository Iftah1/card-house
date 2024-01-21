from dataclasses import dataclass
from typing import List, Dict, Any

Row = List["PrintedCard"]
Page = List[Row]


class PrintedCard:
    def __init__(self, content: str, design_properties: Dict[str, Any]):
        self.content = content
        self.title = design_properties["title"]
        self.sign = design_properties["sign"]
        self.design_id = design_properties["design_id"]
