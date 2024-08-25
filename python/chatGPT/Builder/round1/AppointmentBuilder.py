
from Appointment import Appointment
class AppointmentBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._doctor_name = None
        self._patient_name = None
        self._appointment_type = None
        self._date_time = None
        self._note = None
        self._creator_name = None
        self._clinic_contact = None

    def set_doctor_name(self, doctor_name):
        self._doctor_name = doctor_name
        return self

    def set_patient_name(self, patient_name):
        self._patient_name = patient_name
        return self

    def set_appointment_type(self, appointment_type):
        self._appointment_type = appointment_type
        return self

    def set_date_time(self, date_time):
        self._date_time = date_time
        return self

    def set_note(self, note):
        self._note = note
        return self

    def set_creator_name(self, creator_name):
        self._creator_name = creator_name
        return self

    def set_clinic_contact(self, clinic_contact):
        self._clinic_contact = clinic_contact
        return self

    def build(self):
        appointment = Appointment(
            doctor_name=self._doctor_name,
            patient_name=self._patient_name,
            appointment_type=self._appointment_type,
            date_time=self._date_time,
            note=self._note,
            creator_name=self._creator_name,
            clinic_contact=self._clinic_contact
        )
        self.reset()
        return appointment
