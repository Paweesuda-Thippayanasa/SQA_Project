package com.template.maven.example.chatgpt.round1;
//File: AppointmentTest.java

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertEquals;

import java.time.LocalDateTime;

public class AppointmentTest {

 private AppointmentTemplate toothExtractionAppointment;
 private AppointmentTemplate deviceInstallationAppointment;
 private AppointmentTemplate monthlyCheckupAppointment;
 private AppointmentTemplate deviceRemovalAppointment;

 @BeforeEach
 public void setUp() {
     toothExtractionAppointment = new ToothExtractionAppointment();
     deviceInstallationAppointment = new DeviceInstallationAppointment();
     monthlyCheckupAppointment = new MonthlyCheckupAppointment();
     deviceRemovalAppointment = new DeviceRemovalAppointment();
 }

 @Test
 public void testToothExtractionAppointment() {
     LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 9, 1, 10, 0);
     toothExtractionAppointment.scheduleAppointment("John Doe", "Dr. Smith", AppointmentType.TOOTH_EXTRACTION,
             "Jane Doe", "123-456-7890", appointmentDateTime);
     assertEquals("Patient advised to avoid eating hard food before the appointment.", toothExtractionAppointment.addNotes());
 }

 @Test
 public void testDeviceInstallationAppointment() {
     LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 9, 2, 11, 0);
     deviceInstallationAppointment.scheduleAppointment("John Doe", "Dr. Smith", AppointmentType.DEVICE_INSTALLATION,
             "Jane Doe", "123-456-7890", appointmentDateTime);
     assertEquals("Patient advised to brush thoroughly before the appointment.", deviceInstallationAppointment.addNotes());
 }

 @Test
 public void testMonthlyCheckupAppointment() {
     LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 9, 3, 9, 0);
     monthlyCheckupAppointment.scheduleAppointment("John Doe", "Dr. Smith", AppointmentType.MONTHLY_CHECKUP,
             "Jane Doe", "123-456-7890", appointmentDateTime);
     assertEquals("Bring your dental hygiene kit to the appointment.", monthlyCheckupAppointment.addNotes());
 }

 @Test
 public void testDeviceRemovalAppointment() {
     LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 9, 4, 8, 0);
     deviceRemovalAppointment.scheduleAppointment("John Doe", "Dr. Smith", AppointmentType.DEVICE_REMOVAL,
             "Jane Doe", "123-456-7890", appointmentDateTime);
     assertEquals("Patient should be prepared for a retainer fitting.", deviceRemovalAppointment.addNotes());
 }
}
