from typing import Dict


class ActivityFinder:
    def __init__(self, activity_repository) -> None:
        self.__activity_repository = activity_repository

    def find(self, trip_id) -> Dict:
        try:
            activities = self.__activity_repository.find_activities_from_trip(trip_id)

            activity_list = []
            for activity in activities:
                activity_list.append(
                    {"id": activity[0], "title": activity[2], "occurs_at": activity[3]}
                )

            return {
                "body": {"activities": activity_list},
                "status_code": 200,
            }

        except Exception as exception:
            return {
                "body": {"error": "Bad Request", "message": str(exception)},
                "status_code": 400,
            }
