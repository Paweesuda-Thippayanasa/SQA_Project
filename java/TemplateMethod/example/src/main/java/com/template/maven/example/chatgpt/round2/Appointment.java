package com.template.maven.example.chatgpt.round2;
//Appointment.java
import java.time.LocalDateTime;

public abstract class Appointment {
 private String patientName;
 private String doctorName;
 private AppointmentType appointmentType;
 private String bookedBy;
 private String clinicContactNumber;
 private LocalDateTime appointmentDateTime;
 private String notes;

    // Main method for demonstration
    public static void main(String[] args) {
    }

 // Template Method
 public final void createAppointment() {
     setPatientName();
     setDoctorName();
     setAppointmentType();
     setBookedBy();
     setClinicContactNumber();
     setAppointmentDateTime();
     if (notes != null) {
         setNotes(notes);
     }
 }

 // Abstract methods to be implemented by subclasses
 protected abstract void setPatientName();
 protected abstract void setDoctorName();
 protected abstract void setAppointmentType();
 protected abstract void setBookedBy();
 protected abstract void setClinicContactNumber();
 protected abstract void setAppointmentDateTime();

 // Concrete method for setting optional notes
 protected void setNotes(String notes) {
     this.notes = notes;
 }

 // Getters and setters for fields
 public String getPatientName() { return patientName; }
 public void setPatientName(String patientName) { this.patientName = patientName; }

 public String getDoctorName() { return doctorName; }
 public void setDoctorName(String doctorName) { this.doctorName = doctorName; }

 public AppointmentType getAppointmentType() { return appointmentType; }
 public void setAppointmentType(AppointmentType appointmentType) { this.appointmentType = appointmentType; }

 public String getBookedBy() { return bookedBy; }
 public void setBookedBy(String bookedBy) { this.bookedBy = bookedBy; }

 public String getClinicContactNumber() { return clinicContactNumber; }
 public void setClinicContactNumber(String clinicContactNumber) { this.clinicContactNumber = clinicContactNumber; }

 public LocalDateTime getAppointmentDateTime() { return appointmentDateTime; }
 public void setAppointmentDateTime(LocalDateTime appointmentDateTime) { this.appointmentDateTime = appointmentDateTime; }

 public String getNotes() { return notes; }
}

//Concrete class implementation
class OrthodonticAppointment extends Appointment {
 public OrthodonticAppointment(String patientName, String doctorName, AppointmentType appointmentType, String bookedBy, String clinicContactNumber, LocalDateTime appointmentDateTime, String notes) {
     setPatientName(patientName);
     setDoctorName(doctorName);
     setAppointmentType(appointmentType);
     setBookedBy(bookedBy);
     setClinicContactNumber(clinicContactNumber);
     setAppointmentDateTime(appointmentDateTime);
     if (notes != null) {
         setNotes(notes);
     }
 }

 @Override
 protected void setPatientName() {
     // Additional logic, if needed
 }

 @Override
 protected void setDoctorName() {
     // Additional logic, if needed
 }

 @Override
 protected void setAppointmentType() {
     // Additional logic, if needed
 }

 @Override
 protected void setBookedBy() {
     // Additional logic, if needed
 }

 @Override
 protected void setClinicContactNumber() {
     // Additional logic, if needed
 }

 @Override
 protected void setAppointmentDateTime() {
     // Additional logic, if needed
 }
}

//Enum for Appointment Types
enum AppointmentType {
 TOOTH_EXTRACTION,
 DEVICE_INSTALLATION,
 MONTHLY_CHECKUP,
 DEVICE_REMOVAL
}
