import math
from logger_config import setup_logging
class Ambulance:
    __slots__ = ['id', 'vehicle_type', 'status', 'location', 'medical_equipment', 'is_assigned', 'incident_location']
    __max_id = 1

    def __init__(self, id, vehicle_type, status, location, medical_equipment):
        self.id = Ambulance.__max_id
        self.vehicle_type = vehicle_type
        self.status = status  # e.g., "available", "on_mission", "servicing"
        self.location = location # as (northing, easting)
        self.medical_equipment = medical_equipment  # List of medical equipment names
        self.is_assigned = False
        self.incident_location = None

        Ambulance.__max_id += 1

        logger = setup_logging()
        if(location[0] > 90 or location[0] < -90):
            logger.error("Longitude must be in the range (-90, 90) for the ambulance!")
        if(location[1] > 180 or location[1] < -180):
            logger.error("Latitude must be in the range (-180, 180) for the ambulance!")

    def update_location(self, new_location):
        self.location = new_location

    def __eq__(self, other):
        if not isinstance(other, Ambulance):
            return NotImplemented
        return self.id == other.id and self.vehicle_type == other.vehicle_type
    
    def __str__(self):
        return (f"Ambulance ID: {self.id}, Type: {self.vehicle_type}, "
                f"Status: {self.status}, Location: {self.location}, "
                f"Equipment: {', '.join(self.medical_equipment)}")
    
    @staticmethod
    def validate_id(ambulance_id):
        return isinstance(ambulance_id, int) and ambulance_id > 0

    @classmethod
    def get_instances_count(cls):
        return f"Number of working ambulances: {cls.__max_id}"
    
    def check_availability(self):
        status = not self.is_assigned
        if(status == True):
            return f"Ambulance number {self.id} is available"
        else:
            return f"Ambulance number {self.id} is not available"
        
    def check_distance_from_incident(self):
        if (self.incident_location != None):
            distance = math.sqrt( (self.location[0] - self.incident_location[0])**2 + (self.location[1] - self.incident_location[1])**2)
            return f"Ambulance number {self.id} is in the distance {distance} from accident"
        else:
            return f"Ambulance number {self.id} was not dispatched"

if __name__ == "__main__":
    ambulance1 = Ambulance(
        id=0,
        vehicle_type="AZ124",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )
    ambulance2 = Ambulance(
        id=1,
        vehicle_type="AZ2000",
        status="Available",
        location=(50.095340, 19.920282),
        medical_equipment = ["defibrillator", "stretcher"]
    )

    print(ambulance1 == ambulance2)
    print(ambulance1)

# slajd 17 - sloty - odkomentować __slots__
    # ambulance1.whatever = "123"
    # print(ambulance1.whatever)

# slajd 17 - metody statyczne i metody klasy - odkomentować 3 rzeczy u góry
    print(Ambulance.validate_id(123))
    print(Ambulance.validate_id("123"))

    print(Ambulance.get_instances_count())