import pytest
from datetime import datetime
from appointmentTemplate import OrthodonticAppointment  # Replace 'your_module' with the name of your module

@pytest.fixture
def valid_appointment():
    return OrthodonticAppointment(
        doctor_name="Dr. Smith",
        patient_name="John Doe",
        appointment_type="tooth extraction",
        date_time=datetime(2024, 8, 30, 10, 0),
        note="Please arrive 10 minutes early.",
        created_by="Receptionist",
        clinic_contact="555-1234"
    )

@pytest.fixture
def invalid_appointment():
    return OrthodonticAppointment(
        doctor_name="",
        patient_name="",
        appointment_type="unknown",
        date_time="invalid_date",
        note="",
        created_by="",
        clinic_contact=""
    )

def test_valid_appointment(valid_appointment):
    result = valid_appointment.schedule_appointment()
    assert "Appointment confirmed:" in result

def test_invalid_appointment(invalid_appointment):
    result = invalid_appointment.schedule_appointment()
    assert result == "Appointment details are invalid."
