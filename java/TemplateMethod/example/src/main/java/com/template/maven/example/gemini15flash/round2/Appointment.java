package com.template.maven.example.gemini15flash.round2;
//File: Appointment.java
import java.time.LocalDateTime;

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
        // Optionally add notes
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

    // Additional functions for scheduling logic:
    public static void scheduleAppointment(Appointment appointment) {
        // Implement scheduling logic here
        System.out.println("Appointment scheduled successfully!");
    }

    public static void cancelAppointment(Appointment appointment) {
        // Implement cancellation logic here
        System.out.println("Appointment canceled successfully!");
    }
}

class AppointmentWithNotes extends Appointment {
    private String notes;

    public AppointmentWithNotes(String patientName, String doctorName, AppointmentType appointmentType,
                               String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime,
                               String notes) {
        super(patientName, doctorName, appointmentType, appointmentMaker, clinicContactNumber, appointmentDateTime);
        this.notes = notes;
    }

    @Override
    protected void setRequiredFields() {
        // No additional fields required
    }

    @Override
    protected void addOptionalNotes() {
        this.setNotes(notes);
    }
}

class AppointmentWithoutNotes extends Appointment {

    public AppointmentWithoutNotes(String patientName, String doctorName, AppointmentType appointmentType,
                                 String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime) {
        super(patientName, doctorName, appointmentType, appointmentMaker, clinicContactNumber, appointmentDateTime);
    }

    @Override
    protected void setRequiredFields() {
        // No additional fields required
    }
}