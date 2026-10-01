class TripAnalyzer:

    def __init__(self, trips):
        self.trips = trips

    def total_trips(self):
        return len(self.trips)

    def completed_trips(self):
        count = 0

        for trip in self.trips:
            if trip.is_completed():
                count += 1

        return count

    def cancelled_trips(self):
        count = 0

        for trip in self.trips:
            if trip.is_cancelled():
                count += 1

        return count

    def completion_rate(self):
        total = self.total_trips()

        if total == 0:
            return 0

        return (self.completed_trips() / total) * 100

    def cancellation_rate(self):
        total = self.total_trips()

        if total == 0:
            return 0

        return (self.cancelled_trips() / total) * 100

    def total_revenue(self):
        revenue = 0

        for trip in self.trips:
            if trip.is_completed():
                revenue += trip.fare

        return revenue

    def average_fare(self):
        completed = []

        for trip in self.trips:
            if trip.is_completed():
                completed.append(trip.fare)

        if len(completed) == 0:
            return 0

        return sum(completed) / len(completed)

    def average_distance(self):
        completed = []

        for trip in self.trips:
            if trip.is_completed():
                completed.append(trip.distance_km)

        if len(completed) == 0:
            return 0

        return sum(completed) / len(completed)

    def average_trip_duration(self):
        durations = []

        for trip in self.trips:
            if trip.is_completed():
                durations.append(
                    trip.calculate_duration()
                )

        if len(durations) == 0:
            return 0

        return sum(durations) / len(durations)

    def summary(self):
        return {
            "total_trips": self.total_trips(),
            "completed_trips": self.completed_trips(),
            "cancelled_trips": self.cancelled_trips(),
            "completion_rate": self.completion_rate(),
            "cancellation_rate": self.cancellation_rate(),
            "total_revenue": self.total_revenue(),
            "average_fare": self.average_fare(),
            "average_distance": self.average_distance(),
            "average_trip_duration": self.average_trip_duration()
        }