package org.chatgpt.round2;
import java.time.LocalDateTime;

public class Appointment {
    private final String patientName;
    private final String doctorName;
    private final AppointmentType appointmentType;
    private final String bookedBy;
    private final String clinicContactNumber;
    private final LocalDateTime appointmentDateTime;
    private final String notes;

    // Private constructor to enforce the use of the Builder
    private Appointment(Builder builder) {
        this.patientName = builder.patientName;
        this.doctorName = builder.doctorName;
        this.appointmentType = builder.appointmentType;
        this.bookedBy = builder.bookedBy;
        this.clinicContactNumber = builder.clinicContactNumber;
        this.appointmentDateTime = builder.appointmentDateTime;
        this.notes = builder.notes;
    }

    // Getters for accessing the fields
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

    public String getClinicContactNumber() {
        return clinicContactNumber;
    }

    public LocalDateTime getAppointmentDateTime() {
        return appointmentDateTime;
    }

    public String getNotes() {
        return notes;
    }

    // Static Builder class
    public static class Builder {
        private final String patientName;
        private final String doctorName;
        private final AppointmentType appointmentType;
        private final String bookedBy;
        private final String clinicContactNumber;
        private final LocalDateTime appointmentDateTime;

        private String notes;

        // Constructor with required fields
        public Builder(String patientName, String doctorName, AppointmentType appointmentType, String bookedBy, String clinicContactNumber, LocalDateTime appointmentDateTime) {
            this.patientName = patientName;
            this.doctorName = doctorName;
            this.appointmentType = appointmentType;
            this.bookedBy = bookedBy;
            this.clinicContactNumber = clinicContactNumber;
            this.appointmentDateTime = appointmentDateTime;
        }

        // Optional notes field
        public Builder notes(String notes) {
            this.notes = notes;
            return this;
        }

        // Build method to create an Appointment object
        public Appointment build() {
            return new Appointment(this);
        }
    }
    // Main method
    public static void main(String[] args) {
    }
}

// Enum for AppointmentType
enum AppointmentType {
    TOOTH_EXTRACTION,
    DEVICE_INSTALLATION,
    MONTHLY_CHECKUP,
    DEVICE_REMOVAL;
}