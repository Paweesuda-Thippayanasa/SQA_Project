package com.template.maven.example.gemini15pro.round2;
import java.time.LocalDateTime;

public abstract class Appointment {

    private String patientName;
    private String doctorName;
    private AppointmentType appointmentType;
    private String madeBy;
    private String clinicContactNumber;
    private LocalDateTime appointmentDateTime;
    private String notes;

    // Main method for demonstration
    public static void main(String[] args) {
    }

    public enum AppointmentType {
        TOOTH_EXTRACTION,
        DEVICE_INSTALLATION,
        MONTHLY_CHECK_UP,
        DEVICE_REMOVAL
    }

    // Template Method
    public final Appointment createAppointment(String patientName, String doctorName, AppointmentType appointmentType, 
                                              String madeBy, String clinicContactNumber, LocalDateTime appointmentDateTime) {
        this.patientName = patientName;
        this.doctorName = doctorName;
        this.appointmentType = appointmentType;
        this.madeBy = madeBy;
        this.clinicContactNumber = clinicContactNumber;
        this.appointmentDateTime = appointmentDateTime;
        addNotes();
        return this;
    }

    // Hook method (optional)
    protected void addNotes() {
        // Subclasses can override to add notes
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

    // Setter for notes
    public void setNotes(String notes) {
        this.notes = notes;
    }
}