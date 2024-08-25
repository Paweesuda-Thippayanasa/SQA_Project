import pytest
from datetime import datetime
from unittest.mock import Mock
from appointmentTemplate import (
    BasicAppointmentScheduler,
    AppointmentType,
)


@pytest.fixture
def valid_appointment_data():
    return {
        "doctor_name": "Dr. Smith",
        "patient_name": "John Doe",
        "appointment_type": AppointmentType.BRACES_FITTING,
        "date_time": datetime(2024, 3, 15, 10, 30),
        "note": "Bring previous dental records.",
        "creator_name": "Receptionist",
    }


# Test cases for AppointmentScheduler

def test_schedule(valid_appointment_data, monkeypatch):
    scheduler = BasicAppointmentScheduler(**valid_appointment_data)

    mock_check_availability = Mock()
    mock_save_appointment = Mock()
    mock_send_confirmation = Mock()

    monkeypatch.setattr(
        BasicAppointmentScheduler,
        "_check_doctor_availability",
        mock_check_availability,
    )
    monkeypatch.setattr(
        BasicAppointmentScheduler, "_save_appointment", mock_save_appointment
    )
    monkeypatch.setattr(
        BasicAppointmentScheduler, "_send_confirmation", mock_send_confirmation
    )

    scheduler.schedule()

    mock_check_availability.assert_called_once()
    mock_save_appointment.assert_called_once()
    mock_send_confirmation.assert_called_once()


def test_validate_input_valid_data(valid_appointment_data):
    try:
        scheduler = BasicAppointmentScheduler(**valid_appointment_data)
        scheduler._validate_input()
    except Exception as e:
        pytest.fail(f"_validate_input() raised an exception with valid data: {e}")


def test_validate_input_invalid_doctor_name(valid_appointment_data):
    invalid_data = valid_appointment_data.copy()
    invalid_data["doctor_name"] = 123
    with pytest.raises(TypeError) as excinfo:
        BasicAppointmentScheduler(**invalid_data)._validate_input()
    assert "Doctor name and patient name must be strings." in str(excinfo.value)


def test_validate_input_invalid_patient_name(valid_appointment_data):
    invalid_data = valid_appointment_data.copy()
    invalid_data["patient_name"] = 123
    with pytest.raises(TypeError) as excinfo:
        BasicAppointmentScheduler(**invalid_data)._validate_input()
    assert "Doctor name and patient name must be strings." in str(excinfo.value)


def test_validate_input_invalid_appointment_type(valid_appointment_data):
    invalid_data = valid_appointment_data.copy()
    invalid_data["appointment_type"] = "Invalid Type"
    with pytest.raises(TypeError) as excinfo:
        BasicAppointmentScheduler(**invalid_data)._validate_input()
    assert "Appointment type must be a valid AppointmentType enum value." in str(
        excinfo.value
    )


def test_validate_input_invalid_date_time(valid_appointment_data):
    invalid_data = valid_appointment_data.copy()
    invalid_data["date_time"] = "Invalid Datetime"
    with pytest.raises(TypeError) as excinfo:
        BasicAppointmentScheduler(**invalid_data)._validate_input()
    assert "Appointment date and time must be a datetime object." in str(excinfo.value)


# Test cases for the abstract methods

def test_check_doctor_availability(valid_appointment_data, monkeypatch):
    scheduler = BasicAppointmentScheduler(**valid_appointment_data)

    mock_check_availability = Mock()
    monkeypatch.setattr(
        scheduler, "_check_doctor_availability", mock_check_availability
    )

    scheduler._check_doctor_availability()

    mock_check_availability.assert_called_once()


def test_save_appointment(valid_appointment_data, monkeypatch):
    scheduler = BasicAppointmentScheduler(**valid_appointment_data)

    mock_save_appointment = Mock()
    monkeypatch.setattr(scheduler, "_save_appointment", mock_save_appointment)

    scheduler._save_appointment()

    mock_save_appointment.assert_called_once()


def test_send_confirmation(valid_appointment_data, monkeypatch):
    scheduler = BasicAppointmentScheduler(**valid_appointment_data)

    expected_output = (
        f"Appointment Confirmation:\n"
        f"Doctor: {scheduler.doctor_name}\n"
        f"Patient: {scheduler.patient_name}\n"
        f"Type: {scheduler.appointment_type.value}\n"
        f"Date & Time: {scheduler.date_time.strftime('%Y-%m-%d %H:%M')}\n"
        f"Note: {scheduler.note}\n"
        f"Created by: {scheduler.creator_name}\n"
        f"Clinic Contact: {scheduler.clinic_contact}\n"
    )

    mock_print = Mock()
    monkeypatch.setattr("builtins.print", mock_print)

    scheduler._send_confirmation()

    mock_print.assert_called_once_with(expected_output)


@pytest.mark.parametrize(
    "appointment_type",
    [
        AppointmentType.EXTRACTION,
        AppointmentType.RUBBER_BAND_CHANGE,
        AppointmentType.BRACES_REMOVAL,
        AppointmentType.BRACES_FITTING,
    ],
)
def test_all_appointment_types(valid_appointment_data, appointment_type):
    valid_appointment_data["appointment_type"] = appointment_type

    scheduler = BasicAppointmentScheduler(**valid_appointment_data)
    scheduler._validate_input() 
