from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class Appointment:
    """Represents an appointment with all its details."""
    doctor_name: str
    patient_name: str
    appointment_type: str
    date_time: datetime
    note: Optional[str] = None
    created_by: Optional[str] = None
    clinic_contact_number: Optional[str] = None

class AppointmentBuilder:
    """Builder class for creating Appointment objects step-by-step."""

    def __init__(self):
        self.appointment = Appointment(None, None, None, None)

    def for_doctor(self, doctor_name: str) -> 'AppointmentBuilder':
        self.appointment.doctor_name = doctor_name
        return self

    def for_patient(self, patient_name: str) -> 'AppointmentBuilder':
        self.appointment.patient_name = patient_name
        return self

    def with_type(self, appointment_type: str) -> 'AppointmentBuilder':
        self.appointment.appointment_type = appointment_type
        return self

    def on_date_time(self, date_time: datetime) -> 'AppointmentBuilder':
        self.appointment.date_time = date_time
        return self

    def with_note(self, note: str) -> 'AppointmentBuilder':
        self.appointment.note = note
        return self

    def created_by(self, created_by: str) -> 'AppointmentBuilder':
        self.appointment.created_by = created_by
        return self

    def with_clinic_contact(self, clinic_contact_number: str) -> 'AppointmentBuilder':
        self.appointment.clinic_contact_number = clinic_contact_number
        return self

    def build(self) -> Appointment:
        if not all([self.appointment.doctor_name, self.appointment.patient_name, 
                    self.appointment.appointment_type, self.appointment.date_time]):
            raise ValueError("Doctor, patient, type and date/time are required.")
        return self.appointment