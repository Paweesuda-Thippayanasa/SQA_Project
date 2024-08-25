from abc import ABC, abstractmethod
from datetime import datetime
from enum import Enum
from typing import Optional

class AppointmentType(Enum):
    EXTRACTION = "Tooth Extraction"
    RUBBER_BAND_CHANGE = "Monthly Rubber Band Change"
    BRACES_REMOVAL = "Braces Removal"
    BRACES_FITTING = "Braces Fitting"

class AppointmentScheduler(ABC):
    """
    Abstract base class for appointment scheduling using the Template Method pattern.
    """

    def __init__(
        self,
        doctor_name: str,
        patient_name: str,
        appointment_type: AppointmentType,
        date_time: datetime,
        note: Optional[str] = None,
        creator_name: str = "System",
    ):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.creator_name = creator_name
        self.clinic_contact = "+1-555-123-4567" 

    def schedule(self):
        """Template method for scheduling an appointment."""
        self._validate_input()
        self._check_doctor_availability()
        self._save_appointment()
        self._send_confirmation()

    @abstractmethod
    def _validate_input(self):
        """Validate appointment details (to be implemented by subclasses)."""
        pass

    @abstractmethod
    def _check_doctor_availability(self):
        """Check doctor's availability (to be implemented by subclasses)."""
        pass

    @abstractmethod
    def _save_appointment(self):
        """Save appointment details (to be implemented by subclasses)."""
        pass

    def _send_confirmation(self):
        """Send appointment confirmation."""
        print(
            f"Appointment Confirmation:\n"
            f"Doctor: {self.doctor_name}\n"
            f"Patient: {self.patient_name}\n"
            f"Type: {self.appointment_type.value}\n"
            f"Date & Time: {self.date_time.strftime('%Y-%m-%d %H:%M')}\n"
            f"Note: {self.note}\n"
            f"Created by: {self.creator_name}\n"
            f"Clinic Contact: {self.clinic_contact}\n"
        )


class BasicAppointmentScheduler(AppointmentScheduler):
    """
    Concrete class for basic appointment scheduling.
    """

    def _validate_input(self):
        if not all(
            [
                isinstance(arg, str)
                for arg in [self.doctor_name, self.patient_name]
            ]
        ):
            raise TypeError("Doctor name and patient name must be strings.")

        if not isinstance(self.appointment_type, AppointmentType):
            raise TypeError(
                "Appointment type must be a valid AppointmentType enum value."
            )

        if not isinstance(self.date_time, datetime):
            raise TypeError("Appointment date and time must be a datetime object.")

    def _check_doctor_availability(self):
        print(f"Checking {self.doctor_name}'s availability for {self.date_time}...")

    def _save_appointment(self):
        print(
            f"Saving appointment for {self.patient_name} with {self.doctor_name} on {self.date_time}..."
        )



class AppointmentType(Enum):
    EXTRACTION = "Tooth Extraction"
    RUBBER_BAND_CHANGE = "Monthly Rubber Band Change"
    BRACES_REMOVAL = "Braces Removal"
    BRACES_FITTING = "Braces Fitting"

class AppointmentScheduler(ABC):
    """
    Abstract base class for appointment scheduling using the Template Method pattern.
    """

    def __init__(
        self,
        doctor_name: str,
        patient_name: str,
        appointment_type: AppointmentType,
        date_time: datetime,
        note: Optional[str] = None,
        creator_name: str = "System",
    ):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.creator_name = creator_name
        self.clinic_contact = "+1-555-123-4567" 

    def schedule(self):
        """Template method for scheduling an appointment."""
        self._validate_input()
        self._check_doctor_availability()
        self._save_appointment()
        self._send_confirmation()

    @abstractmethod
    def _validate_input(self):
        """Validate appointment details (to be implemented by subclasses)."""
        pass

    @abstractmethod
    def _check_doctor_availability(self):
        """Check doctor's availability (to be implemented by subclasses)."""
        pass

    @abstractmethod
    def _save_appointment(self):
        """Save appointment details (to be implemented by subclasses)."""
        pass

    def _send_confirmation(self):
        """Send appointment confirmation."""
        print(
            f"Appointment Confirmation:\n"
            f"Doctor: {self.doctor_name}\n"
            f"Patient: {self.patient_name}\n"
            f"Type: {self.appointment_type.value}\n"
            f"Date & Time: {self.date_time.strftime('%Y-%m-%d %H:%M')}\n"
            f"Note: {self.note}\n"
            f"Created by: {self.creator_name}\n"
            f"Clinic Contact: {self.clinic_contact}\n"
        )


class BasicAppointmentScheduler(AppointmentScheduler):
    """
    Concrete class for basic appointment scheduling.
    """

    def _validate_input(self):
        if not all(
            [
                isinstance(arg, str)
                for arg in [self.doctor_name, self.patient_name]
            ]
        ):
            raise TypeError("Doctor name and patient name must be strings.")

        if not isinstance(self.appointment_type, AppointmentType):
            raise TypeError(
                "Appointment type must be a valid AppointmentType enum value."
            )

        if not isinstance(self.date_time, datetime):
            raise TypeError("Appointment date and time must be a datetime object.")

    def _check_doctor_availability(self):
        print(f"Checking {self.doctor_name}'s availability for {self.date_time}...")

    def _save_appointment(self):
        print(
            f"Saving appointment for {self.patient_name} with {self.doctor_name} on {self.date_time}..."
        )
