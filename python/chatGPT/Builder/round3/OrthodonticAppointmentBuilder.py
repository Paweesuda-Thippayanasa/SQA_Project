import datetime
from AppointmentBuilder import AppointmentBuilder
from OrthodonticAppointment import OrthodonticAppointment


class OrthodonticAppointmentBuilder(AppointmentBuilder):
    def __init__(self):
        self.appointment = OrthodonticAppointment()

    def set_doctor_name(self, doctor_name: str):
        self.appointment.doctor_name = doctor_name
        return self

    def set_patient_name(self, patient_name: str):
        self.appointment.patient_name = patient_name
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

    def set_clinic_contact_number(self, contact_number: str):
        self.appointment.contact_number = contact_number
        return self

    def get_appointment(self):
        return self.appointment
