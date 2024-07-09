import uuid

import pytest

from src.models.repositories.links_repository import LinksRepository
from src.models.settings.db_connection_handler import db_connection_handler

db_connection_handler.connect()
trip_id = str(uuid.uuid4())


@pytest.mark.skip(reason="database interaction")
def test_create_linkl() -> None:
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    link_infos = {
        "id": str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "https://docs.python.org/3/library/",
        "title": "Viagem a Ubatuba",
    }

    links_repository.create_link(link_infos)


@pytest.mark.skip(reason="database interaction")
def test_find_link_by_trip_id():
    conn = db_connection_handler.get_connection()
    links_repository = LinksRepository(conn)

    email = links_repository.find_link_by_trip_id(trip_id)
    print("\n\n", email)