import datetime
from AppointmentBuilder import AppointmentBuilder


class AppointmentDirector:
    def __init__(self, builder: AppointmentBuilder):
        self._builder = builder

    def construct(self, doctor_name: str, patient_name: str, appointment_type: str, 
                  date_time: datetime, note: str, creator_name: str, contact_number: str):
        self._builder.set_doctor_name(doctor_name)\
                     .set_patient_name(patient_name)\
                     .set_appointment_type(appointment_type)\
                     .set_date_time(date_time)\
                     .set_note(note)\
                     .set_creator_name(creator_name)\
                     .set_clinic_contact_number(contact_number)
        return self._builder.get_appointment()
