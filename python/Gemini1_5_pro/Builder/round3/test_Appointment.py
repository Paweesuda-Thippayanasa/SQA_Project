import pytest
from datetime import datetime
from Appointment import Appointment, AppointmentBuilder

@pytest.fixture
def appointment_data():
    return {
        'doctor_name': 'Dr. Smith',
        'patient_name': 'John Doe',
        'appointment_type': 'Fitting of braces',
        'date_time': datetime(2024, 3, 15, 10, 0),
        'note': 'Remember to bring your x-rays',
        'created_by': 'Receptionist',
        'clinic_contact_number': '+1-555-123-4567'
    }

@pytest.mark.parametrize("field, value", [
    ('doctor_name', 'Dr. Jones'),
    ('patient_name', 'Jane Doe'),
    ('appointment_type', 'Monthly rubber band change'),
    ('date_time', datetime(2024, 3, 22, 14, 30)),
    ('note', 'Follow-up after adjustment'),
    ('created_by', 'Dental Assistant'),
    ('clinic_contact_number', '+1-555-987-6543')
])
def test_builder_with_individual_fields(appointment_data, field, value):
    # Arrange
    builder = AppointmentBuilder()

    # Act
    # Dynamically set attribute using setattr
    setattr(builder, field, value)
    appointment = builder.build()

    # Assert
    assert getattr(appointment, field) == value

def test_builder_with_all_fields(appointment_data):
    # Arrange
    builder = AppointmentBuilder()

    # Act
    builder.for_doctor(appointment_data['doctor_name']) \
           .for_patient(appointment_data['patient_name']) \
           .with_type(appointment_data['appointment_type']) \
           .on_date_time(appointment_data['date_time']) \
           .with_note(appointment_data['note']) \
           .created_by(appointment_data['created_by']) \
           .with_clinic_contact(appointment_data['clinic_contact_number'])
    appointment = builder.build()

    # Assert
    assert appointment.doctor_name == appointment_data['doctor_name']
    assert appointment.patient_name == appointment_data['patient_name']
    assert appointment.appointment_type == appointment_data['appointment_type']
    assert appointment.date_time == appointment_data['date_time']
    assert appointment.note == appointment_data['note']
    assert appointment.created_by == appointment_data['created_by']
    assert appointment.clinic_contact_number == appointment_data['clinic_contact_number']

def test_builder_missing_required_fields():
    # Arrange
    builder = AppointmentBuilder()

    # Act & Assert
    with pytest.raises(ValueError) as excinfo:
        builder.build()
    assert "Doctor, patient, type and date/time are required." in str(excinfo.value)