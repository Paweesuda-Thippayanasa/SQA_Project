from abc import ABC, abstractmethod
from datetime import datetime

# Base class for appointment
class AppointmentTemplate(ABC):
    def schedule_appointment(self, doctor_name, patient_name, date_time, created_by, clinic_contact):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.date_time = date_time
        self.created_by = created_by
        self.clinic_contact = clinic_contact
        
        self.gather_patient_details()
        self.perform_appointment_specific_task()
        self.add_doctor_note()
        self.finalize_appointment()
    
    @abstractmethod
    def perform_appointment_specific_task(self):
        pass
    
    def gather_patient_details(self):
        print(f"Gathering details for patient {self.patient_name} with Dr. {self.doctor_name}.")
    
    def add_doctor_note(self):
        self.note = "Please take painkillers after the extraction."  # Simulated input for testing
    
    def finalize_appointment(self):
        print(f"Appointment for {self.patient_name} with Dr. {self.doctor_name} scheduled on {self.date_time}.")

# Subclasses for specific appointment types
class ToothExtractionAppointment(AppointmentTemplate):
    def perform_appointment_specific_task(self):
        print("Scheduling a tooth extraction appointment.")

class MonthlyRubberBandChangeAppointment(AppointmentTemplate):
    def perform_appointment_specific_task(self):
        print("Scheduling a monthly rubber band change appointment.")

class RemovalOfBracesAppointment(AppointmentTemplate):
    def perform_appointment_specific_task(self):
        print("Scheduling a braces removal appointment.")

class FittingOfBracesAppointment(AppointmentTemplate):
    def perform_appointment_specific_task(self):
        print("Scheduling a braces fitting appointment.")

# Function to create an appointment
def create_appointment(appointment_type, doctor_name, patient_name, date_time, created_by, clinic_contact):
    appointment = appointment_type()
    appointment.schedule_appointment(doctor_name, patient_name, date_time, created_by, clinic_contact)
    return appointment
