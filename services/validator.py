from datetime import datetime


class DataValidator:

    def validate_drivers(self, drivers):
        errors = []

        for driver in drivers:

            if not driver.driver_id:
                errors.append("Driver ID is missing")

            if not driver.driver_name:
                errors.append(
                    f"Driver name is missing for {driver.driver_id}"
                )

            if driver.rating < 0 or driver.rating > 5:
                errors.append(
                    f"Invalid rating for driver {driver.driver_id}"
                )

        return errors

    def validate_trips(self, trips, drivers):

        errors = []

        driver_ids = set()

        for driver in drivers:
            driver_ids.add(driver.driver_id)

        for trip in trips:

            # Check driver ID
            if trip.driver_id not in driver_ids:
                errors.append(
                    f"Unknown driver_id {trip.driver_id} "
                    f"in trip {trip.trip_id}"
                )

            # Check negative fare
            if trip.fare < 0:
                errors.append(
                    f"Negative fare in trip {trip.trip_id}"
                )

            # Check negative distance
            if trip.distance_km < 0:
                errors.append(
                    f"Negative distance in trip {trip.trip_id}"
                )

            # Completed trips must have pickup and drop times
            if trip.is_completed():

                if not trip.pickup_time:
                    errors.append(
                        f"Missing pickup_time in completed trip "
                        f"{trip.trip_id}"
                    )

                if not trip.drop_time:
                    errors.append(
                        f"Missing drop_time in completed trip "
                        f"{trip.trip_id}"
                    )

            # Validate timestamps when available
            if trip.pickup_time and trip.drop_time:

                try:
                    pickup = datetime.fromisoformat(
                        trip.pickup_time
                    )

                    drop = datetime.fromisoformat(
                        trip.drop_time
                    )

                    if drop < pickup:
                        errors.append(
                            f"Drop time is before pickup time "
                            f"in trip {trip.trip_id}"
                        )

                except ValueError:
                    errors.append(
                        f"Invalid timestamp in trip {trip.trip_id}"
                    )

        return errors

    def validate(self, drivers, trips):

        driver_errors = self.validate_drivers(drivers)

        trip_errors = self.validate_trips(
            trips,
            drivers
        )

        return driver_errors + trip_errors