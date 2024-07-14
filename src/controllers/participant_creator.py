import uuid
from typing import Dict


class ParticipantCreator:
    def __init__(self, participant_repository, email_repository) -> None:
        self.__participant_repository = participant_repository
        self.__email_repository = email_repository

    def create(self, body: Dict, trip_id) -> Dict:
        try:
            participant_id = uuid.uuid4()
            email_id = uuid.uuid4()

            participant_infos = {
                "id": participant_id,
                "trip_id": trip_id,
                "emails_to_invite_id": email_id,
                "name": body["name"],
            }

            email_to_invite_infos = {
                "id": email_id,
                "trip_id": trip_id,
                "email": body["email"],
            }

            self.__participant_repository.register_participant(participant_infos)
            self.__email_repository.register_email(email_to_invite_infos)

            return {
                "body": {"participantId": participant_id},
                "status_code": 200,
            }

        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
