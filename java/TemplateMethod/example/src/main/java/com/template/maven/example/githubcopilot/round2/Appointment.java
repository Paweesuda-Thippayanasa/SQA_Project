package com.template.maven.example.githubcopilot.round2;
//Appointment.java
import java.time.LocalDateTime;

public abstract class Appointment {
 private String patientName;
 private String doctorName;
 private AppointmentType appointmentType;
 private String personMakingAppointment;
 private String clinicContactNumber;
 private LocalDateTime appointmentDateTime;
 private String notes;


    // Main method for demonstration
    public static void main(String[] args) {
    }

 public Appointment(String patientName, String doctorName, AppointmentType appointmentType, 
                    String personMakingAppointment, String clinicContactNumber, 
                    LocalDateTime appointmentDateTime) {
     this.patientName = patientName;
     this.doctorName = doctorName;
     this.appointmentType = appointmentType;
     this.personMakingAppointment = personMakingAppointment;
     this.clinicContactNumber = clinicContactNumber;
     this.appointmentDateTime = appointmentDateTime;
     this.notes = "";
 }

 // Template method
 public final void createAppointment() {
     setRequiredFields();
     addNotes();
 }

 protected abstract void setRequiredFields();

 protected void addNotes() {
     // Optional hook method
 }

 // Getters and setters
 public String getPatientName() { return patientName; }
 public String getDoctorName() { return doctorName; }
 public AppointmentType getAppointmentType() { return appointmentType; }
 public String getPersonMakingAppointment() { return personMakingAppointment; }
 public String getClinicContactNumber() { return clinicContactNumber; }
 public LocalDateTime getAppointmentDateTime() { return appointmentDateTime; }
 public String getNotes() { return notes; }
 public void setNotes(String notes) { this.notes = notes; }
}

enum AppointmentType {
 TOOTH_EXTRACTION,
 DEVICE_INSTALLATION,
 MONTHLY_CHECKUP,
 DEVICE_REMOVAL
}

class ConcreteAppointment extends Appointment {
 public ConcreteAppointment(String patientName, String doctorName, AppointmentType appointmentType, 
                            String personMakingAppointment, String clinicContactNumber, 
                            LocalDateTime appointmentDateTime) {
     super(patientName, doctorName, appointmentType, personMakingAppointment, clinicContactNumber, appointmentDateTime);
 }

 @Override
 protected void setRequiredFields() {
     // Required fields are already set in the constructor
 }

 @Override
 protected void addNotes() {
     // Optional: Add specific notes if needed
     setNotes("Default notes from doctor to patient.");
 }
}