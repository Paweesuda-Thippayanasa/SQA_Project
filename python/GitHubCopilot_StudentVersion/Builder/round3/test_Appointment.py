# test_appointment.py

import pytest
from datetime import datetime
from Appointment import AppointmentBuilder, Director

@pytest.fixture
def builder():
    return AppointmentBuilder()

@pytest.fixture
def director(builder):
    return Director(builder)

def test_tooth_extraction(director):
    appointment = director.construct_tooth_extraction(
        doctor_name="Dr. Smith",
        patient_name="John Doe",
        appointment_datetime=datetime(2023, 12, 1, 10, 0),
        note="Bring previous X-rays",
        creator_name="Receptionist",
        clinic_contact="123-456-7890"
    )
    assert appointment.doctor_name == "Dr. Smith"
    assert appointment.patient_name == "John Doe"
    assert appointment.appointment_type == "Tooth Extraction"
    assert appointment.appointment_datetime == datetime(2023, 12, 1, 10, 0)
    assert appointment.note == "Bring previous X-rays"
    assert appointment.creator_name == "Receptionist"
    assert appointment.clinic_contact == "123-456-7890"

def test_monthly_rubber_band_change(director):
    appointment = director.construct_monthly_rubber_band_change(
        doctor_name="Dr. Brown",
        patient_name="Jane Doe",
        appointment_datetime=datetime(2023, 12, 2, 11, 0),
        note="Check for any discomfort",
        creator_name="Assistant",
        clinic_contact="098-765-4321"
    )
    assert appointment.doctor_name == "Dr. Brown"
    assert appointment.patient_name == "Jane Doe"
    assert appointment.appointment_type == "Monthly Rubber Band Change"
    assert appointment.appointment_datetime == datetime(2023, 12, 2, 11, 0)
    assert appointment.note == "Check for any discomfort"
    assert appointment.creator_name == "Assistant"
    assert appointment.clinic_contact == "098-765-4321"

def test_removal_of_braces(director):
    appointment = director.construct_removal_of_braces(
        doctor_name="Dr. White",
        patient_name="Alice Smith",
        appointment_datetime=datetime(2023, 12, 3, 12, 0),
        note="Final checkup",
        creator_name="Nurse",
        clinic_contact="321-654-9870"
    )
    assert appointment.doctor_name == "Dr. White"
    assert appointment.patient_name == "Alice Smith"
    assert appointment.appointment_type == "Removal of Braces"
    assert appointment.appointment_datetime == datetime(2023, 12, 3, 12, 0)
    assert appointment.note == "Final checkup"
    assert appointment.creator_name == "Nurse"
    assert appointment.clinic_contact == "321-654-9870"

def test_fitting_of_braces(director):
    appointment = director.construct_fitting_of_braces(
        doctor_name="Dr. Green",
        patient_name="Bob Johnson",
        appointment_datetime=datetime(2023, 12, 4, 13, 0),
        note="Initial fitting",
        creator_name="Coordinator",
        clinic_contact="456-789-0123"
    )
    assert appointment.doctor_name == "Dr. Green"
    assert appointment.patient_name == "Bob Johnson"
    assert appointment.appointment_type == "Fitting of Braces"
    assert appointment.appointment_datetime == datetime(2023, 12, 4, 13, 0)
    assert appointment.note == "Initial fitting"
    assert appointment.creator_name == "Coordinator"
    assert appointment.clinic_contact == "456-789-0123"