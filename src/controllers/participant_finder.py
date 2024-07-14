from typing import Dict


class ParticipantFinder:
    def __init__(self, participant_repository) -> None:
        self.__participant_repository = participant_repository

    def find(self, trip_id) -> Dict:
        try:
            participants = self.__participant_repository.find_participants_from_trip(
                trip_id
            )

            participant_list = []

            for partipant in participants:
                participant_list.append(
                    {
                        "id": partipant[0],
                        "name": partipant[1],
                        "is_confirmed": partipant[2],
                        "email": partipant[3],
                    }
                )

            return {
                "body": {"participants": participant_list},
                "status_code": 200,
            }

        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
