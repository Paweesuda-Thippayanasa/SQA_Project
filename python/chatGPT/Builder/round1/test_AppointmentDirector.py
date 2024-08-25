import pytest
from datetime import datetime
from AppointmentBuilder import AppointmentBuilder
from AppointmentDirector import AppointmentDirector

@pytest.fixture
def builder():
    return AppointmentBuilder()

@pytest.fixture
def director(builder):
    return AppointmentDirector(builder)

def test_tooth_extraction_appointment(director):
    appointment = director.create_tooth_extraction_appointment(
        doctor_name="Dr. Smith",
        patient_name="John Doe",
        date_time=datetime(2024, 9, 1, 10, 0),
        note="Bring previous x-rays.",
        creator_name="Receptionist Jane",
        clinic_contact="123-456-7890"
    )
    assert appointment.doctor_name == "Dr. Smith"
    assert appointment.patient_name == "John Doe"
    assert appointment.appointment_type == "Tooth Extraction"
    assert appointment.date_time == datetime(2024, 9, 1, 10, 0)
    assert appointment.note == "Bring previous x-rays."
    assert appointment.creator_name == "Receptionist Jane"
    assert appointment.clinic_contact == "123-456-7890"

def test_braces_fitting_appointment(director):
    appointment = director.create_braces_fitting_appointment(
        doctor_name="Dr. Brown",
        patient_name="Jane Doe",
        date_time=datetime(2024, 9, 2, 14, 0),
        note="Patient should avoid hard foods after the procedure.",
        creator_name="Receptionist John",
        clinic_contact="098-765-4321"
    )
    assert appointment.doctor_name == "Dr. Brown"
    assert appointment.patient_name == "Jane Doe"
    assert appointment.appointment_type == "Fitting of Braces"
    assert appointment.date_time == datetime(2024, 9, 2, 14, 0)
    assert appointment.note == "Patient should avoid hard foods after the procedure."
    assert appointment.creator_name == "Receptionist John"
    assert appointment.clinic_contact == "098-765-4321"

def test_rubber_band_change_appointment(director):
    appointment = director.create_rubber_band_change_appointment(
        doctor_name="Dr. Green",
        patient_name="Michael Roe",
        date_time=datetime(2024, 9, 3, 11, 0),
        note="Ensure bands are replaced every two weeks.",
        creator_name="Receptionist Alice",
        clinic_contact="555-123-4567"
    )
    assert appointment.doctor_name == "Dr. Green"
    assert appointment.patient_name == "Michael Roe"
    assert appointment.appointment_type == "Monthly Rubber Band Change"
    assert appointment.date_time == datetime(2024, 9, 3, 11, 0)
    assert appointment.note == "Ensure bands are replaced every two weeks."
    assert appointment.creator_name == "Receptionist Alice"
    assert appointment.clinic_contact == "555-123-4567"

def test_braces_removal_appointment(director):
    appointment = director.create_braces_removal_appointment(
        doctor_name="Dr. White",
        patient_name="Emily Smith",
        date_time=datetime(2024, 9, 4, 9, 30),
        note="Take care to avoid sticky foods after removal.",
        creator_name="Receptionist Bob",
        clinic_contact="321-654-9870"
    )
    assert appointment.doctor_name == "Dr. White"
    assert appointment.patient_name == "Emily Smith"
    assert appointment.appointment_type == "Removal of Braces"
    assert appointment.date_time == datetime(2024, 9, 4, 9, 30)
    assert appointment.note == "Take care to avoid sticky foods after removal."
    assert appointment.creator_name == "Receptionist Bob"
    assert appointment.clinic_contact == "321-654-9870"

if __name__ == "__main__":
    pytest.main()