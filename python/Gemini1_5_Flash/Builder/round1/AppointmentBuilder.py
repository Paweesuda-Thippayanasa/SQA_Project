from datetime import datetime

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

class AppointmentBuilder:
    """Builder pattern for creating appointments."""

    def __init__(self):
        self.appointment = Appointment(None, None, None, None, None, None, None)

    def with_doctor(self, doctor):
        self.appointment.doctor = doctor
        return self

    def for_patient(self, patient):
        self.appointment.patient = patient
        return self

    def with_type(self, appointment_type):
        self.appointment.appointment_type = appointment_type
        return self

    def at_datetime(self, date_time):
        self.appointment.date_time = date_time
        return self

    def with_note(self, note):
        self.appointment.note = note
        return self

    def created_by(self, creator):
        self.appointment.creator = creator
        return self

    def with_clinic_phone(self, clinic_phone):
        self.appointment.clinic_phone = clinic_phone
        return self

    def build(self):
        return self.appointment

# Example usage
builder = AppointmentBuilder()
appointment = builder.with_doctor("Dr. Smith") \
                   .for_patient("John Doe") \
                   .with_type("Tooth Extraction") \
                   .at_datetime(datetime(2024, 3, 15, 10, 0)) \
                   .with_note("Please bring a friend for support.") \
                   .created_by("Receptionist") \
                   .with_clinic_phone("+1 555-123-4567") \
                   .build()

print(appointment)