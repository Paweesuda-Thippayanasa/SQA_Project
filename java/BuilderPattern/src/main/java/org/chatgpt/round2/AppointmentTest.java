package org.chatgpt.round2;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import java.time.LocalDateTime;
import static org.junit.jupiter.api.Assertions.*;

class AppointmentTest {
    private Appointment appointment;

    @BeforeEach
    void setUp() {
        // Setup a default appointment for testing
        appointment = new Appointment.Builder(
                "John Doe",
                "Dr. Smith",
                AppointmentType.TOOTH_EXTRACTION,
                "Jane Doe",
                "123-456-7890",
                LocalDateTime.of(2024, 9, 15, 14, 30)
        ).notes("Patient has a history of hypertension").build();
    }

    @Test
    void testAppointmentCreation() {
        assertNotNull(appointment);
        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(AppointmentType.TOOTH_EXTRACTION, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getBookedBy());
        assertEquals("123-456-7890", appointment.getClinicContactNumber());
        assertEquals(LocalDateTime.of(2024, 9, 15, 14, 30), appointment.getAppointmentDateTime());
        assertEquals("Patient has a history of hypertension", appointment.getNotes());
    }

    @Test
    void testAppointmentWithoutNotes() {
        Appointment appointmentWithoutNotes = new Appointment.Builder(
                "Jane Roe",
                "Dr. Jones",
                AppointmentType.DEVICE_INSTALLATION,
                "Mark Roe",
                "098-765-4321",
                LocalDateTime.of(2024, 10, 20, 10, 0)
        ).build();

        assertNotNull(appointmentWithoutNotes);
        assertNull(appointmentWithoutNotes.getNotes());
    }

    @Test
    void testAllAppointmentTypes() {
        AppointmentType[] types = AppointmentType.values();

        for (AppointmentType type : types) {
            Appointment appointment = new Appointment.Builder(
                    "Test Patient",
                    "Test Doctor",
                    type,
                    "Test Booker",
                    "123-456-7890",
                    LocalDateTime.of(2024, 8, 25, 9, 0)
            ).build();

            assertNotNull(appointment);
            assertEquals(type, appointment.getAppointmentType());
        }
    }
}