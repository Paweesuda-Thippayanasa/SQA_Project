package org.copilot.round2;

import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

class AppointmentTest {

    @Test
    void testAppointmentCreation() {
        LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 1, 15, 10, 0);
        Appointment appointment = new Appointment.AppointmentBuilder("John Doe", "Dr. Smith", Appointment.AppointmentType.MONTHLY_CHECKUP, "Jane Doe", "123-456-7890", appointmentDateTime)
                .withNotes("Check teeth cleaning")
                .build();

        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.MONTHLY_CHECKUP, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getAppointmentMaker());
        assertEquals("123-456-7890", appointment.getClinicContactNumber());
        assertEquals(appointmentDateTime, appointment.getAppointmentDateTime());
        assertEquals("Check teeth cleaning", appointment.getNotes());
    }

    @Test
    void testAppointmentCreationWithoutNotes() {
        LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 1, 15, 10, 0);
        Appointment appointment = new Appointment.AppointmentBuilder("John Doe", "Dr. Smith", Appointment.AppointmentType.DEVICE_REMOVAL, "Jane Doe", "123-456-7890", appointmentDateTime)
                .build();

        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.DEVICE_REMOVAL, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getAppointmentMaker());
        assertEquals("123-456-7890", appointment.getClinicContactNumber());
        assertEquals(appointmentDateTime, appointment.getAppointmentDateTime());
        assertNull(appointment.getNotes());
    }

    @Test
    void testAllAppointmentTypes() {
        LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 1, 15, 10, 0);

        Appointment appointment1 = new Appointment.AppointmentBuilder("John Doe", "Dr. Smith", Appointment.AppointmentType.TOOTH_EXTRACTION, "Jane Doe", "123-456-7890", appointmentDateTime).build();
        Appointment appointment2 = new Appointment.AppointmentBuilder("John Doe", "Dr. Smith", Appointment.AppointmentType.DEVICE_INSTALLATION, "Jane Doe", "123-456-7890", appointmentDateTime).build();
        Appointment appointment3 = new Appointment.AppointmentBuilder("John Doe", "Dr. Smith", Appointment.AppointmentType.MONTHLY_CHECKUP, "Jane Doe", "123-456-7890", appointmentDateTime).build();
        Appointment appointment4 = new Appointment.AppointmentBuilder("John Doe", "Dr. Smith", Appointment.AppointmentType.DEVICE_REMOVAL, "Jane Doe", "123-456-7890", appointmentDateTime).build();

        assertEquals(Appointment.AppointmentType.TOOTH_EXTRACTION, appointment1.getAppointmentType());
        assertEquals(Appointment.AppointmentType.DEVICE_INSTALLATION, appointment2.getAppointmentType());
        assertEquals(Appointment.AppointmentType.MONTHLY_CHECKUP, appointment3.getAppointmentType());
        assertEquals(Appointment.AppointmentType.DEVICE_REMOVAL, appointment4.getAppointmentType());
    }
}