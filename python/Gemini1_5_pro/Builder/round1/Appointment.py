from dataclasses import dataclass
from enum import Enum
from typing import Optional


class AppointmentType(Enum):
    TOOTH_EXTRACTION = "Tooth Extraction"
    RUBBER_BAND_CHANGE = "Rubber Band Change"
    BRACES_REMOVAL = "Braces Removal"
    BRACES_FITTING = "Braces Fitting"


@dataclass
class Appointment:
    doctor_name: str
    patient_name: str
    appointment_type: AppointmentType
    date: str
    time: str
    note: Optional[str] = None
    created_by: Optional[str] = None
    clinic_contact_number: Optional[str] = None


class AppointmentBuilder:
    def __init__(self):
        self.appointment = Appointment(None, None, None, None, None)

    def set_doctor_name(self, doctor_name: str):
        self.appointment.doctor_name = doctor_name
        return self

    def set_patient_name(self, patient_name: str):
        self.appointment.patient_name = patient_name
        return self

    def set_appointment_type(self, appointment_type: AppointmentType):
        self.appointment.appointment_type = appointment_type
        return self

    def set_date(self, date: str):
        self.appointment.date = date
        return self

    def set_time(self, time: str):
        self.appointment.time = time
        return self

    def set_note(self, note: str):
        self.appointment.note = note
        return self

    def set_created_by(self, created_by: str):
        self.appointment.created_by = created_by
        return self

    def set_clinic_contact_number(self, clinic_contact_number: str):
        self.appointment.clinic_contact_number = clinic_contact_number
        return self

    def build(self) -> Appointment:
        if not all(
            hasattr(self.appointment, attr) and getattr(self.appointment, attr) is not None
            for attr in ["doctor_name", "patient_name", "appointment_type", "date", "time"]
        ):
            raise ValueError("Missing required fields in appointment")
        return self.appointment