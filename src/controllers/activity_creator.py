import uuid
from typing import Dict


class ActivityCreator:
    def __init__(self, activity_repository) -> None:
        self.__activity_repository = activity_repository

    def create(self, body: Dict, trip_id) -> Dict:
        try:
            activity_id = str(uuid.uuid4())

            activity_infos = {
                "id": activity_id,
                "trip_id": trip_id,
                "title": body["title"],
                "occurs_at": body["occurs_at"],
            }

            self.__activity_repository.register_activity(activity_infos)

            return {
                "body": {"activityId": activity_id},
                "status_code": 200,
            }

        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
