package org.geminipro.round3;
import java.time.LocalDateTime;

public class Appointment {

    private final String patientName;
    private final String doctorName;
    private final AppointmentType appointmentType;
    private final String madeBy;
    private final String clinicContactNumber;
    private final LocalDateTime appointmentDateTime;
    private final String notes;

    private Appointment(Builder builder) {
        this.patientName = builder.patientName;
        this.doctorName = builder.doctorName;
        this.appointmentType = builder.appointmentType;
        this.madeBy = builder.madeBy;
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

    public String getMadeBy() {
        return madeBy;
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

    public enum AppointmentType {
        TOOTH_EXTRACTION,
        DEVICE_INSTALLATION,
        MONTHLY_CHECK_UP,
        DEVICE_REMOVAL
    }

    public static class Builder {
        private String patientName;
        private String doctorName;
        private AppointmentType appointmentType;
        private String madeBy;
        private String clinicContactNumber;
        private LocalDateTime appointmentDateTime;
        private String notes;

        public Builder(String patientName, String doctorName, AppointmentType appointmentType, String madeBy,
                       String clinicContactNumber, LocalDateTime appointmentDateTime) {
            this.patientName = patientName;
            this.doctorName = doctorName;
            this.appointmentType = appointmentType;
            this.madeBy = madeBy;
            this.clinicContactNumber = clinicContactNumber;
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

    // Main method
    public static void main(String[] args) {
    }
}