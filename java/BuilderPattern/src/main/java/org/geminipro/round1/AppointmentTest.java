package org.geminipro.round1;

import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

class AppointmentTest {

    @Test
    void testAppointmentCreation() {
        LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 3, 12, 10, 0);
        Appointment appointment = new Appointment.Builder("John Doe", "Dr. Smith",
                Appointment.AppointmentType.DEVICE_INSTALLATION, "Jane Doe", "123-456-7890", appointmentDateTime)
                .notes("Bring previous X-rays")
                .build();

        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.DEVICE_INSTALLATION, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getMadeByName());
        assertEquals("123-456-7890", appointment.getClinicContactNumber());
        assertEquals(appointmentDateTime, appointment.getDateTime());
        assertEquals("Bring previous X-rays", appointment.getNotes());
    }

    @Test
    void testAppointmentCreationWithoutNotes() {
        LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 3, 12, 10, 0);
        Appointment appointment = new Appointment.Builder("John Doe", "Dr. Smith",
                Appointment.AppointmentType.DEVICE_INSTALLATION, "Jane Doe", "123-456-7890", appointmentDateTime)
                .build();

        assertNull(appointment.getNotes());
    }

    @Test
    void testAllAppointmentTypes() {
        LocalDateTime appointmentDateTime = LocalDateTime.of(2024, 3, 12, 10, 0);

        for (Appointment.AppointmentType type : Appointment.AppointmentType.values()) {
            Appointment appointment = new Appointment.Builder("John Doe", "Dr. Smith",
                    type, "Jane Doe", "123-456-7890", appointmentDateTime)
                    .build();

            assertEquals(type, appointment.getAppointmentType());
        }
    }
}