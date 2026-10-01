class ZoneAnalyzer:

    def __init__(self, trips):
        self.trips = trips

    def total_trips(self, zone):
        count = 0

        for trip in self.trips:
            if trip.pickup_zone == zone:
                count += 1

        return count

    def completed_trips(self, zone):
        count = 0

        for trip in self.trips:
            if trip.pickup_zone == zone:
                if trip.is_completed():
                    count += 1

        return count

    def cancelled_trips(self, zone):
        count = 0

        for trip in self.trips:
            if trip.pickup_zone == zone:
                if trip.is_cancelled():
                    count += 1

        return count

    def completion_rate(self, zone):
        total = self.total_trips(zone)

        if total == 0:
            return 0

        completed = self.completed_trips(zone)

        return (completed / total) * 100

    def cancellation_rate(self, zone):
        total = self.total_trips(zone)

        if total == 0:
            return 0

        cancelled = self.cancelled_trips(zone)

        return (cancelled / total) * 100

    def total_revenue(self, zone):
        revenue = 0

        for trip in self.trips:
            if trip.pickup_zone == zone:
                if trip.is_completed():
                    revenue += trip.fare

        return revenue

    def average_fare(self, zone):
        total_fare = 0
        completed_count = 0

        for trip in self.trips:
            if trip.pickup_zone == zone:
                if trip.is_completed():
                    total_fare += trip.fare
                    completed_count += 1

        if completed_count == 0:
            return 0

        return total_fare / completed_count

    def get_zones(self):
        zones = []

        for trip in self.trips:
            if trip.pickup_zone not in zones:
                zones.append(trip.pickup_zone)

        return zones

    def get_zone_summary(self, zone):
        return {
            "zone": zone,
            "total_trips": self.total_trips(zone),
            "completed_trips": self.completed_trips(zone),
            "cancelled_trips": self.cancelled_trips(zone),
            "completion_rate": self.completion_rate(zone),
            "cancellation_rate": self.cancellation_rate(zone),
            "total_revenue": self.total_revenue(zone),
            "average_fare": self.average_fare(zone)
        }

    def all_zone_summaries(self):
        summaries = []

        for zone in self.get_zones():
            summaries.append(
                self.get_zone_summary(zone)
            )

        return summaries