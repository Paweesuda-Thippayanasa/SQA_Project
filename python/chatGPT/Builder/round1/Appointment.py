
class Appointment:
    def __init__(self, doctor_name, patient_name, appointment_type, date_time, note, creator_name, clinic_contact):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.creator_name = creator_name
        self.clinic_contact = clinic_contact

    def __str__(self):
        return (f"Appointment with Dr. {self.doctor_name} for {self.patient_name} "
                f"on {self.date_time} for {self.appointment_type}. "
                f"Note: {self.note}. "
                f"Appointment created by {self.creator_name}. "
                f"Contact: {self.clinic_contact}")
