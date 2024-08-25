from AppointmentBuilder import AppointmentBuilder

class AppointmentDirector:
    def __init__(self, builder: AppointmentBuilder):
        self._builder = builder

    def construct_tooth_extraction_appointment(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return (self._builder.set_doctor_name(doctor_name)
                             .set_patient_name(patient_name)
                             .set_appointment_type("Tooth Extraction")
                             .set_date_time(date_time)
                             .set_note(note)
                             .set_creator_name(creator_name)
                             .set_clinic_contact(clinic_contact)
                             .build())

    def construct_rubber_band_change_appointment(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return (self._builder.set_doctor_name(doctor_name)
                             .set_patient_name(patient_name)
                             .set_appointment_type("Monthly Rubber Band Change")
                             .set_date_time(date_time)
                             .set_note(note)
                             .set_creator_name(creator_name)
                             .set_clinic_contact(clinic_contact)
                             .build())

    def construct_removal_of_braces_appointment(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return (self._builder.set_doctor_name(doctor_name)
                             .set_patient_name(patient_name)
                             .set_appointment_type("Removal of Braces")
                             .set_date_time(date_time)
                             .set_note(note)
                             .set_creator_name(creator_name)
                             .set_clinic_contact(clinic_contact)
                             .build())

    def construct_fitting_of_braces_appointment(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return (self._builder.set_doctor_name(doctor_name)
                             .set_patient_name(patient_name)
                             .set_appointment_type("Fitting of Braces")
                             .set_date_time(date_time)
                             .set_note(note)
                             .set_creator_name(creator_name)
                             .set_clinic_contact(clinic_contact)
                             .build())