package org.chatgpt.round3;
import java.time.LocalDateTime;


public class Appointment {

    private final String patientName;
    private final String doctorName;
    private final AppointmentType appointmentType;
    private final String bookedBy;
    private final String clinicContact;
    private final LocalDateTime appointmentDateTime;
    private final String notes;

    private Appointment(Builder builder) {
        this.patientName = builder.patientName;
        this.doctorName = builder.doctorName;
        this.appointmentType = builder.appointmentType;
        this.bookedBy = builder.bookedBy;
        this.clinicContact = builder.clinicContact;
        this.appointmentDateTime = builder.appointmentDateTime;
        this.notes = builder.notes;
    }

    public static class Builder {
        private final String patientName;
        private final String doctorName;
        private final AppointmentType appointmentType;
        private final String bookedBy;
        private final String clinicContact;
        private final LocalDateTime appointmentDateTime;
        private String notes;

        public Builder(String patientName, String doctorName, AppointmentType appointmentType,
                       String bookedBy, String clinicContact, LocalDateTime appointmentDateTime) {
            this.patientName = patientName;
            this.doctorName = doctorName;
            this.appointmentType = appointmentType;
            this.bookedBy = bookedBy;
            this.clinicContact = clinicContact;
            this.appointmentDateTime = appointmentDateTime;
        }

        public Builder notes(String notes) {
            this.notes = notes;
            return this;
        }

        public Appointment build() {
            return new Appointment(this);
        }
    }

    // Getters for all fields

    public String getPatientName() {
        return patientName;
    }

    public String getDoctorName() {
        return doctorName;
    }

    public AppointmentType getAppointmentType() {
        return appointmentType;
    }

    public String getBookedBy() {
        return bookedBy;
    }

    public String getClinicContact() {
        return clinicContact;
    }

    public LocalDateTime getAppointmentDateTime() {
        return appointmentDateTime;
    }

    public String getNotes() {
        return notes;
    }
}

// Enum for Appointment Type
enum AppointmentType {
    TOOTH_EXTRACTION,
    DEVICE_INSTALLATION,
    MONTHLY_CHECKUP,
    DEVICE_REMOVAL
}