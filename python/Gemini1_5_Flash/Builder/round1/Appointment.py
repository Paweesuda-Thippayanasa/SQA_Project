class Appointment:
    """Represents an appointment at the orthodontic clinic."""

    def __init__(self, doctor, patient, appointment_type, date_time, note, creator, clinic_phone):
        self.doctor = doctor
        self.patient = patient
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.creator = creator
        self.clinic_phone = clinic_phone

    def __str__(self):
        return f"Appointment for {self.patient} with {self.doctor} on {self.date_time.strftime('%Y-%m-%d %H:%M')} for {self.appointment_type}"
