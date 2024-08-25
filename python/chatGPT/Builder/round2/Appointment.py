
class Appointment:
    def __init__(self):
        self.doctor_name = None
        self.patient_name = None
        self.appointment_type = None
        self.date_time = None
        self.note = None
        self.creator_name = None
        self.clinic_contact = None

    def __str__(self):
        return (f"Appointment:\n"
                f"Doctor: {self.doctor_name}\n"
                f"Patient: {self.patient_name}\n"
                f"Type: {self.appointment_type}\n"
                f"Date and Time: {self.date_time}\n"
                f"Note: {self.note}\n"
                f"Created by: {self.creator_name}\n"
                f"Clinic Contact: {self.clinic_contact}")
