from abc import ABC, abstractmethod

class AppointmentTemplate(ABC):
    def schedule_appointment(self, doctor_name, patient_name, date_time, note, creator_name, contact_number):
        self.set_doctor_name(doctor_name)
        self.set_patient_name(patient_name)
        self.set_date_time(date_time)
        self.set_note(note)
        self.set_creator_name(creator_name)
        self.set_contact_number(contact_number)
        self.set_appointment_type()
        return self.create_appointment_record()

    @abstractmethod
    def set_appointment_type(self):
        pass

    def set_doctor_name(self, doctor_name):
        self.doctor_name = doctor_name

    def set_patient_name(self, patient_name):
        self.patient_name = patient_name

    def set_date_time(self, date_time):
        self.date_time = date_time

    def set_note(self, note):
        self.note = note

    def set_creator_name(self, creator_name):
        self.creator_name = creator_name

    def set_contact_number(self, contact_number):
        self.contact_number = contact_number

    def create_appointment_record(self):
        return AppointmentRecord(
            doctor_name=self.doctor_name,
            patient_name=self.patient_name,
            appointment_type=self.appointment_type,
            date_time=self.date_time,
            note=self.note,
            creator_name=self.creator_name,
            contact_number=self.contact_number
        )

class ToothExtractionAppointment(AppointmentTemplate):
    def set_appointment_type(self):
        self.appointment_type = "Tooth Extraction"

class RubberBandChangeAppointment(AppointmentTemplate):
    def set_appointment_type(self):
        self.appointment_type = "Monthly Rubber Band Change"

class BracesRemovalAppointment(AppointmentTemplate):
    def set_appointment_type(self):
        self.appointment_type = "Braces Removal"

class BracesFittingAppointment(AppointmentTemplate):
    def set_appointment_type(self):
        self.appointment_type = "Braces Fitting"

class AppointmentRecord:
    def __init__(self, doctor_name, patient_name, appointment_type, date_time, note, creator_name, contact_number):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.creator_name = creator_name
        self.contact_number = contact_number

class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def schedule(self, appointment_type, doctor_name, patient_name, date_time, note, creator_name, contact_number):
        if appointment_type == "Tooth Extraction":
            appointment = ToothExtractionAppointment()
        elif appointment_type == "Monthly Rubber Band Change":
            appointment = RubberBandChangeAppointment()
        elif appointment_type == "Braces Removal":
            appointment = BracesRemovalAppointment()
        elif appointment_type == "Braces Fitting":
            appointment = BracesFittingAppointment()
        else:
            raise ValueError("Invalid appointment type")

        record = appointment.schedule_appointment(doctor_name, patient_name, date_time, note, creator_name, contact_number)
        self.appointments.append(record)
        return record
