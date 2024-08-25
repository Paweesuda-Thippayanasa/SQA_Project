package com.template.maven.example.gemini15pro.round1;

import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

class AppointmentTest {

    @Test
    void testCreateAppointment() {
        // Arrange
        LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 3, 15, 10, 0);
        Appointment appointment = new Appointment("John Doe", "Dr. Smith", 
                Appointment.AppointmentType.MONTHLY_CHECK_UP, "Jane Doe", "123-456-7890", appointmentDateTime) {
            @Override
            protected void setRequiredFields() {
                // Implemented as required by the specific appointment type
            }
        };

        // Act
        appointment.createAppointment();

        // Assert
        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.MONTHLY_CHECK_UP, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getMadeBy());
        assertEquals("123-456-7890", appointment.getClinicContactNumber());
        assertEquals(appointmentDateTime, appointment.getAppointmentDateTime());
        assertEquals("N/A", appointment.getNotes()); // Check default notes
    }

    @Test
    void testCreateAppointmentWithNotes() {
        // Arrange
        LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 3, 15, 10, 0);
        Appointment appointment = new Appointment("John Doe", "Dr. Smith",
                Appointment.AppointmentType.DEVICE_INSTALLATION, "Jane Doe", "123-456-7890", appointmentDateTime) {
            @Override
            protected void setRequiredFields() {
                // Implemented as required by the specific appointment type
            }

            @Override
            protected void addNotes() {
                this.notes = "Patient needs to fast for 12 hours before the appointment.";
            }
        };

        // Act
        appointment.createAppointment();

        // Assert
        assertEquals("Patient needs to fast for 12 hours before the appointment.", appointment.getNotes());
    }

    @Test
    void testAllAppointmentTypes() {
        for (Appointment.AppointmentType type : Appointment.AppointmentType.values()) {
            Appointment appointment = new Appointment("John Doe", "Dr. Smith",
                    type, "Jane Doe", "123-456-7890", LocalDateTime.now()) {
                @Override
                protected void setRequiredFields() {
                    // Implemented as required by the specific appointment type
                }
            };
            assertNotNull(appointment.createAppointment());
        }
    }
}