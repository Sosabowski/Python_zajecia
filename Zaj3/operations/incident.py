
import datetime
import importlib
from fleet.ambulance import Ambulance


class Incident:
    __max_id=0
    def __init__(self, id, description, priority, reported_time, reporter_info, ambulance, location):
        self.id = id
        self.description = description
        self.priority = priority
        self.reported_time = reported_time
        self.reporter_info = reporter_info
        self.ambulance = ambulance
        self.location = location
        Incident.__max_id += 1

    def __repr__(self):
        return (f"Incident(id={self.id!r}, description={self.description!r}, "
                f"priority={self.priority!r}, reported_time={self.reported_time!r}, "
                f"reporter_info={self.reporter_info!r}, ambulance={self.ambulance.id!r}, location={self.location!r})")

    def __str__(self):
        return (f"Incident {self.id}: {self.description}\n"
                f"Priority: {self.priority}\n"
                f"Reported Time: {self.reported_time}\n"
                f"Reporter Info: {self.reporter_info}\n"
                f"Responding ambulace: {self.ambulance.id}\n"
                f"Location: {self.location}")
    