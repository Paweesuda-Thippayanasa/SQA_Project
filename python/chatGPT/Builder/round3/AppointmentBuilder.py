from abc import ABC, abstractmethod
from datetime import datetime

class AppointmentBuilder(ABC):
    @abstractmethod
    def set_doctor_name(self, doctor_name: str):
        pass

    @abstractmethod
    def set_patient_name(self, patient_name: str):
        pass

    @abstractmethod
    def set_appointment_type(self, appointment_type: str):
        pass

    @abstractmethod
    def set_date_time(self, date_time: datetime):
        pass

    @abstractmethod
    def set_note(self, note: str):
        pass

    @abstractmethod
    def set_creator_name(self, creator_name: str):
        pass

    @abstractmethod
    def set_clinic_contact_number(self, contact_number: str):
        pass

    @abstractmethod
    def get_appointment(self):
        pass
