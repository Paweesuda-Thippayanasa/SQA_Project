# appointment.py

from abc import ABC, abstractmethod
from datetime import datetime

class Appointment(ABC):
    """Abstract class representing an appointment."""

    def __init__(self, doctor_name, patient_name, appointment_type, date_time, note, creator_name, clinic_number):
        """
        Initializes an appointment with common attributes.

        Args:
            doctor_name (str): Name of the doctor.
            patient_name (str): Name of the patient.
            appointment_type (str): Type of appointment.
            date_time (datetime): Date and time of the appointment.
            note (str): Doctor's note for the patient.
            creator_name (str): Name of the person creating the appointment.
            clinic_number (str): Clinic's contact number.
        """
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.creator_name = creator_name
        self.clinic_number = clinic_number

    @abstractmethod
    def schedule(self):
        """Abstract method to schedule the appointment. This method will be implemented by concrete subclasses."""
        pass

class ToothExtractionAppointment(Appointment):
    """Concrete class representing a tooth extraction appointment."""

    def schedule(self):
        """Schedules a tooth extraction appointment."""
        print(f"Tooth extraction appointment scheduled for {self.patient_name} with Dr. {self.doctor_name} on {self.date_time.strftime('%Y-%m-%d %H:%M')}")
        print(f"Note: {self.note}")

class MonthlyRubberBandChangeAppointment(Appointment):
    """Concrete class representing a monthly rubber band change appointment."""

    def schedule(self):
        """Schedules a monthly rubber band change appointment."""
        print(f"Monthly rubber band change appointment scheduled for {self.patient_name} with Dr. {self.doctor_name} on {self.date_time.strftime('%Y-%m-%d %H:%M')}")
        print(f"Note: {self.note}")

class BracesRemovalAppointment(Appointment):
    """Concrete class representing a braces removal appointment."""

    def schedule(self):
        """Schedules a braces removal appointment."""
        print(f"Braces removal appointment scheduled for {self.patient_name} with Dr. {self.doctor_name} on {self.date_time.strftime('%Y-%m-%d %H:%M')}")
        print(f"Note: {self.note}")

class BracesFittingAppointment(Appointment):
    """Concrete class representing a braces fitting appointment."""

    def schedule(self):
        """Schedules a braces fitting appointment."""
        print(f"Braces fitting appointment scheduled for {self.patient_name} with Dr. {self.doctor_name} on {self.date_time.strftime('%Y-%m-%d %H:%M')}")
        print(f"Note: {self.note}")

def create_appointment(appointment_type, doctor_name, patient_name, date_time, note, creator_name, clinic_number):
    """Creates an appointment based on the given type."""
    if appointment_type == "Tooth Extraction":
        return ToothExtractionAppointment(doctor_name, patient_name, appointment_type, date_time, note, creator_name, clinic_number)
    elif appointment_type == "Monthly Rubber Band Change":
        return MonthlyRubberBandChangeAppointment(doctor_name, patient_name, appointment_type, date_time, note, creator_name, clinic_number)
    elif appointment_type == "Removal of Braces":
        return BracesRemovalAppointment(doctor_name, patient_name, appointment_type, date_time, note, creator_name, clinic_number)
    elif appointment_type == "Fitting of Braces":
        return BracesFittingAppointment(doctor_name, patient_name, appointment_type, date_time, note, creator_name, clinic_number)
    else:
        raise ValueError("Invalid appointment type.")
