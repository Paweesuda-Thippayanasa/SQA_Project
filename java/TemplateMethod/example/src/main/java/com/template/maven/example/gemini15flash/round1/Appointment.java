package com.template.maven.example.gemini15flash.round1;
//File: Appointment.java
import java.time.LocalDateTime;
import java.util.Objects;

public abstract class Appointment {

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

    public Appointment(String patientName, String doctorName, AppointmentType appointmentType,
                       String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime) {
        this.patientName = patientName;
        this.doctorName = doctorName;
        this.appointmentType = appointmentType;
        this.appointmentMaker = appointmentMaker;
        this.clinicContactNumber = clinicContactNumber;
        this.appointmentDateTime = appointmentDateTime;
    }

    public final void createAppointment() {
        setRequiredFields();
        addOptionalNotes();
    }

    protected abstract void setRequiredFields();

    protected void addOptionalNotes() {
        // This method can be overridden to add notes specific to the appointment type.
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

    public void setNotes(String notes) {
        this.notes = notes;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Appointment that = (Appointment) o;
        return Objects.equals(patientName, that.patientName) && Objects.equals(doctorName, that.doctorName) &&
                appointmentType == that.appointmentType && Objects.equals(appointmentMaker, that.appointmentMaker) &&
                Objects.equals(clinicContactNumber, that.clinicContactNumber) &&
                Objects.equals(appointmentDateTime, that.appointmentDateTime) && Objects.equals(notes, that.notes);
    }

    @Override
    public int hashCode() {
        return Objects.hash(patientName, doctorName, appointmentType, appointmentMaker, clinicContactNumber,
                appointmentDateTime, notes);
    }

    // Subclasses for specific appointment types

    public static class ToothExtractionAppointment extends Appointment {

        public ToothExtractionAppointment(String patientName, String doctorName, AppointmentType appointmentType,
                                          String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime) {
            super(patientName, doctorName, appointmentType, appointmentMaker, clinicContactNumber, appointmentDateTime);
        }

        @Override
        protected void setRequiredFields() {
            // No additional required fields for Tooth Extraction appointments.
        }

        @Override
        protected void addOptionalNotes() {
            setNotes("Please bring a list of your current medications.");
        }
    }

    public static class DeviceInstallationAppointment extends Appointment {

        public DeviceInstallationAppointment(String patientName, String doctorName, AppointmentType appointmentType,
                                            String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime) {
            super(patientName, doctorName, appointmentType, appointmentMaker, clinicContactNumber, appointmentDateTime);
        }

        @Override
        protected void setRequiredFields() {
            // No additional required fields for Device Installation appointments.
        }

        @Override
        protected void addOptionalNotes() {
            setNotes("Please bring your insurance card and ID.");
        }
    }

    public static class MonthlyCheckUpAppointment extends Appointment {

        public MonthlyCheckUpAppointment(String patientName, String doctorName, AppointmentType appointmentType,
                                          String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime) {
            super(patientName, doctorName, appointmentType, appointmentMaker, clinicContactNumber, appointmentDateTime);
        }

        @Override
        protected void setRequiredFields() {
            // No additional required fields for Monthly Check-Up appointments.
        }

        @Override
        protected void addOptionalNotes() {
            setNotes("Please bring your previous X-rays.");
        }
    }

    public static class DeviceRemovalAppointment extends Appointment {

        public DeviceRemovalAppointment(String patientName, String doctorName, AppointmentType appointmentType,
                                        String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime) {
            super(patientName, doctorName, appointmentType, appointmentMaker, clinicContactNumber, appointmentDateTime);
        }

        @Override
        protected void setRequiredFields() {
            // No additional required fields for Device Removal appointments.
        }

        @Override
        protected void addOptionalNotes() {
            setNotes("Please bring your device removal form.");
        }
    }
}