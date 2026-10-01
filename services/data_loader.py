import csv

from models.driver import Driver
from models.trip import Trip
from models.activity import DriverActivity


class DataLoader:

    def load_drivers(self, file_path):
        drivers = []

        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                driver = Driver(
                    row["driver_id"],
                    row["driver_name"],
                    row["city"],
                    row["vehicle_type"],
                    float(row["rating"]),
                    row["status"]
                )

                drivers.append(driver)

        return drivers

    def load_trips(self, file_path):
        trips = []

        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                trip = Trip(
                    row["trip_id"],
                    row["driver_id"],
                    row["rider_id"],
                    row["city"],
                    row["pickup_zone"],
                    row["drop_zone"],
                    row["request_time"],
                    row["pickup_time"],
                    row["drop_time"],
                    float(row["distance_km"]),
                    float(row["fare"]),
                    row["status"],
                    row["cancellation_reason"]
                )

                trips.append(trip)

        return trips

    def load_activity(self, file_path):
        activities = []

        with open(file_path, "r", newline="") as file:
            reader = csv.DictReader(file)

            for row in reader:
                activity = DriverActivity(
                    row["driver_id"],
                    row["timestamp"],
                    row["status"]
                )

                activities.append(activity)

        return activities