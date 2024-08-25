package org.copilot.round3;

import org.junit.Before;
import org.junit.Test;
import static org.junit.Assert.*;

import java.time.LocalDateTime;

public class AppointmentTest {
    private Appointment appointment;

    @Before
    public void setUp() {
        appointment = new Appointment.AppointmentBuilder("John Doe", "Dr. Smith",
                AppointmentType.DEVICE_INSTALLATION, "Jane Doe",
                "123-456-7890", LocalDateTime.of(2024, 9, 1, 14, 30))
                .setNotes("Bring previous X-rays")
                .build();
    }

    @Test
    public void testAppointmentCreation() {
        assertNotNull(appointment);
        assertEquals("John Doe", appointment.patientName);
        assertEquals("Dr. Smith", appointment.doctorName);
        assertEquals(AppointmentType.DEVICE_INSTALLATION, appointment.appointmentType);
        assertEquals("Jane Doe", appointment.appointmentMakerName);
        assertEquals("123-456-7890", appointment.clinicContactNumber);
        assertEquals(LocalDateTime.of(2024, 9, 1, 14, 30), appointment.appointmentDateTime);
        assertEquals("Bring previous X-rays", appointment.notes);
    }

    @Test
    public void testAllAppointmentTypes() {
        for (AppointmentType type : AppointmentType.values()) {
            Appointment appointment = new Appointment.AppointmentBuilder("John Doe", "Dr. Smith",
                    type, "Jane Doe", "123-456-7890", LocalDateTime.of(2024, 9, 1, 14, 30))
                    .build();
            assertEquals(type, appointment.appointmentType);
        }
    }
}