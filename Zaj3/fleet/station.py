class Station:
    __max_id = 0

    def __init__(self, id, location, ambulance, driver, employee):
        self.id = Station.__max_id
        self.location = location # as (northing, easting)
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        Station.__max_id += 1

    def check_location(self):
        frontText = f"Station number {self.id}: Ambulance number {self.ambulance.id}"
        if (self.location == self.ambulance.location):
            return  frontText + f" In station"
        else:
            return frontText + f" Not in station"
    @classmethod   
    def get_instances_count(cls):
        return f"Number of stations: {cls.__max_id}"