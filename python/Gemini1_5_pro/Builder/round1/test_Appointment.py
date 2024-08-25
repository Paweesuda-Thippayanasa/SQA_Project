from datetime import date

import pytest
from Appointment import Appointment, AppointmentBuilder, AppointmentType

@pytest.fixture
def appointment_builder():
    return AppointmentBuilder()


def test_create_appointment(appointment_builder):
    appointment = (
        appointment_builder.set_doctor_name("Dr. Smith")
        .set_patient_name("John Doe")
        .set_appointment_type(AppointmentType.BRACES_FITTING)
        .set_date(date.today().strftime("%Y-%m-%d"))
        .set_time("10:00 AM")
        .set_note("Bring previous dental records.")
        .set_created_by("Receptionist")
        .set_clinic_contact_number("123-456-7890")
        .build()
    )

    assert appointment.doctor_name == "Dr. Smith"
    assert appointment.patient_name == "John Doe"
    assert appointment.appointment_type == AppointmentType.BRACES_FITTING
    assert appointment.date == date.today().strftime("%Y-%m-%d")
    assert appointment.time == "10:00 AM"
    assert appointment.note == "Bring previous dental records."
    assert appointment.created_by == "Receptionist"
    assert appointment.clinic_contact_number == "123-456-7890"


def test_missing_required_fields(appointment_builder):
    with pytest.raises(ValueError):
        appointment_builder.set_doctor_name("Dr. Smith").set_patient_name("John Doe").build()