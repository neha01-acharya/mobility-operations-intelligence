from datetime import datetime


class DriverActivity:

    def __init__(self, driver_id, timestamp, status):
        self.driver_id = driver_id
        self.timestamp = timestamp
        self.status = status

    def get_datetime(self):
        return datetime.fromisoformat(self.timestamp)

    def is_online(self):
        return self.status.lower() == "online"

    def is_busy(self):
        return self.status.lower() == "busy"

    def is_idle(self):
        return self.status.lower() == "idle"