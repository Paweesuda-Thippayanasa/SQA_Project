from datetime import datetime

class Appointment:
    """Represents an appointment record."""

    def __init__(self, doctor_name, patient_name, appointment_type, date_time, note, creator_name, clinic_contact_number):
        self.doctor_name = doctor_name
        self.patient_name = patient_name
        self.appointment_type = appointment_type
        self.date_time = date_time
        self.note = note
        self.creator_name = creator_name
        self.clinic_contact_number = clinic_contact_number

    def __str__(self):
        return f"Appointment for {self.patient_name} with Dr. {self.doctor_name} for {self.appointment_type} on {self.date_time}."

class AppointmentBuilder:
    """The builder pattern for constructing Appointment objects."""

    def __init__(self):
        self.appointment = Appointment(None, None, None, None, None, None, None)

    def with_doctor(self, doctor_name):
        self.appointment.doctor_name = doctor_name
        return self

    def for_patient(self, patient_name):
        self.appointment.patient_name = patient_name
        return self

    def of_type(self, appointment_type):
        self.appointment.appointment_type = appointment_type
        return self

    def on_date_time(self, date_time):
        self.appointment.date_time = date_time
        return self

    def with_note(self, note):
        self.appointment.note = note
        return self

    def created_by(self, creator_name):
        self.appointment.creator_name = creator_name
        return self

    def at_clinic_number(self, clinic_contact_number):
        self.appointment.clinic_contact_number = clinic_contact_number
        return self

    def build(self):
        return self.appointment

# Example usage
appointment_builder = AppointmentBuilder()
appointment = appointment_builder.with_doctor("Dr. Smith")\
                                 .for_patient("John Doe")\
                                 .of_type("Tooth Extraction")\
                                 .on_date_time(datetime(2024, 3, 15, 10, 0, 0))\
                                 .with_note("Please bring your insurance card.")\
                                 .created_by("Alice")\
                                 .at_clinic_number("123-456-7890")\
                                 .build()

print(appointment)