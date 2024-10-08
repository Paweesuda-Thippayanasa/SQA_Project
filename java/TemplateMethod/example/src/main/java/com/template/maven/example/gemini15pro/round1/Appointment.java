package com.template.maven.example.gemini15pro.round1;

import java.time.LocalDateTime;

public abstract class Appointment {

    private String patientName;
    private String doctorName;
    private AppointmentType appointmentType;
    private String madeBy;
    private String clinicContactNumber;
    private LocalDateTime appointmentDateTime;
    protected String notes;

    // Main method for demonstration
    public static void main(String[] args) {
    }

    public Appointment(String patientName, String doctorName, AppointmentType appointmentType, String madeBy, String clinicContactNumber, LocalDateTime appointmentDateTime) {
        this.patientName = patientName;
        this.doctorName = doctorName;
        this.appointmentType = appointmentType;
        this.madeBy = madeBy;
        this.clinicContactNumber = clinicContactNumber;
        this.appointmentDateTime = appointmentDateTime;
    }

    // Template Method
    public final Appointment createAppointment() {
        setRequiredFields();
        addNotes();
        return this;
    }

    // Abstract method to be implemented by subclasses
    protected abstract void setRequiredFields();

    // Hook method (optional implementation)
    protected void addNotes() {
        // Optional: Add notes to the appointment
        this.notes = "N/A";
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


    // Enum for appointment types
    public enum AppointmentType {
        TOOTH_EXTRACTION,
        DEVICE_INSTALLATION,
        MONTHLY_CHECK_UP,
        DEVICE_REMOVAL
    }
}