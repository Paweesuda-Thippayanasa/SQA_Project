# appointment_scheduler.py
from abc import ABC, abstractmethod
from datetime import datetime

class Appointment:
    def __init__(self, doctor_name, patient_name, appointment_type, date_time, note, created_by, contact_number):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.created_by = created_by
        self.contact_number = contact_number

    def __str__(self):
        return f"Appointment({self.doctor_name}, {self.patient_name}, {self.appointment_type}, {self.date_time}, {self.note}, {self.created_by}, {self.contact_number})"

class AppointmentScheduler(ABC):
    def schedule_appointment(self, doctor_name, patient_name, date_time, note, created_by, contact_number):
        appointment_type = self.get_appointment_type()
        appointment = Appointment(doctor_name, patient_name, appointment_type, date_time, note, created_by, contact_number)
        self.save_appointment(appointment)
        return appointment

    @abstractmethod
    def get_appointment_type(self):
        pass

    def save_appointment(self, appointment):
        # Placeholder for saving the appointment to a database or file
        print(f"Saving appointment: {appointment}")

class ToothExtractionScheduler(AppointmentScheduler):
    def get_appointment_type(self):
        return "Tooth Extraction"

class RubberBandChangeScheduler(AppointmentScheduler):
    def get_appointment_type(self):
        return "Monthly Rubber Band Change"

class RemovalOfBracesScheduler(AppointmentScheduler):
    def get_appointment_type(self):
        return "Removal of Braces"

class FittingOfBracesScheduler(AppointmentScheduler):
    def get_appointment_type(self):
        return "Fitting of Braces"
