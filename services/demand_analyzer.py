
from datetime import datetime


class DemandAnalyzer:

    def __init__(self, trips):
        self.trips = trips

    def get_time_slot(self, request_time):

        request_datetime = datetime.fromisoformat(
            request_time
        )

        hour = request_datetime.hour

        if 6 <= hour < 9:
            return "06-09"

        elif 9 <= hour < 12:
            return "09-12"

        elif 12 <= hour < 15:
            return "12-15"

        elif 15 <= hour < 18:
            return "15-18"

        elif 18 <= hour < 21:
            return "18-21"

        elif 21 <= hour < 24:
            return "21-00"

        else:
            return "00-06"

    def demand_by_time_slot(self):

        result = {
            "06-09": 0,
            "09-12": 0,
            "12-15": 0,
            "15-18": 0,
            "18-21": 0,
            "21-00": 0,
            "00-06": 0
        }

        for trip in self.trips:

            if not trip.request_time:
                continue

            time_slot = self.get_time_slot(
                trip.request_time
            )

            result[time_slot] += 1

        return result

    def demand_by_zone(self, zone):

        result = {
            "06-09": 0,
            "09-12": 0,
            "12-15": 0,
            "15-18": 0,
            "18-21": 0,
            "21-00": 0,
            "00-06": 0
        }

        for trip in self.trips:

            if trip.pickup_zone != zone:
                continue

            if not trip.request_time:
                continue

            time_slot = self.get_time_slot(
                trip.request_time
            )

            result[time_slot] += 1

        return result

    def demand_by_zone_and_time(self):

        result = {}

        for trip in self.trips:

            if not trip.request_time:
                continue

            zone = trip.pickup_zone

            time_slot = self.get_time_slot(
                trip.request_time
            )

            if zone not in result:

                result[zone] = {
                    "06-09": 0,
                    "09-12": 0,
                    "12-15": 0,
                    "15-18": 0,
                    "18-21": 0,
                    "21-00": 0,
                    "00-06": 0
                }

            result[zone][time_slot] += 1

        return result

