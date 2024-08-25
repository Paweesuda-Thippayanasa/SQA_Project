import pytest
from datetime import datetime
from appointmentTemplate import create_appointment, ToothExtractionAppointment, FittingOfBracesAppointment

# Fixture for sample appointment data
@pytest.fixture
def sample_appointment_data():
    return {
        "doctor_name": "Dr. Smith",
        "patient_name": "John Doe",
        "date_time": datetime(2024, 8, 30, 14, 0),
        "created_by": "Receptionist",
        "clinic_contact": "123-456-7890"
    }

def test_tooth_extraction_appointment(sample_appointment_data):
    appointment = create_appointment(
        ToothExtractionAppointment,
        **sample_appointment_data
    )
    assert appointment.doctor_name == "Dr. Smith"
    assert appointment.patient_name == "John Doe"
    assert appointment.date_time == datetime(2024, 8, 30, 14, 0)
    assert appointment.created_by == "Receptionist"
    assert appointment.clinic_contact == "123-456-7890"
    assert appointment.note == "Please take painkillers after the extraction."

def test_braces_fitting_appointment(sample_appointment_data):
    appointment = create_appointment(
        FittingOfBracesAppointment,
        **sample_appointment_data
    )
    assert appointment.doctor_name == "Dr. Smith"
    assert appointment.patient_name == "John Doe"
    assert appointment.date_time == datetime(2024, 8, 30, 14, 0)
    assert appointment.created_by == "Receptionist"
    assert appointment.clinic_contact == "123-456-7890"
    assert appointment.note == "Please take painkillers after the extraction."

if __name__ == "__main__":
    pytest.main()
