
class DriverAnalyzer:

    def __init__(self, drivers, trips):
        self.drivers = drivers
        self.trips = trips

    def total_trips(self, driver_id):
        count = 0

        for trip in self.trips:
            if trip.driver_id == driver_id:
                count += 1

        return count

    def completed_trips(self, driver_id):
        count = 0

        for trip in self.trips:
            if trip.driver_id == driver_id:
                if trip.is_completed():
                    count += 1

        return count

    def cancelled_trips(self, driver_id):
        count = 0

        for trip in self.trips:
            if trip.driver_id == driver_id:
                if trip.is_cancelled():
                    count += 1

        return count

    def completion_rate(self, driver_id):
        total = self.total_trips(driver_id)

        if total == 0:
            return 0

        completed = self.completed_trips(driver_id)

        return (completed / total) * 100

    def cancellation_rate(self, driver_id):
        total = self.total_trips(driver_id)

        if total == 0:
            return 0

        cancelled = self.cancelled_trips(driver_id)

        return (cancelled / total) * 100

    def total_revenue(self, driver_id):
        revenue = 0

        for trip in self.trips:
            if trip.driver_id == driver_id:
                if trip.is_completed():
                    revenue += trip.fare

        return revenue

    def average_fare(self, driver_id):
        total_fare = 0
        completed_count = 0

        for trip in self.trips:
            if trip.driver_id == driver_id:
                if trip.is_completed():
                    total_fare += trip.fare
                    completed_count += 1

        if completed_count == 0:
            return 0

        return total_fare / completed_count

    def average_distance(self, driver_id):
        total_distance = 0
        completed_count = 0

        for trip in self.trips:
            if trip.driver_id == driver_id:
                if trip.is_completed():
                    total_distance += trip.distance_km
                    completed_count += 1

        if completed_count == 0:
            return 0

        return total_distance / completed_count

    def fare_per_km(self, driver_id):
        total_fare = 0
        total_distance = 0

        for trip in self.trips:
            if trip.driver_id == driver_id:
                if trip.is_completed():
                    total_fare += trip.fare
                    total_distance += trip.distance_km

        if total_distance == 0:
            return 0

        return total_fare / total_distance

    def get_driver(self, driver_id):
        for driver in self.drivers:
            if driver.driver_id == driver_id:
                return driver

        return None

    def get_profile(self, driver_id):
        driver = self.get_driver(driver_id)

        if driver is None:
            return None

        return {
            "driver_id": driver.driver_id,
            "driver_name": driver.driver_name,
            "city": driver.city,
            "vehicle_type": driver.vehicle_type,
            "rating": driver.rating,
            "status": driver.status,
            "total_trips": self.total_trips(driver_id),
            "completed_trips": self.completed_trips(driver_id),
            "cancelled_trips": self.cancelled_trips(driver_id),
            "completion_rate": self.completion_rate(driver_id),
            "cancellation_rate": self.cancellation_rate(driver_id),
            "total_revenue": self.total_revenue(driver_id),
            "average_fare": self.average_fare(driver_id),
            "average_distance": self.average_distance(driver_id),
            "fare_per_km": self.fare_per_km(driver_id)
        }

