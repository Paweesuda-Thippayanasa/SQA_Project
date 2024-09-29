package com.template.maven.example.gemini15flash.round3;
//File: Appointment.java
import java.time.LocalDateTime;

public class Appointment {

    private String patientName;
    private String doctorName;
    private AppointmentType appointmentType;
    private String appointmentMakerName;
    private String clinicContactNumber;
    private LocalDateTime appointmentDateTime;
    private String notes;

    // Main method for demonstration
    public static void main(String[] args) {
    }

    public enum AppointmentType {
        TOOTH_EXTRACTION, DEVICE_INSTALLATION, MONTHLY_CHECK_UP, DEVICE_REMOVAL
    }

    // Template Method
    public Appointment createAppointment(String patientName, String doctorName,
                                      AppointmentType appointmentType,
                                      String appointmentMakerName,
                                      String clinicContactNumber,
                                      LocalDateTime appointmentDateTime) {
        this.patientName = patientName;
        this.doctorName = doctorName;
        this.appointmentType = appointmentType;
        this.appointmentMakerName = appointmentMakerName;
        this.clinicContactNumber = clinicContactNumber;
        this.appointmentDateTime = appointmentDateTime;

        return this;
    }

    // Hook Method - Optional
    public void addNotes(String notes) {
        this.notes = notes;
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
}