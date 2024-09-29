package org.geminiflash.round3;
import java.time.LocalDateTime;

public class Appointment {
    private String patientName;
    private String doctorName;
    private AppointmentType appointmentType;
    private String appointmentMaker;
    private String clinicContactNumber;
    private LocalDateTime appointmentDateTime;
    private String notes;

    public enum AppointmentType {
        TOOTH_EXTRACTION,
        DEVICE_INSTALLATION,
        MONTHLY_CHECKUP,
        DEVICE_REMOVAL
    }

    private Appointment(AppointmentBuilder builder) {
        this.patientName = builder.patientName;
        this.doctorName = builder.doctorName;
        this.appointmentType = builder.appointmentType;
        this.appointmentMaker = builder.appointmentMaker;
        this.clinicContactNumber = builder.clinicContactNumber;
        this.appointmentDateTime = builder.appointmentDateTime;
        this.notes = builder.notes;
    }

    public String getPatientName() {
        return patientName;
    }

    public String getDoctorName() {
        return doctorName;
    }

    public AppointmentType getAppointmentType() {
        return appointmentType;
    }

    public String getAppointmentMaker() {
        return appointmentMaker;
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

    public static class AppointmentBuilder {
        private String patientName;
        private String doctorName;
        private AppointmentType appointmentType;
        private String appointmentMaker;
        private String clinicContactNumber;
        private LocalDateTime appointmentDateTime;
        private String notes;

        public AppointmentBuilder(String patientName, String doctorName, AppointmentType appointmentType, String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime) {
            this.patientName = patientName;
            this.doctorName = doctorName;
            this.appointmentType = appointmentType;
            this.appointmentMaker = appointmentMaker;
            this.clinicContactNumber = clinicContactNumber;
            this.appointmentDateTime = appointmentDateTime;
        }

        public AppointmentBuilder withNotes(String notes) {
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