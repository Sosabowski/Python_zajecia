import pytest
from fleet.ambulance import Ambulance

@pytest.fixture
def ambulance():
    return Ambulance(1, "Type A", "available", (64.095340, 90.920282), ["Defibrillator", "Oxygen tank"])

def test_initialization(ambulance):
    assert ambulance.id == 1
    assert ambulance.vehicle_type == "Type A"
    assert ambulance.status == "available"
    assert ambulance.location == (64.095340, 90.920282)
    assert ambulance.medical_equipment == ["Defibrillator", "Oxygen tank"]

def test_check_availability(ambulance):
    result = ambulance.check_availability()
    print(f"Expected: 'Ambulance number 2 is available', Actual: {repr(result)}")
    assert result == 'Ambulance number 2 is available'
    
    ambulance.is_assigned = True
    result = ambulance.check_availability()
    print(f"Expected: 'Ambulance number 2 is not available', Actual: {repr(result)}")
    assert result == 'Ambulance number 2 is not available'