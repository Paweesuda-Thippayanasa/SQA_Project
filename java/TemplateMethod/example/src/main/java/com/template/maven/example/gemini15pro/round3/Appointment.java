package com.template.maven.example.gemini15pro.round3;
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

    public Appointment(String patientName, String doctorName, AppointmentType appointmentType, String madeBy, String clinicContactNumber, LocalDateTime appointmentDateTime) {
        this.patientName = patientName;
        this.doctorName = doctorName;
        this.appointmentType = appointmentType;
        this.madeBy = madeBy;
        this.clinicContactNumber = clinicContactNumber;
        this.appointmentDateTime = appointmentDateTime;
    }

    public final Appointment createAppointment() {
        setPatientName();
        setDoctorName();
        setAppointmentType();
        setMadeBy();
        setClinicContactNumber();
        setAppointmentDateTime();
        addNotes();
        return this;
    }

    // Abstract methods to be implemented by concrete classes
    protected abstract void setPatientName();
    protected abstract void setDoctorName();
    protected abstract void setAppointmentType();
    protected abstract void setMadeBy();
    protected abstract void setClinicContactNumber();
    protected abstract void setAppointmentDateTime();

    // Hook method (optional)
    protected void addNotes() {
        // Optionally add notes to the appointment.
    }

    // Getters for all fields
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

    public void setNotes(String notes) {
        this.notes = notes;
    }
}

enum AppointmentType {
    TOOTH_EXTRACTION,
    DEVICE_INSTALLATION,
    MONTHLY_CHECK_UP,
    DEVICE_REMOVAL
}