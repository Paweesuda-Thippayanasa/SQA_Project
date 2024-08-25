import pytest
from datetime import datetime
from appointmentTemplate import (
    ToothExtractionAppointment,
    RubberBandChangeAppointment,
    BracesRemovalAppointment,
    BracesFittingAppointment,
)

# Test Fixture for Appointment Data
@pytest.fixture
def appointment_data():
    return {
        "doctor_name": "Dr. Smith",
        "patient_name": "John Doe",
        "appointment_type": "Tooth Extraction",
        "appointment_datetime": datetime(2024, 3, 15, 10, 0),
        "note": "Prepare for extraction",
        "created_by": "Receptionist",
    }

# Test Cases using the Fixture

def test_tooth_extraction_appointment(appointment_data):
    appointment = ToothExtractionAppointment().schedule_appointment(**appointment_data)
    assert appointment["doctor_name"] == appointment_data["doctor_name"]
    assert appointment["appointment_type"] == appointment_data["appointment_type"]

def test_rubber_band_change_appointment(appointment_data):
    appointment_data["appointment_type"] = "Rubber Band Change"
    appointment = RubberBandChangeAppointment().schedule_appointment(**appointment_data)
    assert appointment["appointment_type"] == "Rubber Band Change"

def test_braces_removal_appointment(appointment_data):
    appointment_data["appointment_type"] = "Braces Removal"
    appointment = BracesRemovalAppointment().schedule_appointment(**appointment_data)
    assert appointment["appointment_type"] == "Braces Removal"

def test_braces_fitting_appointment(appointment_data):
    appointment_data["appointment_type"] = "Braces Fitting"
    appointment = BracesFittingAppointment().schedule_appointment(**appointment_data)
    assert appointment["appointment_type"] == "Braces Fitting"

# Add more test cases for edge cases and validation logic
