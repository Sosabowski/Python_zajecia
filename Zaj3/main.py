from fleet.ambulance import Ambulance
from fleet.station import Station
from operations import *
from personnel import *


def run_application():
    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance(1, "Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance2 = Ambulance(2, "Type B", "on mission", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])

    employee1 = Employee("John", "Doe", 123, 12000.0)
    employee2 = Employee("Jane", "Smith", 124, 8000.0)

    driver1 = Driver("Mike", "Johnson", 125, 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 126, 11500.0, "DL12346", ["ALS", "PHTLS"])

    station1 = Station(1, (50.095340, 18.920282), ambulance1, driver1, employee1)
    station2 = Station(1, (50.154789, 18.528458), ambulance2, driver2, employee2)


    # sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")
    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # sprawdzanie ile mamy stacji
    print(Station.get_instances_count())

    # stworzenie kolejki
    queue = IncidentQueue()

    # zaraportowanie 2 zgłoszeń
    incident1 = Incident(1, "Power outage in sector 4",1, "Szymon Trojan", '2024-07-30 18:13', ambulance1, (50.087542, 18.213769))
    incident2 = Incident(2, "Fire alarm in building 21",1, "Bartlomiej Skora", '2024-07-30 18:11', ambulance2, (51.087542, 19.213769))
    queue += incident1
    queue += incident2

    # wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)

    # daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")

    print(station1.check_location())
    print(station2.check_location())

    print(ambulance1.check_availability())
    print(ambulance2.check_availability())

    print(ambulance1.check_distance_from_incident())
    print(ambulance2.check_distance_from_incident())

if __name__ == "__main__":
    run_application()