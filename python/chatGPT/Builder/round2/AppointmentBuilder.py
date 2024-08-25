import datetime
from Appointment import Appointment

class AppointmentBuilder:
    def __init__(self):
        self.appointment = Appointment()

    def set_doctor_name(self, name: str):
        self.appointment.doctor_name = name
        return self

    def set_patient_name(self, name: str):
        self.appointment.patient_name = name
        return self

    def set_appointment_type(self, appointment_type: str):
        self.appointment.appointment_type = appointment_type
        return self

    def set_date_time(self, date_time: datetime):
        self.appointment.date_time = date_time
        return self

    def set_note(self, note: str):
        self.appointment.note = note
        return self

    def set_creator_name(self, creator_name: str):
        self.appointment.creator_name = creator_name
        return self

    def set_clinic_contact(self, contact: str):
        self.appointment.clinic_contact = contact
        return self

    def build(self):
        return self.appointment