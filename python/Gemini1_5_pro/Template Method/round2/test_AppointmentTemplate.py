# test_appointment.py

from datetime import datetime
import pytest
from appointmentTemplate import (
    ToothExtractionAppointment,
    MonthlyRubberBandChangeAppointment,
    RemovalOfBracesAppointment,
    FittingOfBracesAppointment,
)

@pytest.fixture
def appointment_data():
    doctor = "Dr. Smith"
    patient = "John Doe"
    date_time = datetime(2024, 3, 15, 10, 0)
    note = "Please bring your insurance card."
    creator = "Receptionist"
    clinic_contact = "123-456-7890"
    return doctor, patient, date_time, note, creator, clinic_contact

def test_create_tooth_extraction_appointment(appointment_data):
    doctor, patient, date_time, note, creator, clinic_contact = appointment_data
    appointment = ToothExtractionAppointment(doctor, patient, date_time, note, creator, clinic_contact)
    assert appointment.get_appointment_type() == "Tooth Extraction"
    appointment.schedule()

def test_create_monthly_rubber_band_change_appointment(appointment_data):
    doctor, patient, date_time, note, creator, clinic_contact = appointment_data
    appointment = MonthlyRubberBandChangeAppointment(doctor, patient, date_time, note, creator, clinic_contact)
    assert appointment.get_appointment_type() == "Monthly Rubber Band Change"
    appointment.schedule()

def test_create_removal_of_braces_appointment(appointment_data):
    doctor, patient, date_time, note, creator, clinic_contact = appointment_data
    appointment = RemovalOfBracesAppointment(doctor, patient, date_time, note, creator, clinic_contact)
    assert appointment.get_appointment_type() == "Removal of Braces"
    appointment.schedule()

def test_create_fitting_of_braces_appointment(appointment_data):
    doctor, patient, date_time, note, creator, clinic_contact = appointment_data
    appointment = FittingOfBracesAppointment(doctor, patient, date_time, note, creator, clinic_contact)
    assert appointment.get_appointment_type() == "Fitting of Braces"
    appointment.schedule()

def test_template_method(appointment_data):
    doctor, patient, date_time, note, creator, clinic_contact = appointment_data
    appointment = ToothExtractionAppointment(doctor, patient, date_time, note, creator, clinic_contact)
    appointment._validate_appointment()
    appointment._create_appointment_record()
    appointment._send_confirmation()
