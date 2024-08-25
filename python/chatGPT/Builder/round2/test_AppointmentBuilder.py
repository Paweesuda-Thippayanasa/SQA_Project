import pytest
from datetime import datetime
from AppointmentDirector import AppointmentDirector
from AppointmentBuilder import AppointmentBuilder

@pytest.fixture
def builder():
    return AppointmentBuilder()

@pytest.fixture
def director(builder):
    return AppointmentDirector(builder)

def test_tooth_extraction_appointment(director):
    appointment = director.construct_tooth_extraction_appointment(
        doctor_name="Dr. John Doe",
        patient_name="Alice Smith",
        date_time=datetime(2024, 8, 30, 14, 0),
        note="Take painkillers after extraction.",
        creator_name="Receptionist",
        clinic_contact="555-1234"
    )
    assert appointment.doctor_name == "Dr. John Doe"
    assert appointment.patient_name == "Alice Smith"
    assert appointment.appointment_type == "Tooth Extraction"
    assert appointment.date_time == datetime(2024, 8, 30, 14, 0)
    assert appointment.note == "Take painkillers after extraction."
    assert appointment.creator_name == "Receptionist"
    assert appointment.clinic_contact == "555-1234"

def test_rubber_band_change_appointment(director):
    appointment = director.construct_rubber_band_change_appointment(
        doctor_name="Dr. Jane Roe",
        patient_name="Bob Jones",
        date_time=datetime(2024, 9, 1, 10, 0),
        note="Monthly checkup.",
        creator_name="Assistant",
        clinic_contact="555-5678"
    )
    assert appointment.doctor_name == "Dr. Jane Roe"
    assert appointment.patient_name == "Bob Jones"
    assert appointment.appointment_type == "Monthly Rubber Band Change"
    assert appointment.date_time == datetime(2024, 9, 1, 10, 0)
    assert appointment.note == "Monthly checkup."
    assert appointment.creator_name == "Assistant"
    assert appointment.clinic_contact == "555-5678"

def test_removal_of_braces_appointment(director):
    appointment = director.construct_removal_of_braces_appointment(
        doctor_name="Dr. Richard Roe",
        patient_name="Charlie Brown",
        date_time=datetime(2024, 9, 5, 15, 0),
        note="Braces removal procedure, may take up to 1 hour.",
        creator_name="Coordinator",
        clinic_contact="555-7890"
    )
    assert appointment.doctor_name == "Dr. Richard Roe"
    assert appointment.patient_name == "Charlie Brown"
    assert appointment.appointment_type == "Removal of Braces"
    assert appointment.date_time == datetime(2024, 9, 5, 15, 0)
    assert appointment.note == "Braces removal procedure, may take up to 1 hour."
    assert appointment.creator_name == "Coordinator"
    assert appointment.clinic_contact == "555-7890"

def test_fitting_of_braces_appointment(director):
    appointment = director.construct_fitting_of_braces_appointment(
        doctor_name="Dr. Mary Major",
        patient_name="Diana Prince",
        date_time=datetime(2024, 9, 10, 11, 0),
        note="Initial fitting of braces, includes a consultation.",
        creator_name="Technician",
        clinic_contact="555-2468"
    )
    assert appointment.doctor_name == "Dr. Mary Major"
    assert appointment.patient_name == "Diana Prince"
    assert appointment.appointment_type == "Fitting of Braces"
    assert appointment.date_time == datetime(2024, 9, 10, 11, 0)
    assert appointment.note == "Initial fitting of braces, includes a consultation."
    assert appointment.creator_name == "Technician"
    assert appointment.clinic_contact == "555-2468"