# appointment.py

from abc import ABC, abstractmethod
from datetime import datetime

class Appointment(ABC):
    """Abstract class for all appointment types."""

    def __init__(self, doctor, patient, date_time, note, creator, clinic_contact):
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time
        self.note = note
        self.creator = creator
        self.clinic_contact = clinic_contact

    @abstractmethod
    def get_appointment_type(self):
        """Returns the type of appointment."""
        pass

    def schedule(self):
        """Template method for scheduling an appointment."""
        self._validate_appointment()
        self._create_appointment_record()
        self._send_confirmation()

    def _validate_appointment(self):
        """Validates the appointment details."""
        # Placeholder for validation logic
        print(f"Validating appointment for {self.patient} on {self.date_time}")

    def _create_appointment_record(self):
        """Creates the appointment record."""
        print(f"Creating appointment record for {self.patient} with {self.doctor}")

    def _send_confirmation(self):
        """Sends confirmation to the patient."""
        print(f"Sending confirmation to {self.patient} for the appointment on {self.date_time}")

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
