import pytest
from appointmentTemplate import AppointmentScheduler

@pytest.fixture
def appointment_data():
    return {
        "doctor_name": "Dr. Smith",
        "patient_name": "John Doe",
        "date_time": "2023-10-10 10:00",
        "note": "Follow-up required",
        "creator_name": "Admin",
        "contact_number": "1234567890"
    }

def test_create_tooth_extraction_appointment(appointment_data):
    scheduler = AppointmentScheduler()
    record = scheduler.schedule(
        appointment_type="Tooth Extraction",
        doctor_name=appointment_data["doctor_name"],
        patient_name=appointment_data["patient_name"],
        date_time=appointment_data["date_time"],
        note=appointment_data["note"],
        creator_name=appointment_data["creator_name"],
        contact_number=appointment_data["contact_number"]
    )
    assert record.doctor_name == appointment_data["doctor_name"]
    assert record.patient_name == appointment_data["patient_name"]
    assert record.appointment_type == "Tooth Extraction"
    assert record.date_time == appointment_data["date_time"]
    assert record.note == appointment_data["note"]
    assert record.creator_name == appointment_data["creator_name"]
    assert record.contact_number == appointment_data["contact_number"]

def test_create_rubber_band_change_appointment(appointment_data):
    scheduler = AppointmentScheduler()
    record = scheduler.schedule(
        appointment_type="Monthly Rubber Band Change",
        doctor_name=appointment_data["doctor_name"],
        patient_name=appointment_data["patient_name"],
        date_time=appointment_data["date_time"],
        note=appointment_data["note"],
        creator_name=appointment_data["creator_name"],
        contact_number=appointment_data["contact_number"]
    )
    assert record.doctor_name == appointment_data["doctor_name"]
    assert record.patient_name == appointment_data["patient_name"]
    assert record.appointment_type == "Monthly Rubber Band Change"
    assert record.date_time == appointment_data["date_time"]
    assert record.note == appointment_data["note"]
    assert record.creator_name == appointment_data["creator_name"]
    assert record.contact_number == appointment_data["contact_number"]

def test_create_braces_removal_appointment(appointment_data):
    scheduler = AppointmentScheduler()
    record = scheduler.schedule(
        appointment_type="Braces Removal",
        doctor_name=appointment_data["doctor_name"],
        patient_name=appointment_data["patient_name"],
        date_time=appointment_data["date_time"],
        note=appointment_data["note"],
        creator_name=appointment_data["creator_name"],
        contact_number=appointment_data["contact_number"]
    )
    assert record.doctor_name == appointment_data["doctor_name"]
    assert record.patient_name == appointment_data["patient_name"]
    assert record.appointment_type == "Braces Removal"
    assert record.date_time == appointment_data["date_time"]
    assert record.note == appointment_data["note"]
    assert record.creator_name == appointment_data["creator_name"]
    assert record.contact_number == appointment_data["contact_number"]

def test_create_braces_fitting_appointment(appointment_data):
    scheduler = AppointmentScheduler()
    record = scheduler.schedule(
        appointment_type="Braces Fitting",
        doctor_name=appointment_data["doctor_name"],
        patient_name=appointment_data["patient_name"],
        date_time=appointment_data["date_time"],
        note=appointment_data["note"],
        creator_name=appointment_data["creator_name"],
        contact_number=appointment_data["contact_number"]
    )
    assert record.doctor_name == appointment_data["doctor_name"]
    assert record.patient_name == appointment_data["patient_name"]
    assert record.appointment_type == "Braces Fitting"
    assert record.date_time == appointment_data["date_time"]
    assert record.note == appointment_data["note"]
    assert record.creator_name == appointment_data["creator_name"]
    assert record.contact_number == appointment_data["contact_number"]
