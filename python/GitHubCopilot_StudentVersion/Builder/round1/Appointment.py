# appointment.py
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
        return f"Appointment({self.doctor_name}, {self.patient_name}, {self.appointment_type}, {self.date_time}, {self.note}, {self.creator_name}, {self.clinic_contact})"


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

    def set_note (self, note):
        self._note = note
        return self

    def set_creator_name(self, creator_name):
        self._creator_name = creator_name
        return self

    def set_clinic_contact(self, clinic_contact):
        self._clinic_contact = clinic_contact
        return self

    def build(self):
        return Appointment(self._doctor_name, self._patient_name, self._appointment_type, self._date_time, self._note, self._creator_name, self._clinic_contact)


class AppointmentDirector:
    def __init__(self, builder):
        self._builder = builder

    def construct_tooth_extraction(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return self._builder.set_doctor_name(doctor_name).set_patient_name(patient_name).set_appointment_type("Tooth Extraction").set_date_time(date_time).set_note(note).set_creator_name(creator_name).set_clinic_contact(clinic_contact).build()

    def construct_monthly_rubber_band_change(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return self._builder.set_doctor_name(doctor_name).set_patient_name(patient_name).set_appointment_type("Monthly Rubber Band Change").set_date_time(date_time).set_note(note).set_creator_name(creator_name).set_clinic_contact(clinic_contact).build()

    def construct_removal_of_braces(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return self._builder.set_doctor_name(doctor_name).set_patient_name(patient_name).set_appointment_type("Removal of Braces").set_date_time(date_time).set_note(note).set_creator_name(creator_name).set_clinic_contact(clinic_contact).build()

    def construct_fitting_of_braces(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return self._builder.set_doctor_name(doctor_name).set_patient_name(patient_name).set_appointment_type("Fitting of Braces").set_date_time(date_time).set_note(note).set_creator_name(creator_name).set_clinic_contact(clinic_contact).build()