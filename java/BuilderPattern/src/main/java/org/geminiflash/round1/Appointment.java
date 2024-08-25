package org.geminiflash.round1;
import java.time.LocalDateTime;
import java.util.Objects;

public class Appointment {

    private String patientName;
    private String doctorName;
    private AppointmentType appointmentType;
    private String appointmentMaker;
    private String clinicContactNumber;
    private LocalDateTime appointmentDateTime;
    private String notes;

    public enum AppointmentType {
        TOOTH_EXTRACTION, DEVICE_INSTALLATION, MONTHLY_CHECK_UP, DEVICE_REMOVAL
    }

    private Appointment(Builder builder) {
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

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Appointment that = (Appointment) o;
        return Objects.equals(patientName, that.patientName) &&
                Objects.equals(doctorName, that.doctorName) &&
                appointmentType == that.appointmentType &&
                Objects.equals(appointmentMaker, that.appointmentMaker) &&
                Objects.equals(clinicContactNumber, that.clinicContactNumber) &&
                Objects.equals(appointmentDateTime, that.appointmentDateTime) &&
                Objects.equals(notes, that.notes);
    }

    @Override
    public int hashCode() {
        return Objects.hash(patientName, doctorName, appointmentType, appointmentMaker, clinicContactNumber, appointmentDateTime, notes);
    }

    @Override
    public String toString() {
        return "Appointment{" +
                "patientName='" + patientName + '\'' +
                ", doctorName='" + doctorName + '\'' +
                ", appointmentType=" + appointmentType +
                ", appointmentMaker='" + appointmentMaker + '\'' +
                ", clinicContactNumber='" + clinicContactNumber + '\'' +
                ", appointmentDateTime=" + appointmentDateTime +
                ", notes='" + notes + '\'' +
                '}';
    }

    public static class Builder {
        private String patientName;
        private String doctorName;
        private AppointmentType appointmentType;
        private String appointmentMaker;
        private String clinicContactNumber;
        private LocalDateTime appointmentDateTime;
        private String notes;

        public Builder(String patientName, String doctorName, AppointmentType appointmentType, String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime) {
            this.patientName = patientName;
            this.doctorName = doctorName;
            this.appointmentType = appointmentType;
            this.appointmentMaker = appointmentMaker;
            this.clinicContactNumber = clinicContactNumber;
            this.appointmentDateTime = appointmentDateTime;
        }

        public Builder withNotes(String notes) {
            this.notes = notes;
            return this;
        }

        public Appointment build() {
            return new Appointment(this);
        }
    }
}