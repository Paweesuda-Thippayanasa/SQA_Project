import pytest
from datetime import datetime
from Appointment import Appointment, AppointmentBuilder

# Test Suite
@pytest.fixture
def appointment_data():
    return {
        "doctor": "Dr. Smith",
        "patient": "Alice",
        "type": "Braces Fitting",
        "date_time": datetime(2024, 3, 15, 10, 0),
        "note": "Remember to bring your x-rays",
        "created_by": "Receptionist",
        "clinic_contact": "123-456-7890",
    }

# Test Cases
def test_create_appointment(appointment_data):
    """Test creating an appointment with all fields."""

    appointment = (
        AppointmentBuilder()
        .set_doctor(appointment_data["doctor"])
        .set_patient(appointment_data["patient"])
        .set_type(appointment_data["type"])
        .set_date_time(appointment_data["date_time"])
        .set_note(appointment_data["note"])
        .set_created_by(appointment_data["created_by"])
        .set_clinic_contact(appointment_data["clinic_contact"])
        .build()
    )
    assert appointment.doctor == appointment_data["doctor"]
    assert appointment.patient == appointment_data["patient"]
    assert appointment.type == appointment_data["type"]
    assert appointment.date_time == appointment_data["date_time"]
    assert appointment.note == appointment_data["note"]
    assert appointment.created_by == appointment_data["created_by"]
    assert appointment.clinic_contact == appointment_data["clinic_contact"]


def test_missing_required_fields(appointment_data):
    """Test creating an appointment with missing required fields."""

    with pytest.raises(ValueError):
        AppointmentBuilder().set_doctor("Dr. Smith").set_patient("Alice").build()


def test_appointment_str_representation(appointment_data):
    """Test the string representation of an appointment."""

    appointment = (
        AppointmentBuilder()
        .set_doctor(appointment_data["doctor"])
        .set_patient(appointment_data["patient"])
        .set_type(appointment_data["type"])
        .set_date_time(appointment_data["date_time"])
        .set_note(appointment_data["note"])
        .set_created_by(appointment_data["created_by"])
        .set_clinic_contact(appointment_data["clinic_contact"])
        .build()
    )

    expected_str = (
        "Appointment Details:\n"
        f"  Doctor: {appointment_data['doctor']}\n"
        f"  Patient: {appointment_data['patient']}\n"
        f"  Type: {appointment_data['type']}\n"
        f"  Date & Time: {appointment_data['date_time'].strftime('%Y-%m-%d %H:%M')}\n"
        f"  Note: {appointment_data['note']}\n"
        f"  Created By: {appointment_data['created_by']}\n"
        f"  Clinic Contact: {appointment_data['clinic_contact']}"
    )
    assert str(appointment) == expected_str