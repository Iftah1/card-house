import sqlite3
from card_house.db.cards_db_columns import CardsDBColumns

from typing import List, Any, Dict

from card_house.infrastructure.entities.card_type import CardType
from card_house.infrastructure.entities.db_card import DBCard
from card_house.db.iclient_db import IClientDB


class CardsDB(IClientDB):
    def __init__(self, db_name: str):
        self.db_name = db_name
        self.create_cards_table()

    def create_cards_table(self):
        create_table_query = """
            CREATE TABLE IF NOT EXISTS cards (
                id INTEGER PRIMARY KEY,
                card_id TEXT NOT NULL,
                type TEXT NOT NULL,
                content TEXT NOT NULL,
                creation_time DATETIME NOT NULL,
                version TEXT NOT NULL
            )
        """
        self.execute_query(create_table_query)

    def add_card(self, card: DBCard) -> str:
        insert_query = f"""
            INSERT INTO cards (content, version, creation_time, card_id, type)
            VALUES ('{card.content}', '{card.version}', '{card.creation_time}', '{card.card_id}', '{card.type.value}')
        """
        self.execute_query(insert_query)
        return card.card_id

    def remove_card(self, card_id: str) -> bool:
        delete_query = f"""
            DELETE FROM cards
            WHERE card_id = '{card_id}'
        """
        self.execute_query(delete_query)
        return True

    def get_cards(self, card_properties: Dict[str, Any]) -> List[DBCard]:
        select_query = """
            SELECT * FROM cards where 1 = 1
        """
        for key, value in card_properties.items():
            select_query += f" and {key} = '{value}'"
        resulted_cards = self.execute_query(select_query)
        cards = []
        for card in resulted_cards:
            cards.append(
                DBCard(
                    card_id=card[CardsDBColumns.CARD_ID_COLUM],
                    type=CardType(card[CardsDBColumns.TYPE_COLUM]),
                    content=card[CardsDBColumns.CONTENT_COLUM],
                    creation_time=card[CardsDBColumns.CREATION_TIME_COLUM],
                    version=card[CardsDBColumns.VERSION_COLUM],
                )
            )
        return cards

    def execute_query(self, query: str) -> Any:
        conn, cursor = self.get_db_connection()
        cursor.execute(query)
        result = cursor.fetchall()
        conn.commit()
        conn.close()
        return result

    def get_db_connection(self):
        conn = sqlite3.connect(self.db_name)
        return conn, conn.cursor()
