from collections import defaultdict


class UtilizationAnalyzer:

    def __init__(self, activities):
        self.activities = activities

    def _group_by_driver(self):
        grouped = defaultdict(list)

        for activity in self.activities:
            grouped[activity.driver_id].append(activity)

        for driver_id in grouped:
            grouped[driver_id].sort(
                key=lambda activity: activity.get_datetime()
            )

        return grouped

    def calculate_hours(self, driver_id):
        grouped = self._group_by_driver()

        if driver_id not in grouped:
            return {
                "online_hours": 0,
                "busy_hours": 0,
                "idle_hours": 0,
                "utilization": 0
            }

        activities = grouped[driver_id]

        online_hours = 0
        busy_hours = 0
        idle_hours = 0

        for i in range(len(activities) - 1):
            current = activities[i]
            next_activity = activities[i + 1]

            hours = (
                next_activity.get_datetime()
                - current.get_datetime()
            ).total_seconds() / 3600

            if current.is_online():
                online_hours += hours

            elif current.is_busy():
                busy_hours += hours

            elif current.is_idle():
                idle_hours += hours

        total_active_hours = (
            online_hours +
            busy_hours +
            idle_hours
        )

        if total_active_hours == 0:
            utilization = 0
        else:
            utilization = (
                busy_hours / total_active_hours
            ) * 100

        return {
            "online_hours": online_hours,
            "busy_hours": busy_hours,
            "idle_hours": idle_hours,
            "utilization": utilization
        }

    def get_driver_utilization(self, driver_id):
        result = self.calculate_hours(driver_id)

        result["driver_id"] = driver_id

        return result

    def all_driver_utilization(self):
        driver_ids = []

        for activity in self.activities:
            if activity.driver_id not in driver_ids:
                driver_ids.append(activity.driver_id)

        results = []

        for driver_id in driver_ids:
            results.append(
                self.get_driver_utilization(driver_id)
            )

        return results