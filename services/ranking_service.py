import heapq


class RankingService:

    def __init__(self, drivers, trips):
        self.drivers = drivers
        self.trips = trips

    def completed_trips_by_driver(self):
        result = {}

        for trip in self.trips:
            if trip.is_completed():

                driver_id = trip.driver_id

                if driver_id not in result:
                    result[driver_id] = 0

                result[driver_id] += 1

        return result

    def revenue_by_driver(self):
        result = {}

        for trip in self.trips:
            if trip.is_completed():

                driver_id = trip.driver_id

                if driver_id not in result:
                    result[driver_id] = 0

                result[driver_id] += trip.fare

        return result

    def trips_by_zone(self):
        result = {}

        for trip in self.trips:

            zone = trip.pickup_zone

            if zone not in result:
                result[zone] = 0

            result[zone] += 1

        return result

    def top_drivers_by_completed_trips(self, k=3):
        data = self.completed_trips_by_driver()

        heap = []

        for driver_id, count in data.items():
            heapq.heappush(
                heap,
                (count, driver_id)
            )

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(
                heapq.heappop(heap)
            )

        result.reverse()

        return result

    def top_drivers_by_revenue(self, k=3):
        data = self.revenue_by_driver()

        heap = []

        for driver_id, revenue in data.items():
            heapq.heappush(
                heap,
                (revenue, driver_id)
            )

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(
                heapq.heappop(heap)
            )

        result.reverse()

        return result

    def top_zones_by_demand(self, k=3):
        data = self.trips_by_zone()

        heap = []

        for zone, count in data.items():
            heapq.heappush(
                heap,
                (count, zone)
            )

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(
                heapq.heappop(heap)
            )

        result.reverse()

        return result

    def trips_by_rider(self):
        result = {}

        for trip in self.trips:
            rider_id = trip.rider_id

            if rider_id not in result:
                result[rider_id] = 0

            result[rider_id] += 1

        return result

    def cancellations_by_zone(self):
        result = {}

        for trip in self.trips:
            if trip.is_cancelled():

                zone = trip.pickup_zone

                if zone not in result:
                    result[zone] = 0

                result[zone] += 1

        return result

    def top_riders_by_trip_count(self, k=3):

        data = self.trips_by_rider()

        heap = []

        for rider_id, count in data.items():

            heapq.heappush(
                heap,
                (count, rider_id)
            )

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(
                heapq.heappop(heap)
            )

        result.reverse()

        return result

    def top_zones_by_cancellation(self, k=3):

        data = self.cancellations_by_zone()

        heap = []

        for zone, count in data.items():

            heapq.heappush(
                heap,
                (count, zone)
            )

            if len(heap) > k:
                heapq.heappop(heap)

        result = []

        while heap:
            result.append(
                heapq.heappop(heap)
            )

        result.reverse()

        return result