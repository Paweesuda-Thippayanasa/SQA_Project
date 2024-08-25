
from abc import ABC, abstractmethod
from datetime import datetime

class AppointmentScheduler:
    """
    Abstract base class for scheduling appointments.
    Implements the Template Method pattern.
    """

    def schedule_appointment(self, doctor_name, patient_name, appointment_type, appointment_datetime, note, created_by):
        """
        Template method for scheduling an appointment.
        """
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.appointment_datetime = appointment_datetime
        self.note = note
        self.created_by = created_by
        self.clinic_contact_number = "+1-555-123-4567" 
        self.validate_appointment()
        return self.create_appointment_record()

    @abstractmethod
    def validate_appointment(self):
        """
        Abstract method to be implemented by subclasses
        to validate the appointment details.
        """
        pass

    def create_appointment_record(self):
        """
        Creates the appointment record with all necessary details.
        """
        appointment_record = {
            "doctor_name": self.doctor_name,
            "patient_name": self.patient_name,
            "appointment_type": self.appointment_type,
            "appointment_datetime": self.appointment_datetime.strftime("%Y-%m-%d %H:%M"),
            "note": self.note,
            "created_by": self.created_by,
            "clinic_contact_number": self.clinic_contact_number,
        }
        return appointment_record

class ToothExtractionAppointment(AppointmentScheduler):
    """
    Concrete class for scheduling tooth extraction appointments.
    """

    def validate_appointment(self):
        """
        Validates if the doctor is qualified for tooth extraction.
        """
        # Placeholder for validation logic
        # Example: Check if doctor's specialization includes tooth extraction
        is_valid = True  # Replace with actual validation logic
        if not is_valid:
            raise ValueError("Invalid appointment: Doctor not qualified for tooth extraction.")

class RubberBandChangeAppointment(AppointmentScheduler):
    """
    Concrete class for scheduling rubber band change appointments.
    """

    def validate_appointment(self):
        """
        Validates if the appointment is within the allowed frequency.
        """
        # Placeholder for validation logic
        # Example: Check if the last appointment was at least 3 weeks ago
        is_valid = True  # Replace with actual validation logic
        if not is_valid:
            raise ValueError("Invalid appointment: Rubber band change appointments should be at least 3 weeks apart.")

class BracesRemovalAppointment(AppointmentScheduler):
    """
    Concrete class for scheduling braces removal appointments.
    """

    def validate_appointment(self):
        """
        Validates if the patient has braces to remove.
        """
        # Placeholder for validation logic
        # Example: Check patient's record to see if they have braces
        is_valid = True  # Replace with actual validation logic
        if not is_valid:
            raise ValueError("Invalid appointment: Patient does not have braces to remove.")

class BracesFittingAppointment(AppointmentScheduler):
    """
    Concrete class for scheduling braces fitting appointments.
    """

    def validate_appointment(self):
        """
        Validates if the patient does not already have braces.
        """
        # Placeholder for validation logic
        # Example: Check patient's record to see if they already have braces
        is_valid = True  # Replace with actual validation logic
        if not is_valid:
            raise ValueError("Invalid appointment: Patient already has braces.")
