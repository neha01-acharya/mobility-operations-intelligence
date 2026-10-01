class AnomalyDetector:

    def __init__(self, trips, drivers):
        self.trips = trips
        self.drivers = drivers

    def cancellation_by_reason(self):
        result = {}

        for trip in self.trips:
            if trip.is_cancelled():

                reason = trip.cancellation_reason

                if not reason:
                    reason = "unknown"

                if reason not in result:
                    result[reason] = 0

                result[reason] += 1

        return result

    def cancellation_by_zone(self):
        result = {}

        for trip in self.trips:
            if trip.is_cancelled():

                zone = trip.pickup_zone

                if zone not in result:
                    result[zone] = 0

                result[zone] += 1

        return result

    def cancellation_by_driver(self):
        result = {}

        for trip in self.trips:
            if trip.is_cancelled():

                driver_id = trip.driver_id

                if driver_id not in result:
                    result[driver_id] = 0

                result[driver_id] += 1

        return result

    def zero_distance_trips(self):
        anomalies = []

        for trip in self.trips:
            if trip.distance_km == 0:
                anomalies.append(trip.trip_id)

        return anomalies

    def negative_fare_trips(self):
        anomalies = []

        for trip in self.trips:
            if trip.fare < 0:
                anomalies.append(trip.trip_id)

        return anomalies

    def invalid_duration_trips(self):
        anomalies = []

        for trip in self.trips:

            if trip.pickup_time and trip.drop_time:

                duration = trip.calculate_duration()

                if duration < 0:
                    anomalies.append(trip.trip_id)

        return anomalies

    def unknown_driver_trips(self):
        driver_ids = set()

        for driver in self.drivers:
            driver_ids.add(driver.driver_id)

        anomalies = []

        for trip in self.trips:
            if trip.driver_id not in driver_ids:
                anomalies.append(trip.trip_id)

        return anomalies

    def long_duration_trips(self, threshold_minutes=180):
        anomalies = []

        for trip in self.trips:

            if trip.is_completed():

                duration = trip.calculate_duration()

                if duration > threshold_minutes:
                    anomalies.append(trip.trip_id)

        return anomalies

    def get_all_anomalies(self):
        return {
            "zero_distance": self.zero_distance_trips(),
            "negative_fare": self.negative_fare_trips(),
            "invalid_duration": self.invalid_duration_trips(),
            "unknown_driver": self.unknown_driver_trips(),
            "long_duration": self.long_duration_trips()
        }
    def cancellation_by_time(self):

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

            if not trip.is_cancelled():
                continue

            if not trip.request_time:
                continue

            hour = int(
                trip.request_time[11:13]
            )

            if 6 <= hour < 9:
                result["06-09"] += 1

            elif 9 <= hour < 12:
                result["09-12"] += 1

            elif 12 <= hour < 15:
                result["12-15"] += 1

            elif 15 <= hour < 18:
                result["15-18"] += 1

            elif 18 <= hour < 21:
                result["18-21"] += 1

            elif 21 <= hour < 24:
                result["21-00"] += 1

            else:
                result["00-06"] += 1

        return result