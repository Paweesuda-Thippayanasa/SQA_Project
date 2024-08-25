class AppointmentDirector:
    def __init__(self, builder):
        self._builder = builder

    def create_tooth_extraction_appointment(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return (self._builder
                .set_doctor_name(doctor_name)
                .set_patient_name(patient_name)
                .set_appointment_type("Tooth Extraction")
                .set_date_time(date_time)
                .set_note(note)
                .set_creator_name(creator_name)
                .set_clinic_contact(clinic_contact)
                .build())

    def create_braces_fitting_appointment(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return (self._builder
                .set_doctor_name(doctor_name)
                .set_patient_name(patient_name)
                .set_appointment_type("Fitting of Braces")
                .set_date_time(date_time)
                .set_note(note)
                .set_creator_name(creator_name)
                .set_clinic_contact(clinic_contact)
                .build())

    def create_rubber_band_change_appointment(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return (self._builder
                .set_doctor_name(doctor_name)
                .set_patient_name(patient_name)
                .set_appointment_type("Monthly Rubber Band Change")
                .set_date_time(date_time)
                .set_note(note)
                .set_creator_name(creator_name)
                .set_clinic_contact(clinic_contact)
                .build())

    def create_braces_removal_appointment(self, doctor_name, patient_name, date_time, note, creator_name, clinic_contact):
        return (self._builder
                .set_doctor_name(doctor_name)
                .set_patient_name(patient_name)
                .set_appointment_type("Removal of Braces")
                .set_date_time(date_time)
                .set_note(note)
                .set_creator_name(creator_name)
                .set_clinic_contact(clinic_contact)
                .build())
