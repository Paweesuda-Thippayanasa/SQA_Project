from abc import ABC, abstractmethod
from datetime import datetime

# Base class for appointment scheduling using the Template Method pattern
class AppointmentScheduler(ABC):
    def schedule_appointment(self, doctor_name, patient_name, date_time, created_by, clinic_contact):
        appointment = self.create_appointment(doctor_name, patient_name, date_time, created_by, clinic_contact)
        self.add_note()
        self.send_confirmation(appointment)
        return appointment

    @abstractmethod
    def create_appointment(self, doctor_name, patient_name, date_time, created_by, clinic_contact):
        pass

    @abstractmethod
    def add_note(self):
        pass

    def send_confirmation(self, appointment):
        print(f"Confirmation sent for {appointment['type']} on {appointment['date_time']} to {appointment['patient_name']}")

# Concrete class for Tooth Extraction appointments
class ToothExtractionAppointment(AppointmentScheduler):
    def create_appointment(self, doctor_name, patient_name, date_time, created_by, clinic_contact):
        return {
            "doctor_name": doctor_name,
            "patient_name": patient_name,
            "type": "Tooth Extraction",
            "date_time": date_time,
            "created_by": created_by,
            "clinic_contact": clinic_contact,
            "note": ""
        }

    def add_note(self):
        print("Note: The patient should avoid eating 2 hours before the extraction.")

# Concrete class for Monthly Rubber Band Change appointments
class MonthlyRubberBandChangeAppointment(AppointmentScheduler):
    def create_appointment(self, doctor_name, patient_name, date_time, created_by, clinic_contact):
        return {
            "doctor_name": doctor_name,
            "patient_name": patient_name,
            "type": "Monthly Rubber Band Change",
            "date_time": date_time,
            "created_by": created_by,
            "clinic_contact": clinic_contact,
            "note": ""
        }

    def add_note(self):
        print("Note: The patient should bring the previous set of rubber bands.")

# Concrete class for Removal of Braces appointments
class RemovalOfBracesAppointment(AppointmentScheduler):
    def create_appointment(self, doctor_name, patient_name, date_time, created_by, clinic_contact):
        return {
            "doctor_name": doctor_name,
            "patient_name": patient_name,
            "type": "Removal of Braces",
            "date_time": date_time,
            "created_by": created_by,
            "clinic_contact": clinic_contact,
            "note": ""
        }

    def add_note(self):
        print("Note: The patient should bring retainers for the fitting.")

# Concrete class for Fitting of Braces appointments
class FittingOfBracesAppointment(AppointmentScheduler):
    def create_appointment(self, doctor_name, patient_name, date_time, created_by, clinic_contact):
        return {
            "doctor_name": doctor_name,
            "patient_name": patient_name,
            "type": "Fitting of Braces",
            "date_time": date_time,
            "created_by": created_by,
            "clinic_contact": clinic_contact,
            "note": ""
        }

    def add_note(self):
        print("Note: The patient should expect some discomfort during the fitting process.")
