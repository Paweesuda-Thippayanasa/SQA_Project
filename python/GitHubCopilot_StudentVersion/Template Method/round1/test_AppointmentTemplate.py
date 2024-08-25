import pytest
from datetime import datetime
from appointmentTemplate import (
    Doctor, Patient, AppointmentScheduler,
    ToothExtraction, MonthlyRubberBandChange,
    RemovalOfBraces, FittingOfBraces
)

@pytest.fixture
def setup_environment():
    doctor = Doctor("Dr. Smith", "1234567890")
    patient = Patient("John Doe", doctor)
    scheduler = AppointmentScheduler()
    date_time = datetime(2023, 12, 25, 10, 0)
    note = "Please arrive 10 minutes early."
    creator = "Receptionist"
    contact_number = "0987654321"
    return scheduler, doctor, patient, date_time, note, creator, contact_number

def test_create_tooth_extraction_appointment(setup_environment):
    scheduler, doctor, patient, date_time, note, creator, contact_number = setup_environment
    scheduler.create_appointment(ToothExtraction, doctor, patient, date_time, note, creator, contact_number)
    assert len(scheduler.appointments) == 1

def test_create_monthly_rubber_band_change_appointment(setup_environment):
    scheduler, doctor, patient, date_time, note, creator, contact_number = setup_environment
    scheduler.create_appointment(MonthlyRubberBandChange, doctor, patient, date_time, note, creator, contact_number)
    assert len(scheduler.appointments) == 1

def test_create_removal_of_braces_appointment(setup_environment):
    scheduler, doctor, patient, date_time, note, creator, contact_number = setup_environment
    scheduler.create_appointment(RemovalOfBraces, doctor, patient, date_time, note, creator, contact_number)
    assert len(scheduler.appointments) == 1

def test_create_fitting_of_braces_appointment(setup_environment):
    scheduler, doctor, patient, date_time, note, creator, contact_number = setup_environment
    scheduler.create_appointment(FittingOfBraces, doctor, patient, date_time, note, creator, contact_number)
    assert len(scheduler.appointments) == 1
