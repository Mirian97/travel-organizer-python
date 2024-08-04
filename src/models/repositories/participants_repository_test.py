import uuid

from src.models.repositories.participants_repository import ParticipantsRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())
participant_id = str(uuid.uuid4())


def test_register_participant() -> None:
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participant_infos = {
        "id": participant_id,
        "trip_id": trip_id,
        "emails_to_invite_id": 2,
        "name": "Mirian Quispe",
    }
    participants_repository.register_participant(participant_infos)


def test_find_participants_from_trip() -> None:
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    response = participants_repository.find_participants_from_trip(trip_id)
    print("\n\n", response)

    assert isinstance(response, list)


def test_update_participant_status() -> None:
    conn = db_connection_handler.get_connection()
    participants_repository = ParticipantsRepository(conn)

    participants_repository.update_participant_status(participant_id)
