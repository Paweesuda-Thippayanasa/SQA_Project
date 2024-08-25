# appointment.py
from abc import ABC, abstractmethod

class Appointment(ABC):
    """Abstract base class for appointment types."""

    def __init__(self, doctor_name, patient_name, date, time, note, creator_name, clinic_contact):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.date = date
        self.time = time
        self.note = note
        self.creator_name = creator_name
        self.clinic_contact = clinic_contact

    @abstractmethod
    def get_appointment_type(self):
        """Returns the type of appointment."""
        pass

    def get_appointment_details(self):
        """Returns a dictionary containing all appointment details."""
        return {
            "doctor_name": self.doctor_name,
            "patient_name": self.patient_name,
            "appointment_type": self.get_appointment_type(),
            "date": self.date,
            "time": self.time,
            "note": self.note,
            "creator_name": self.creator_name,
            "clinic_contact": self.clinic_contact
        }


class ToothExtractionAppointment(Appointment):
    """Represents a tooth extraction appointment."""

    def get_appointment_type(self):
        return "Tooth Extraction"


class MonthlyRubberBandChangeAppointment(Appointment):
    """Represents a monthly rubber band change appointment."""

    def get_appointment_type(self):
        return "Monthly Rubber Band Change"


class RemovalOfBracesAppointment(Appointment):
    """Represents a removal of braces appointment."""

    def get_appointment_type(self):
        return "Removal of Braces"


class FittingOfBracesAppointment(Appointment):
    """Represents a fitting of braces appointment."""

    def get_appointment_type(self):
        return "Fitting of Braces"
