from datetime import datetime

class AppointmentBuilder:
    def __init__(self):
        self.doctor = None
        self.patient = None
        self.appointment_type = None
        self.date_time = None
        self.note = None
        self.creator = None
        self.clinic_contact = None

    def set_doctor(self, doctor):
        self.doctor = doctor
        return self

    def set_patient(self, patient):
        self.patient = patient
        return self

    def set_appointment_type(self, appointment_type):
        self.appointment_type = appointment_type
        return self

    def set_date_time(self, date_time):
        self.date_time = date_time
        return self

    def set_note(self, note):
        self.note = note
        return self

    def set_creator(self, creator):
        self.creator = creator
        return self

    def set_clinic_contact(self, clinic_contact):
        self.clinic_contact = clinic_contact
        return self

    def build(self):
        return Appointment(self.doctor, self.patient, self.appointment_type, 
                           self.date_time, self.note, self.creator, self.clinic_contact)


class Appointment:
    def __init__(self, doctor, patient, appointment_type, date_time, note, creator, clinic_contact):
        self.doctor = doctor
        self.patient = patient
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.creator = creator
        self.clinic_contact = clinic_contact

    def __str__(self):
        return f"Appointment for {self.patient} with Dr. {self.doctor} for {self.appointment_type} on {self.date_time}."