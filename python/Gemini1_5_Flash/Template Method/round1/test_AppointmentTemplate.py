# test_appointment_scheduler.py

import pytest
from appointmentTemplate import AppointmentScheduler, TOOTH_EXTRACTION, MONTHLY_RUBBER_BAND_CHANGE, REMOVAL_OF_BRACES, FITTING_OF_BRACES, FittingOfBracesAppointment, MonthlyRubberBandChangeAppointment, RemovalOfBracesAppointment, ToothExtractionAppointment, datetime

@pytest.fixture
def scheduler():
    return AppointmentScheduler("1234567890")

def test_schedule_appointment(scheduler):
    # Test Tooth Extraction
    appointment = scheduler.schedule_appointment(TOOTH_EXTRACTION, "Dr. Smith", "John Doe", datetime(2024, 3, 15), datetime(10, 0, 0), "Extract wisdom tooth", "Alice", "1234567890")
    assert isinstance(appointment, ToothExtractionAppointment)
    assert appointment.doctor_name == "Dr. Smith"
    assert appointment.patient_name == "John Doe"
    assert appointment.date == datetime(2024, 3, 15)
    assert appointment.time == datetime(10, 0, 0)
    assert appointment.note == "Extract wisdom tooth"
    assert appointment.creator_name == "Alice"
    assert appointment.clinic_contact_number == "1234567890"

    # Test Monthly Rubber Band Change
    appointment = scheduler.schedule_appointment(MONTHLY_RUBBER_BAND_CHANGE, "Dr. Jones", "Jane Doe", datetime(2024, 3, 22), datetime(14, 30, 0), "Change rubber bands", "Bob", "1234567890")
    assert isinstance(appointment, MonthlyRubberBandChangeAppointment)

    # Test Removal of Braces
    appointment = scheduler.schedule_appointment(REMOVAL_OF_BRACES, "Dr. Brown", "Peter Pan", datetime(2024, 4, 10), datetime(11, 0, 0), "Remove braces", "Charlie", "1234567890")
    assert isinstance(appointment, RemovalOfBracesAppointment)

    # Test Fitting of Braces
    appointment = scheduler.schedule_appointment(FITTING_OF_BRACES, "Dr. White", "Wendy Darling", datetime(2024, 4, 17), datetime(15, 0, 0), "Fit braces", "David", "1234567890")
    assert isinstance(appointment, FittingOfBracesAppointment)

    # Test Invalid Appointment Type
    with pytest.raises(ValueError):
        scheduler.schedule_appointment("Invalid Type", "Dr. Black", "Hook", datetime(2024, 4, 24), datetime(16, 0, 0), "Invalid", "Eve", "1234567890")
