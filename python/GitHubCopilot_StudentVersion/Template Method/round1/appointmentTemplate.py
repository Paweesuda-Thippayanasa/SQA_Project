from abc import ABC, abstractmethod
from datetime import datetime

# Abstract Base Class for Appointments
class Appointment(ABC):
    def __init__(self, doctor, patient, date_time, note, creator, contact_number):
        self.doctor = doctor
        self.patient = patient
        self.date_time = date_time
        self.note = note
        self.creator = creator
        self.contact_number = contact_number

    def schedule_appointment(self):
        self.check_availability()
        self.book_slot()
        self.send_confirmation()

    @abstractmethod
    def check_availability(self):
        pass

    @abstractmethod
    def book_slot(self):
        pass

    @abstractmethod
    def send_confirmation(self):
        pass

# Concrete Appointment Types
class ToothExtraction(Appointment):
    def check_availability(self):
        print(f"Checking availability for {self.doctor.name} on {self.date_time}")

    def book_slot(self):
        print(f"Booking slot for tooth extraction with {self.doctor.name} for {self.patient.name} on {self.date_time}")

    def send_confirmation(self):
        print(f"Sending confirmation to {self.patient.name} for tooth extraction on {self.date_time}")

class MonthlyRubberBandChange(Appointment):
    def check_availability(self):
        print(f"Checking availability for {self.doctor.name} on {self.date_time}")

    def book_slot(self):
        print(f"Booking slot for monthly rubber band change with {self.doctor.name} for {self.patient.name} on {self.date_time}")

    def send_confirmation(self):
        print(f"Sending confirmation to {self.patient.name} for monthly rubber band change on {self.date_time}")

class RemovalOfBraces(Appointment):
    def check_availability(self):
        print(f"Checking availability for {self.doctor.name} on {self.date_time}")

    def book_slot(self):
        print(f"Booking slot for removal of braces with {self.doctor.name} for {self.patient.name} on {self.date_time}")

    def send_confirmation(self):
        print(f"Sending confirmation to {self.patient.name} for removal of braces on {self.date_time}")

class FittingOfBraces(Appointment):
    def check_availability(self):
        print(f"Checking availability for {self.doctor.name} on {self.date_time}")

    def book_slot(self):
        print(f"Booking slot for fitting of braces with {self.doctor.name} for {self.patient.name} on {self.date_time}")

    def send_confirmation(self):
        print(f"Sending confirmation to {self.patient.name} for fitting of braces on {self.date_time}")

# Doctor and Patient Classes
class Doctor:
    def __init__(self, name, contact_number):
        self.name = name
        self.contact_number = contact_number

class Patient:
    def __init__(self, name, doctor):
        self.name = name
        self.doctor = doctor

# Appointment Scheduler
class AppointmentScheduler:
    def __init__(self):
        self.appointments = []

    def create_appointment(self, appointment_type, doctor, patient, date_time, note, creator, contact_number):
        appointment = appointment_type(doctor, patient, date_time, note, creator, contact_number)
        appointment.schedule_appointment()
        self.appointments.append(appointment)
