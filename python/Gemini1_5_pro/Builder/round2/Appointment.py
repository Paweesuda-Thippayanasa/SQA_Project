from datetime import datetime


class Appointment:
    """Represents an appointment at the orthodontic clinic."""

    def __init__(self, builder):
        self.doctor = builder.doctor
        self.patient = builder.patient
        self.type = builder.type
        self.date_time = builder.date_time
        self.note = builder.note
        self.created_by = builder.created_by
        self.clinic_contact = builder.clinic_contact

    def __str__(self):
        """Returns a string representation of the appointment."""

        return (
            f"Appointment Details:\n"
            f"  Doctor: {self.doctor}\n"
            f"  Patient: {self.patient}\n"
            f"  Type: {self.type}\n"
            f"  Date & Time: {self.date_time.strftime('%Y-%m-%d %H:%M')}\n"
            f"  Note: {self.note}\n"
            f"  Created By: {self.created_by}\n"
            f"  Clinic Contact: {self.clinic_contact}"
        )


class AppointmentBuilder:
    """Builder class for creating Appointment objects."""

    def __init__(self):
        self.doctor = None
        self.patient = None
        self.type = None
        self.date_time = None
        self.note = None
        self.created_by = None
        self.clinic_contact = None

    def set_doctor(self, doctor: str):
        self.doctor = doctor
        return self

    def set_patient(self, patient: str):
        self.patient = patient
        return self

    def set_type(self, type: str):
        self.type = type
        return self

    def set_date_time(self, date_time: datetime):
        self.date_time = date_time
        return self

    def set_note(self, note: str):
        self.note = note
        return self

    def set_created_by(self, created_by: str):
        self.created_by = created_by
        return self

    def set_clinic_contact(self, clinic_contact: str):
        self.clinic_contact = clinic_contact
        return self

    def build(self):
        """Builds and returns an Appointment object."""

        if not all(
            [
                self.doctor,
                self.patient,
                self.type,
                self.date_time,
                self.created_by,
                self.clinic_contact,
            ]
        ):
            raise ValueError(
                "Doctor, Patient, Type, Date & Time, Created By, and Clinic Contact are required fields."
            )
        return Appointment(self)