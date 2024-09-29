import datetime
import pytest
from AppointmentBuilder import AppointmentBuilder, Appointment


class TestAppointmentBuilder:
    @pytest.fixture
    def builder(self):
        return AppointmentBuilder()

    def test_build_appointment(self, builder):
        appointment = builder.with_doctor("Dr. Smith") \
                           .for_patient("John Doe") \
                           .with_type("Tooth Extraction") \
                           .at_datetime(datetime.datetime(2024, 3, 15, 10, 0)) \
                           .with_note("Please bring a friend for support.") \
                           .created_by("Receptionist") \
                           .with_clinic_phone("+1 555-123-4567") \
                           .build()
        assert isinstance(appointment, Appointment)

    def test_appointment_attributes(self, builder):
        appointment = builder.with_doctor("Dr. Smith") \
                           .for_patient("John Doe") \
                           .with_type("Tooth Extraction") \
                           .at_datetime(datetime.datetime(2024, 3, 15, 10, 0)) \
                           .with_note("Please bring a friend for support.") \
                           .created_by("Receptionist") \
                           .with_clinic_phone("+1 555-123-4567") \
                           .build()
        assert appointment.doctor == "Dr. Smith"
        assert appointment.patient == "John Doe"
        assert appointment.appointment_type == "Tooth Extraction"
        assert appointment.date_time == datetime.datetime(2024, 3, 15, 10, 0)
        assert appointment.note == "Please bring a friend for support."
        assert appointment.creator == "Receptionist"
        assert appointment.clinic_phone == "+1 555-123-4567"