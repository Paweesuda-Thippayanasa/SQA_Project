# test_appointment.py

import pytest
from appointmentTemplate  import create_appointment, ToothExtractionAppointment, MonthlyRubberBandChangeAppointment, BracesRemovalAppointment, BracesFittingAppointment
from datetime import datetime

@pytest.mark.parametrize("appointment_type, expected_class", [
    ("Tooth Extraction", ToothExtractionAppointment),
    ("Monthly Rubber Band Change", MonthlyRubberBandChangeAppointment),
    ("Removal of Braces", BracesRemovalAppointment),
    ("Fitting of Braces", BracesFittingAppointment),
])
def test_create_appointment(appointment_type, expected_class):
    """Test function with 100% statement coverage for `create_appointment`."""
    doctor_name = "Dr. Smith"
    patient_name = "John Doe"
    date_time = datetime.now()
    note = "Please bring your insurance card."
    creator_name = "Alice"
    clinic_number = "123-456-7890"

    appointment = create_appointment(appointment_type, doctor_name, patient_name, date_time, note, creator_name, clinic_number)
    assert isinstance(appointment, expected_class)

def test_create_appointment_invalid_type():
    """Test for invalid appointment type."""
    with pytest.raises(ValueError):
        create_appointment("Invalid Type", "Dr. Smith", "John Doe", datetime.now(), "Please bring your insurance card.", "Alice", "123-456-7890")
