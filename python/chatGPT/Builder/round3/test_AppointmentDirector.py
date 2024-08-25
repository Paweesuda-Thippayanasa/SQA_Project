import pytest
from datetime import datetime
from OrthodonticAppointmentBuilder import OrthodonticAppointmentBuilder
from AppointmentDirector import AppointmentDirector

@pytest.fixture
def appointment_builder():
    return OrthodonticAppointmentBuilder()

def test_appointment_creation(appointment_builder):
    director = AppointmentDirector(appointment_builder)
    appointment = director.construct(
        doctor_name="Dr. John Doe",
        patient_name="Jane Smith",
        appointment_type="Tooth Extraction",
        date_time=datetime(2024, 9, 1, 10, 0),
        note="Take painkillers after the procedure.",
        creator_name="Alice Johnson",
        contact_number="0123456789"
    )

    assert appointment.doctor_name == "Dr. John Doe"
    assert appointment.patient_name == "Jane Smith"
    assert appointment.appointment_type == "Tooth Extraction"
    assert appointment.date_time == datetime(2024, 9, 1, 10, 0)
    assert appointment.note == "Take painkillers after the procedure."
    assert appointment.creator_name == "Alice Johnson"
    assert appointment.contact_number == "0123456789"

    print(appointment)


