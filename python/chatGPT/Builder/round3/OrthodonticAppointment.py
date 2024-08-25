class OrthodonticAppointment:
    def __init__(self):
        self.doctor_name = None
        self.patient_name = None
        self.appointment_type = None
        self.date_time = None
        self.note = None
        self.creator_name = None
        self.contact_number = None

    def __str__(self):
        return f"Appointment:\nDoctor: {self.doctor_name}\nPatient: {self.patient_name}\n" \
               f"Type: {self.appointment_type}\nDate & Time: {self.date_time}\n" \
               f"Note: {self.note}\nCreator: {self.creator_name}\n" \
               f"Contact: {self.contact_number}"
