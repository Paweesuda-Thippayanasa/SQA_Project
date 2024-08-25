# test_AppointmentTemplate.py
import pytest
from appointmentTemplate import ToothExtractionScheduler, RubberBandChangeScheduler, RemovalOfBracesScheduler, FittingOfBracesScheduler
from datetime import datetime

@pytest.fixture
def schedulers():
    return [
        ToothExtractionScheduler(),
        RubberBandChangeScheduler(),
        RemovalOfBracesScheduler(),
        FittingOfBracesScheduler()
    ]

def test_schedule_appointment(schedulers):
    expected_types = [
        "Tooth Extraction",
        "Monthly Rubber Band Change",
        "Removal of Braces",
        "Fitting of Braces"
    ]
    
    for scheduler, expected_type in zip(schedulers, expected_types):
        appointment = scheduler.schedule_appointment(
            doctor_name="Dr. Smith",
            patient_name="John Doe",
            date_time=datetime(2023, 10, 1, 10, 0),
            note="Bring previous X-rays",
            created_by="Receptionist",
            contact_number="123-456-7890"
        )
        assert appointment.doctor_name == "Dr. Smith"
        assert appointment.patient_name == "John Doe"
        assert appointment.date_time == datetime(2023, 10, 1, 10, 0)
        assert appointment.note == "Bring previous X-rays"
        assert appointment.created_by == "Receptionist"
        assert appointment.contact_number == "123-456-7890"
        assert appointment.appointment_type == expected_type

if __name__ == "__main__":
    pytest.main()
