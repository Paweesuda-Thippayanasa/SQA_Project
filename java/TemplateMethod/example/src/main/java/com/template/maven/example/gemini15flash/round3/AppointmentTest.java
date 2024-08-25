package com.template.maven.example.gemini15flash.round3;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;
import java.time.LocalDateTime;

public class AppointmentTest {

    @Test
    void testCreateAppointmentWithAllFields() {
        Appointment appointment = new Appointment()
                .createAppointment("John Doe", "Dr. Smith", Appointment.AppointmentType.TOOTH_EXTRACTION,
                        "Jane Doe", "123-456-7890", LocalDateTime.now());

        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.TOOTH_EXTRACTION, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getAppointmentMakerName());
        assertEquals("123-456-7890", appointment.getClinicContactNumber());
        assertNotNull(appointment.getAppointmentDateTime());
    }

    @Test
    void testCreateAppointmentWithNotes() {
        Appointment appointment = new Appointment()
                .createAppointment("John Doe", "Dr. Smith", Appointment.AppointmentType.DEVICE_INSTALLATION,
                        "Jane Doe", "123-456-7890", LocalDateTime.now());

        // Add notes directly to the object
        appointment.addNotes("Please bring X-rays.");

        assertEquals("Please bring X-rays.", appointment.getNotes());
    }

    @Test
    void testCreateAppointmentAllTypes() {
        Appointment appointment1 = new Appointment()
                .createAppointment("John Doe", "Dr. Smith", Appointment.AppointmentType.TOOTH_EXTRACTION,
                        "Jane Doe", "123-456-7890", LocalDateTime.now());
        Appointment appointment2 = new Appointment()
                .createAppointment("John Doe", "Dr. Smith", Appointment.AppointmentType.DEVICE_INSTALLATION,
                        "Jane Doe", "123-456-7890", LocalDateTime.now());
        Appointment appointment3 = new Appointment()
                .createAppointment("John Doe", "Dr. Smith", Appointment.AppointmentType.MONTHLY_CHECK_UP,
                        "Jane Doe", "123-456-7890", LocalDateTime.now());
        Appointment appointment4 = new Appointment()
                .createAppointment("John Doe", "Dr. Smith", Appointment.AppointmentType.DEVICE_REMOVAL,
                        "Jane Doe", "123-456-7890", LocalDateTime.now());

        assertEquals(Appointment.AppointmentType.TOOTH_EXTRACTION, appointment1.getAppointmentType());
        assertEquals(Appointment.AppointmentType.DEVICE_INSTALLATION, appointment2.getAppointmentType());
        assertEquals(Appointment.AppointmentType.MONTHLY_CHECK_UP, appointment3.getAppointmentType());
        assertEquals(Appointment.AppointmentType.DEVICE_REMOVAL, appointment4.getAppointmentType());
    }
}