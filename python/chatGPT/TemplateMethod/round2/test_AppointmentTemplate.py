import pytest
from datetime import datetime
from appointmentTemplate import (
    ToothExtractionAppointment,
    MonthlyRubberBandChangeAppointment,
    RemovalOfBracesAppointment,
    FittingOfBracesAppointment
)

@pytest.fixture
def sample_appointment():
    return {
        "doctor_name": "Dr. Smith",
        "patient_name": "John Doe",
        "date_time": datetime.now(),
        "created_by": "Admin",
        "clinic_contact": "+1234567890"
    }

def test_tooth_extraction_appointment(sample_appointment):
    scheduler = ToothExtractionAppointment()
    appointment = scheduler.schedule_appointment(
        sample_appointment["doctor_name"],
        sample_appointment["patient_name"],
        sample_appointment["date_time"],
        sample_appointment["created_by"],
        sample_appointment["clinic_contact"]
    )
    assert appointment["type"] == "Tooth Extraction"

def test_monthly_rubber_band_change_appointment(sample_appointment):
    scheduler = MonthlyRubberBandChangeAppointment()
    appointment = scheduler.schedule_appointment(
        sample_appointment["doctor_name"],
        sample_appointment["patient_name"],
        sample_appointment["date_time"],
        sample_appointment["created_by"],
        sample_appointment["clinic_contact"]
    )
    assert appointment["type"] == "Monthly Rubber Band Change"

def test_removal_of_braces_appointment(sample_appointment):
    scheduler = RemovalOfBracesAppointment()
    appointment = scheduler.schedule_appointment(
        sample_appointment["doctor_name"],
        sample_appointment["patient_name"],
        sample_appointment["date_time"],
        sample_appointment["created_by"],
        sample_appointment["clinic_contact"]
    )
    assert appointment["type"] == "Removal of Braces"

def test_fitting_of_braces_appointment(sample_appointment):
    scheduler = FittingOfBracesAppointment()
    appointment = scheduler.schedule_appointment(
        sample_appointment["doctor_name"],
        sample_appointment["patient_name"],
        sample_appointment["date_time"],
        sample_appointment["created_by"],
        sample_appointment["clinic_contact"]
    )
    assert appointment["type"] == "Fitting of Braces"
    
if __name__ == "__main__":
    pytest.main()
