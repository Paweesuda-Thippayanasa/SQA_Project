package org.geminipro.round1;
import java.time.LocalDateTime;

public class Appointment {

    private final String patientName;
    private final String doctorName;
    private final AppointmentType appointmentType;
    private final String madeByName;
    private final String clinicContactNumber;
    private final LocalDateTime dateTime;
    private final String notes;

    public enum AppointmentType {
        TOOTH_EXTRACTION,
        DEVICE_INSTALLATION,
        MONTHLY_CHECK_UP,
        DEVICE_REMOVAL
    }

    // Private constructor to enforce Builder pattern
    private Appointment(Builder builder) {
        this.patientName = builder.patientName;
        this.doctorName = builder.doctorName;
        this.appointmentType = builder.appointmentType;
        this.madeByName = builder.madeByName;
        this.clinicContactNumber = builder.clinicContactNumber;
        this.dateTime = builder.dateTime;
        this.notes = builder.notes;
    }

    // Getters
    public String getPatientName() {
        return patientName;
    }

    public String getDoctorName() {
        return doctorName;
    }

    public AppointmentType getAppointmentType() {
        return appointmentType;
    }

    public String getMadeByName() {
        return madeByName;
    }

    public String getClinicContactNumber() {
        return clinicContactNumber;
    }

    public LocalDateTime getDateTime() {
        return dateTime;
    }

    public String getNotes() {
        return notes;
    }

    // Builder class
    public static class Builder {
        // Required parameters
        private final String patientName;
        private final String doctorName;
        private final AppointmentType appointmentType;
        private final String madeByName;
        private final String clinicContactNumber;
        private final LocalDateTime dateTime;

        // Optional parameter
        private String notes;

        public Builder(String patientName, String doctorName, AppointmentType appointmentType,
                       String madeByName, String clinicContactNumber, LocalDateTime dateTime) {
            this.patientName = patientName;
            this.doctorName = doctorName;
            this.appointmentType = appointmentType;
            this.madeByName = madeByName;
            this.clinicContactNumber = clinicContactNumber;
            this.dateTime = dateTime;
        }

        public Builder notes(String notes) {
            this.notes = notes;
            return this;
        }

        public Appointment build() {
            return new Appointment(this);
        }
    }

    // Main method
    public static void main(String[] args) {
    }
}