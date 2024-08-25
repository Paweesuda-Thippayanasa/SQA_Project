package com.template.maven.example.chatgpt.round1;
//File: Appointment.java

import java.time.LocalDateTime;

enum AppointmentType {
 TOOTH_EXTRACTION,
 DEVICE_INSTALLATION,
 MONTHLY_CHECKUP,
 DEVICE_REMOVAL
}

abstract class AppointmentTemplate {
 protected String patientName;
 protected String doctorName;
 protected AppointmentType appointmentType;
 protected String appointmentMaker;
 protected String clinicContactNumber;
 protected LocalDateTime appointmentDateTime;
 protected String notes;

 public final void scheduleAppointment(String patientName, String doctorName, AppointmentType appointmentType,
                                       String appointmentMaker, String clinicContactNumber, LocalDateTime appointmentDateTime) {
     this.patientName = patientName;
     this.doctorName = doctorName;
     this.appointmentType = appointmentType;
     this.appointmentMaker = appointmentMaker;
     this.clinicContactNumber = clinicContactNumber;
     this.appointmentDateTime = appointmentDateTime;
     this.notes = addNotes();
 }

 // Hook method that can be overridden by subclasses to add specific notes.
 protected String addNotes() {
     return "No additional notes.";
 }

 @Override
 public String toString() {
     return "Appointment Details:\n" +
             "Patient: " + patientName + "\n" +
             "Doctor: " + doctorName + "\n" +
             "Type: " + appointmentType + "\n" +
             "Scheduled by: " + appointmentMaker + "\n" +
             "Clinic Contact: " + clinicContactNumber + "\n" +
             "Date and Time: " + appointmentDateTime + "\n" +
             "Notes: " + notes;
 }
}

class ToothExtractionAppointment extends AppointmentTemplate {
 @Override
 protected String addNotes() {
     return "Patient advised to avoid eating hard food before the appointment.";
 }
}

class DeviceInstallationAppointment extends AppointmentTemplate {
 @Override
 protected String addNotes() {
     return "Patient advised to brush thoroughly before the appointment.";
 }
}

class MonthlyCheckupAppointment extends AppointmentTemplate {
 @Override
 protected String addNotes() {
     return "Bring your dental hygiene kit to the appointment.";
 }
}

class DeviceRemovalAppointment extends AppointmentTemplate {
 @Override
 protected String addNotes() {
     return "Patient should be prepared for a retainer fitting.";
 }
}
