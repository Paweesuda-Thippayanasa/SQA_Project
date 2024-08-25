package com.template.maven.example.chatgpt.round2;

//AppointmentTest.java
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AppointmentTest {
 private OrthodonticAppointment appointment;

 @BeforeEach
 public void setUp() {
     appointment = new OrthodonticAppointment(
             "John Doe",
             "Dr. Smith",
             AppointmentType.TOOTH_EXTRACTION,
             "Jane Doe",
             "123-456-7890",
             LocalDateTime.of(2024, 9, 1, 10, 0),
             "No notes"
     );
     appointment.createAppointment();
 }

 @Test
 public void testAppointmentCreation() {
     assertEquals("John Doe", appointment.getPatientName());
     assertEquals("Dr. Smith", appointment.getDoctorName());
     assertEquals(AppointmentType.TOOTH_EXTRACTION, appointment.getAppointmentType());
     assertEquals("Jane Doe", appointment.getBookedBy());
     assertEquals("123-456-7890", appointment.getClinicContactNumber());
     assertEquals(LocalDateTime.of(2024, 9, 1, 10, 0), appointment.getAppointmentDateTime());
     assertEquals("No notes", appointment.getNotes());
 }

 @Test
 public void testDifferentAppointmentTypes() {
     OrthodonticAppointment extractionAppointment = new OrthodonticAppointment(
             "John Doe",
             "Dr. Smith",
             AppointmentType.TOOTH_EXTRACTION,
             "Jane Doe",
             "123-456-7890",
             LocalDateTime.of(2024, 9, 1, 10, 0),
             "No notes"
     );
     OrthodonticAppointment installationAppointment = new OrthodonticAppointment(
             "John Doe",
             "Dr. Smith",
             AppointmentType.DEVICE_INSTALLATION,
             "Jane Doe",
             "123-456-7890",
             LocalDateTime.of(2024, 9, 2, 10, 0),
             "No notes"
     );
     OrthodonticAppointment checkupAppointment = new OrthodonticAppointment(
             "John Doe",
             "Dr. Smith",
             AppointmentType.MONTHLY_CHECKUP,
             "Jane Doe",
             "123-456-7890",
             LocalDateTime.of(2024, 9, 3, 10, 0),
             "No notes"
     );
     OrthodonticAppointment removalAppointment = new OrthodonticAppointment(
             "John Doe",
             "Dr. Smith",
             AppointmentType.DEVICE_REMOVAL,
             "Jane Doe",
             "123-456-7890",
             LocalDateTime.of(2024, 9, 4, 10, 0),
             "No notes"
     );

     assertEquals(AppointmentType.TOOTH_EXTRACTION, extractionAppointment.getAppointmentType());
     assertEquals(AppointmentType.DEVICE_INSTALLATION, installationAppointment.getAppointmentType());
     assertEquals(AppointmentType.MONTHLY_CHECKUP, checkupAppointment.getAppointmentType());
     assertEquals(AppointmentType.DEVICE_REMOVAL, removalAppointment.getAppointmentType());
 }
}
