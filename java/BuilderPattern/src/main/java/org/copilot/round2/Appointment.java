package org.copilot.round2;

import java.time.LocalDateTime;

public class Appointment {
    private String patientName;
    private String doctorName;
    private AppointmentType appointmentType;
    private String appointmentMakerName;
    private String clinicContactNumber;
    private LocalDateTime appointmentDateTime;
    private String notes;

    // Private constructor to enforce use of the Builder
    private Appointment(AppointmentBuilder builder) {
        this.patientName = builder.patientName;
        this.doctorName = builder.doctorName;
        this.appointmentType = builder.appointmentType;
        this.appointmentMakerName = builder.appointmentMakerName;
        this.clinicContactNumber = builder.clinicContactNumber;
        this.appointmentDateTime = builder.appointmentDateTime;
        this.notes = builder.notes;
    }

    // Static builder class
    public static class AppointmentBuilder {
        private final String patientName;
        private final String doctorName;
        private final AppointmentType appointmentType;
        private final String appointmentMakerName;
        private final String clinicContactNumber;
        private final LocalDateTime appointmentDateTime;
        private String notes;

        public AppointmentBuilder(String patientName, String doctorName, AppointmentType appointmentType,
                                  String appointmentMakerName, String clinicContactNumber, LocalDateTime appointmentDateTime) {
            this.patientName = patientName;
            this.doctorName = doctorName;
            this.appointmentType = appointmentType;
            this.appointmentMakerName = appointmentMakerName;
            this.clinicContactNumber = clinicContactNumber;
            this.appointmentDateTime = appointmentDateTime;
        }

        public AppointmentBuilder setNotes(String notes) {
            this.notes = notes;
            return this;
        }

        public Appointment build() {
            return new Appointment(this);
        }
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

    public String getAppointmentMakerName() {
        return appointmentMakerName;
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

    // Setters
    public void setPatientName(String patientName) {
        this.patientName = patientName;
    }

    public void setDoctorName(String doctorName) {
        this.doctorName = doctorName;
    }

    public void setAppointmentType(AppointmentType appointmentType) {
        this.appointmentType = appointmentType;
    }

    public void setAppointmentMakerName(String appointmentMakerName) {
        this.appointmentMakerName = appointmentMakerName;
    }

    public void setClinicContactNumber(String clinicContactNumber) {
        this.clinicContactNumber = clinicContactNumber;
    }

    public void setAppointmentDateTime(LocalDateTime appointmentDateTime) {
        this.appointmentDateTime = appointmentDateTime;
    }

    public void setNotes(String notes) {
        this.notes = notes;
    }

    // Main method
    public static void main(String[] args) {
    }

    // Enum for appointment types
    public enum AppointmentType {
        TOOTH_EXTRACTION,
        DEVICE_INSTALLATION,
        MONTHLY_CHECKUP,
        DEVICE_REMOVAL
    }
}
