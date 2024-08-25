# test_appointment.py
import pytest
from appointmentTemplate import ToothExtractionAppointment, MonthlyRubberBandChangeAppointment, \
    RemovalOfBracesAppointment, FittingOfBracesAppointment

@pytest.fixture
def appointment_data():
    """Fixture for providing data for creating appointments."""
    return {
        "doctor_name": "Dr. Smith",
        "patient_name": "John Doe",
        "date": "2023-12-25",
        "time": "10:00 AM",
        "note": "Please bring your insurance card",
        "creator_name": "Alice",
        "clinic_contact": "+1234567890"
    }

def test_tooth_extraction_appointment(appointment_data):
    """Tests creating a tooth extraction appointment."""
    appointment = ToothExtractionAppointment(**appointment_data)
    assert appointment.get_appointment_type() == "Tooth Extraction"
    assert appointment.get_appointment_details() == {
        "doctor_name": appointment_data["doctor_name"],
        "patient_name": appointment_data["patient_name"],
        "appointment_type": "Tooth Extraction",
        "date": appointment_data["date"],
        "time": appointment_data["time"],
        "note": appointment_data["note"],
        "creator_name": appointment_data["creator_name"],
        "clinic_contact": appointment_data["clinic_contact"]
    }

def test_monthly_rubber_band_change_appointment(appointment_data):
    """Tests creating a monthly rubber band change appointment."""
    appointment = MonthlyRubberBandChangeAppointment(**appointment_data)
    assert appointment.get_appointment_type() == "Monthly Rubber Band Change"
    assert appointment.get_appointment_details() == {
        "doctor_name": appointment_data["doctor_name"],
        "patient_name": appointment_data["patient_name"],
        "appointment_type": "Monthly Rubber Band Change",
        "date": appointment_data["date"],
        "time": appointment_data["time"],
        "note": appointment_data["note"],
        "creator_name": appointment_data["creator_name"],
        "clinic_contact": appointment_data["clinic_contact"]
    }

def test_removal_of_braces_appointment(appointment_data):
    """Tests creating a removal of braces appointment."""
    appointment = RemovalOfBracesAppointment(**appointment_data)
    assert appointment.get_appointment_type() == "Removal of Braces"
    assert appointment.get_appointment_details() == {
        "doctor_name": appointment_data["doctor_name"],
        "patient_name": appointment_data["patient_name"],
        "appointment_type": "Removal of Braces",
        "date": appointment_data["date"],
        "time": appointment_data["time"],
        "note": appointment_data["note"],
        "creator_name": appointment_data["creator_name"],
        "clinic_contact": appointment_data["clinic_contact"]
    }

def test_fitting_of_braces_appointment(appointment_data):
    """Tests creating a fitting of braces appointment."""
    appointment = FittingOfBracesAppointment(**appointment_data)
    assert appointment.get_appointment_type() == "Fitting of Braces"
    assert appointment.get_appointment_details() == {
        "doctor_name": appointment_data["doctor_name"],
        "patient_name": appointment_data["patient_name"],
        "appointment_type": "Fitting of Braces",
        "date": appointment_data["date"],
        "time": appointment_data["time"],
        "note": appointment_data["note"],
        "creator_name": appointment_data["creator_name"],
        "clinic_contact": appointment_data["clinic_contact"]
    }
