import uuid

import pytest

from src.models.repositories.emails_to_invite_repository import EmailsToInviteRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="database interaction")
def test_register_email() -> None:
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email_trip_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "email": "mirian.quispe@wivenn.com",
    }

    emails_to_invite_repository.register_email(email_trip_infos)


@pytest.mark.skip(reason="database interaction")
def test_find_email_from_trip():
    conn = db_connection_handler.get_connection()
    emails_to_invite_repository = EmailsToInviteRepository(conn)

    email = emails_to_invite_repository.find_email_from_trip(trip_id)
    print("\n\n", email)
