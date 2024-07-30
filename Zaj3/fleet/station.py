from logger_config import setup_logging
class Station:
    __max_id = 0

    def __init__(self, id, location, ambulance, driver, employee):
        self.id = Station.__max_id
        self.location = location # as (northing, easting)
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee
        Station.__max_id += 1

        logger = setup_logging()
        if(location[0] > 90 or location[0] < -90):
            logger.error("Longitude must be in the range (-90, 90) for the station!")
        if(location[1] > 180 or location[1] < -180):
            logger.error("Latitude must be in the range (-180, 180) for the station!")

    def check_location(self):
        frontText = f"Station number {self.id}: Ambulance number {self.ambulance.id}"
        if (self.location == self.ambulance.location):
            return  frontText + f" In station"
        else:
            return frontText + f" Not in station"
    @classmethod   
    def get_instances_count(cls):
        return f"Number of stations: {cls.__max_id}"