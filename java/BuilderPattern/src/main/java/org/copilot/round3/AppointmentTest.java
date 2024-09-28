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
        assertNotNull(appointment); //change all of this to get
        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(AppointmentType.DEVICE_INSTALLATION, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getAppointmentMakerName());
        assertEquals("123-456-7890", appointment.getClinicContactNumber());
        assertEquals(LocalDateTime.of(2024, 9, 1, 14, 30), appointment.getAppointmentDateTime());
        assertEquals("Bring previous X-rays", appointment.getNotes());
    }

    @Test
    public void testAllAppointmentTypes() {
        for (AppointmentType type : AppointmentType.values()) {
            Appointment appointment = new Appointment.AppointmentBuilder("John Doe", "Dr. Smith",
                    type, "Jane Doe", "123-456-7890", LocalDateTime.of(2024, 9, 1, 14, 30))
                    .build();
            assertEquals(type, appointment.getAppointmentType());
        }
    }
}
