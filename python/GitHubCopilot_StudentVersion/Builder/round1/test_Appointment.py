
# test_appointment.py
import pytest
from Appointment import AppointmentBuilder, AppointmentDirector

@pytest.fixture
def builder():
    return AppointmentBuilder()

def test_tooth_extraction(builder):
    director = AppointmentDirector(builder)
    appointment = director.construct_tooth_extraction("Dr. Smith", "John Doe", "2023-10-10 10:00", "Take painkillers", "Admin", "1234567890")
    assert appointment.doctor_name == "Dr. Smith"
    assert appointment.patient_name == "John Doe"
    assert appointment.appointment_type == "Tooth Extraction"
    assert appointment.date_time == "2023-10-10 10:00"
    assert appointment.note == "Take painkillers"
    assert appointment.creator_name == "Admin"
    assert appointment.clinic_contact == "1234567890"

def test_monthly_rubber_band_change(builder):
    director = AppointmentDirector(builder)
    appointment = director.construct_monthly_rubber_band_change("Dr. Brown", "Jane Doe", "2023-11-11 11:00", "Change every month", "Admin", "0987654321")
    assert appointment.doctor_name == "Dr. Brown"
    assert appointment.patient_name == "Jane Doe"
    assert appointment.appointment_type == "Monthly Rubber Band Change"
    assert appointment.date_time == "2023-11-11 11:00"
    assert appointment.note == "Change every month"
    assert appointment.creator_name == "Admin"
    assert appointment.clinic_contact == "0987654321"

def test_removal_of_braces(builder):
    director = AppointmentDirector(builder)
    appointment = director.construct_removal_of_braces("Dr. White", "Alice", "2023-12-12 12:00", "Final checkup", "Admin", "1122334455")
    assert appointment.doctor_name == "Dr. White"
    assert appointment.patient_name == "Alice"
    assert appointment.appointment_type == "Removal of Braces"
    assert appointment.date_time == "2023-12-12 12:00"
    assert appointment.note == "Final checkup"
    assert appointment.creator_name == "Admin"
    assert appointment.clinic_contact == "1122334455"

def test_fitting_of_braces(builder):
    director = AppointmentDirector(builder)
    appointment = director.construct_fitting_of_braces("Dr. Black", "Bob", "2023-09-09 09:00", "Initial fitting", "Admin", "5566778899")
    assert appointment.doctor_name == "Dr. Black"
    assert appointment.patient_name == "Bob"
    assert appointment.appointment_type == "Fitting of Braces"
    assert appointment.date_time == "2023-09-09 09:00"
    assert appointment.note == "Initial fitting"
    assert appointment.creator_name == "Admin"
    assert appointment.clinic_contact == "5566778899"