from sqlite3 import Connection
from typing import Dict, List, Tuple


class EmailsToInviteRepository:
    def __init__(self, conn: Connection) -> None:
        self.__conn = conn

    def register_email(self, email_trip_infos: Dict) -> None:
        cursor = self.__conn.cursor()
        cursor.execute(
            """
                INSERT INTO emails_to_invite 
                    (id, trip_id, email)
                VALUES 
                    (?, ?, ?)
            """,
            (
                email_trip_infos["id"],
                email_trip_infos["trip_id"],
                email_trip_infos["email"],
            ),
        )
        self.__conn.commit()

    def find_email_from_trip(self, trip_id: str) -> List[Tuple]:
        cursor = self.__conn.cursor()
        cursor.execute(
            """SELECT * FROM 
                emails_to_invite 
            WHERE 
                trip_id = ?""",
            (trip_id,),
        )
        email = cursor.fetchall()
        return email