import uuid

import pytest

from src.models.repositories.activities_repository import ActivitiesRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="database interaction")
def test_register_activity() -> None:
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    activity_info = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "title": "Trilha no Salar de Uyuni",
        "occurs_at": "15-05-2025",
    }

    activities_repository.register_activity(activity_info)


@pytest.mark.skip(reason="database interaction")
def test_find_activities_from_trip():
    conn = db_connection_handler.get_connection()
    activities_repository = ActivitiesRepository(conn)

    response = activities_repository.find_activities_from_trip(trip_id)
    print("\n\n", response)

    assert isinstance(response, list)
    assert isinstance(response[0], tuple)
