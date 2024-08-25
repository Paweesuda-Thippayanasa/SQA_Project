import datetime
import pytest
from AppointmentBuilder import AppointmentBuilder, Appointment

@pytest.fixture
def appointment_builder():
    return AppointmentBuilder()

class TestAppointmentBuilder:

    def test_build_empty_appointment(self, appointment_builder):
        """Test building an appointment with all fields set to None."""
        appointment = appointment_builder.build()
        assert appointment.doctor_name is None
        assert appointment.patient_name is None
        assert appointment.appointment_type is None
        assert appointment.date_time is None
        assert appointment.note is None
        assert appointment.creator_name is None
        assert appointment.clinic_contact_number is None

    def test_build_complete_appointment(self, appointment_builder):
        """Test building an appointment with all fields filled."""
        appointment = appointment_builder.with_doctor("Dr. Jones")\
                                         .for_patient("Jane Doe")\
                                         .of_type("Monthly Rubber Band Change")\
                                         .on_date_time(datetime(2024, 4, 1, 14, 0, 0))\
                                         .with_note("Please bring your old rubber bands.")\
                                         .created_by("Bob")\
                                         .at_clinic_number("987-654-3210")\
                                         .build()

        assert appointment.doctor_name == "Dr. Jones"
        assert appointment.patient_name == "Jane Doe"
        assert appointment.appointment_type == "Monthly Rubber Band Change"
        assert appointment.date_time == datetime(2024, 4, 1, 14, 0, 0)
        assert appointment.note == "Please bring your old rubber bands."
        assert appointment.creator_name == "Bob"
        assert appointment.clinic_contact_number == "987-654-3210"