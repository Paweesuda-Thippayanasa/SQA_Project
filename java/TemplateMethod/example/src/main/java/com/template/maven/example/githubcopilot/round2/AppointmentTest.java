package com.template.maven.example.githubcopilot.round2;
import static org.junit.jupiter.api.Assertions.*;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.time.LocalDateTime;

public class AppointmentTest {
    private ConcreteAppointment appointment;

    @BeforeEach
    public void setUp() {
        appointment = new ConcreteAppointment("John Doe", "Dr. Smith", AppointmentType.TOOTH_EXTRACTION, 
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
        assertEquals("Default notes from doctor to patient.", appointment.getNotes());
    }

    @Test
    public void testAppointmentTypes() {
        for (AppointmentType type : AppointmentType.values()) {
            ConcreteAppointment appointment = new ConcreteAppointment("John Doe", "Dr. Smith", type, 
                                                                       "Jane Doe", "123-456-7890", 
                                                                       LocalDateTime.of(2023, 10, 10, 10, 0));
            appointment.createAppointment();
            assertEquals(type, appointment.getAppointmentType());
        }
    }
}