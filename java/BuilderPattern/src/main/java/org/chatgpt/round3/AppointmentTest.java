package org.chatgpt.round3;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

class AppointmentTest {

    private Appointment.Builder builder;

    @BeforeEach
    void setUp() {
        builder = new Appointment.Builder(
                "John Doe",
                "Dr. Smith",
                AppointmentType.DEVICE_INSTALLATION,
                "Jane Doe",
                "123-456-7890",
                LocalDateTime.of(2024, 9, 1, 10, 0)
        );
    }

    @Test
    void testAppointmentCreation() {
        Appointment appointment = builder.build();

        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(AppointmentType.DEVICE_INSTALLATION, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getBookedBy());
        assertEquals("123-456-7890", appointment.getClinicContact());
        assertEquals(LocalDateTime.of(2024, 9, 1, 10, 0), appointment.getAppointmentDateTime());
        assertNull(appointment.getNotes());
    }

    @Test
    void testAppointmentCreationWithNotes() {
        Appointment appointment = builder.notes("Bring previous X-rays").build();

        assertEquals("Bring previous X-rays", appointment.getNotes());
    }

    @Test
    void testAllAppointmentTypes() {
        for (AppointmentType type : AppointmentType.values()) {
            Appointment appointment = new Appointment.Builder(
                    "John Doe",
                    "Dr. Smith",
                    type,
                    "Jane Doe",
                    "123-456-7890",
                    LocalDateTime.of(2024, 9, 1, 10, 0)
            ).build();
            assertEquals(type, appointment.getAppointmentType());
        }
    }
}