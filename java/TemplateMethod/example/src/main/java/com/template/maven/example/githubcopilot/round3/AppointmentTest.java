package com.template.maven.example.githubcopilot.round3;
//AppointmentTest.java

import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.time.LocalDateTime;

public class AppointmentTest {
    private OrthodonticAppointment appointment;

    @BeforeEach
    public void setUp() {
        appointment = new OrthodonticAppointment("John Doe", "Dr. Smith", AppointmentType.TOOTH_EXTRACTION, 
                                                 "Jane Doe", "123-456-7890", LocalDateTime.of(2023, 10, 10, 10, 0));
    }

    @Test
    public void testCreateAppointment() {
        appointment.createAppointment();
        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(AppointmentType.TOOTH_EXTRACTION, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getPersonMakingAppointment());
        assertEquals("123-456-7890", appointment.getClinicContactNumber());
        assertEquals(LocalDateTime.of(2023, 10, 10, 10, 0), appointment.getAppointmentDateTime());
        assertEquals("", appointment.getNotes());
    }

    @Test
    public void testAddNotes() {
        appointment.setNotes("Bring previous medical records.");
        assertEquals("Bring previous medical records.", appointment.getNotes());
    }

    @Test
    public void testAllAppointmentTypes() {
        for (AppointmentType type : AppointmentType.values()) {
            OrthodonticAppointment testAppointment = new OrthodonticAppointment("John Doe", "Dr. Smith", type, 
                                                                                "Jane Doe", "123-456-7890", 
                                                                                LocalDateTime.of(2023, 10, 10, 10, 0));
            testAppointment.createAppointment();
            assertEquals(type, testAppointment.getAppointmentType());
        }
    }
}