import datetime
import pytest

from AppointmentBuilder import AppointmentBuilder

@pytest.fixture
def builder():
    return AppointmentBuilder()

@pytest.mark.parametrize("appointment_type", ["tooth extraction", "monthly rubber band change", "removal of braces", "fitting of braces"])
def test_set_appointment_type(builder, appointment_type):
    appointment = builder.set_appointment_type(appointment_type).build()
    assert appointment.appointment_type == appointment_type

def test_set_doctor(builder):
    doctor_name = "Dr. Smith"
    appointment = builder.set_doctor(doctor_name).build()
    assert appointment.doctor == doctor_name

def test_set_patient(builder):
    patient_name = "John Doe"
    appointment = builder.set_patient(patient_name).build()
    assert appointment.patient == patient_name

def test_set_date_time(builder):
    date_time = datetime.datetime(2024, 3, 15, 10, 0)
    appointment = builder.set_date_time(date_time).build()
    assert appointment.date_time == date_time

def test_set_note(builder):
    note = "Please bring your insurance card."
    appointment = builder.set_note(note).build()
    assert appointment.note == note

def test_set_creator(builder):
    creator_name = "Jane Doe"
    appointment = builder.set_creator(creator_name).build()
    assert appointment.creator == creator_name

def test_set_clinic_contact(builder):
    clinic_contact = "123-456-7890"
    appointment = builder.set_clinic_contact(clinic_contact).build()
    assert appointment.clinic_contact == clinic_contact

def test_build_appointment(builder):
    appointment = builder.set_doctor("Dr. Smith")\
                     .set_patient("John Doe")\
                     .set_appointment_type("tooth extraction")\
                     .set_date_time(datetime.datetime(2024, 3, 15, 10, 0))\
                     .set_note("Please bring your insurance card.")\
                     .set_creator("Jane Doe")\
                     .set_clinic_contact("123-456-7890")\
                     .build()

    assert appointment.doctor == "Dr. Smith"
    assert appointment.patient == "John Doe"
    assert appointment.appointment_type == "tooth extraction"
    assert appointment.date_time == datetime.datetime(2024, 3, 15, 10, 0)
    assert appointment.note == "Please bring your insurance card."
    assert appointment.creator == "Jane Doe"
    assert appointment.clinic_contact == "123-456-7890"