from abc import ABC, abstractmethod
from datetime import datetime

class Appointment(ABC):
    def __init__(self, doctor_name, patient_name, appointment_type, date_time, note, created_by, clinic_contact):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.created_by = created_by
        self.clinic_contact = clinic_contact

    def schedule_appointment(self):
        if self._validate_details():
            self._save_appointment()
            return self._generate_confirmation()
        else:
            return "Appointment details are invalid."

    @abstractmethod
    def _validate_details(self):
        pass

    @abstractmethod
    def _save_appointment(self):
        pass

    @abstractmethod
    def _generate_confirmation(self):
        pass

class OrthodonticAppointment(Appointment):
    def _validate_details(self):
        # Basic validation logic
        return all([
            self.doctor_name,
            self.patient_name,
            self.appointment_type in ['tooth extraction', 'monthly rubber band change', 'removal of braces', 'fitting of braces'],
            isinstance(self.date_time, datetime),
            self.created_by,
            self.clinic_contact
        ])

    def _save_appointment(self):
        # In a real application, you would save this to a database
        print("Saving appointment details to database...")

    def _generate_confirmation(self):
        return (f"Appointment confirmed:\n"
                f"Doctor: {self.doctor_name}\n"
                f"Patient: {self.patient_name}\n"
                f"Type: {self.appointment_type}\n"
                f"Date & Time: {self.date_time}\n"
                f"Note: {self.note}\n"
                f"Created By: {self.created_by}\n"
                f"Clinic Contact: {self.clinic_contact}")

# Example usage
# if __name__ == "__main__":
#     appointment = OrthodonticAppointment(
#         doctor_name="Dr. Smith",
#         patient_name="John Doe",
#         appointment_type="tooth extraction",
#         date_time=datetime(2024, 8, 30, 10, 0),
#         note="Please arrive 10 minutes early.",
#         created_by="Receptionist",
#         clinic_contact="555-1234"
#     )
#     print(appointment.schedule_appointment())
