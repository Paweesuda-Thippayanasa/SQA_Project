# appointment_scheduler.py

from abc import ABC, abstractmethod
from datetime import datetime

class Appointment(ABC):
    """Abstract base class for all appointment types."""

    def __init__(self, doctor_name, patient_name, date, time, note, creator_name, clinic_contact_number):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.date = date
        self.time = time
        self.note = note
        self.creator_name = creator_name
        self.clinic_contact_number = clinic_contact_number

    @abstractmethod
    def get_appointment_type(self):
        """Returns the type of appointment."""
        pass

    def get_appointment_details(self):
        """Returns a formatted string with the appointment details."""
        return f"Appointment Type: {self.get_appointment_type()}\n" \
               f"Doctor: {self.doctor_name}\n" \
               f"Patient: {self.patient_name}\n" \
               f"Date: {self.date.strftime('%Y-%m-%d')}\n" \
               f"Time: {self.time.strftime('%H:%M')}\n" \
               f"Note: {self.note}\n" \
               f"Created by: {self.creator_name}\n" \
               f"Clinic Contact Number: {self.clinic_contact_number}"

class ToothExtractionAppointment(Appointment):
    """Appointment for tooth extraction."""

    def get_appointment_type(self):
        return "Tooth Extraction"

class MonthlyRubberBandChangeAppointment(Appointment):
    """Appointment for monthly rubber band change."""

    def get_appointment_type(self):
        return "Monthly Rubber Band Change"

class RemovalOfBracesAppointment(Appointment):
    """Appointment for removal of braces."""

    def get_appointment_type(self):
        return "Removal of Braces"

class FittingOfBracesAppointment(Appointment):
    """Appointment for fitting of braces."""

    def get_appointment_type(self):
        return "Fitting of Braces"

# Define Appointment Types as Constants
TOOTH_EXTRACTION = "Tooth Extraction"
MONTHLY_RUBBER_BAND_CHANGE = "Monthly Rubber Band Change"
REMOVAL_OF_BRACES = "Removal of Braces"
FITTING_OF_BRACES = "Fitting of Braces"

class AppointmentScheduler:
    """Class responsible for scheduling appointments."""

    def __init__(self, clinic_contact_number):
        self.clinic_contact_number = clinic_contact_number

    def schedule_appointment(self, appointment_type, doctor_name, patient_name, date, time, note, creator_name):
        """Creates and schedules an appointment based on the given type."""

        if appointment_type == TOOTH_EXTRACTION:
            appointment = ToothExtractionAppointment(doctor_name, patient_name, date, time, note, creator_name, self.clinic_contact_number)
        elif appointment_type == MONTHLY_RUBBER_BAND_CHANGE:
            appointment = MonthlyRubberBandChangeAppointment(doctor_name, patient_name, date, time, note, creator_name, self.clinic_contact_number)
        elif appointment_type == REMOVAL_OF_BRACES:
            appointment = RemovalOfBracesAppointment(doctor_name, patient_name, date, time, note, creator_name, self.clinic_contact_number)
        elif appointment_type == FITTING_OF_BRACES:
            appointment = FittingOfBracesAppointment(doctor_name, patient_name, date, time, note, creator_name, self.clinic_contact_number)
        else:
            raise ValueError("Invalid appointment type.")

        # Perform any necessary checks or validations here

        return appointment
