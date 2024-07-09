from sqlite3 import Connection
from typing import Dict, Tuple


class LinksRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def create_link(self, link_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO links 
                    (id, trip_id, link, title)
                VALUES 
                    (?, ?, ?, ?)
            """,
            (
                link_infos["id"],
                link_infos["trip_id"],
                link_infos["link"],
                link_infos["title"],
            ),
        )
        self.__conn.commit()

    def find_link_by_trip_id(self, trip_id: str) -> Tuple:
        cursor = self.__conn.cursor()
        cursor.execute(
            """SELECT * FROM 
                links 
            WHERE 
                trip_id = ?""",
            (trip_id,),
        )
        link = cursor.fetchone()
        return link
