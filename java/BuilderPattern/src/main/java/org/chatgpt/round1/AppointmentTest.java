package org.chatgpt.round1;
import org.junit.jupiter.api.Assertions;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.assertEquals;
import static org.junit.jupiter.api.Assertions.assertNull;

public class AppointmentTest {
    private Appointment.AppointmentBuilder builder;

    @BeforeEach
    public void setUp() {
        builder = new Appointment.AppointmentBuilder(
                "John Doe",
                "Dr. Smith",
                AppointmentType.MONTHLY_CHECK_UP,
                "Jane Doe",
                "123-456-7890",
                LocalDateTime.of(2024, 9, 1, 10, 30)
        );
    }

    @Test
    public void testCreateAppointmentWithAllFields() {
        Appointment appointment = builder.notes("Bring previous X-rays").build();

        Assertions.assertEquals("John Doe", appointment.getPatientName());
        Assertions.assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(AppointmentType.MONTHLY_CHECK_UP, appointment.getAppointmentType());
        Assertions.assertEquals("Jane Doe", appointment.getMadeBy());
        Assertions.assertEquals("123-456-7890", appointment.getClinicContactNumber());
        Assertions.assertEquals(LocalDateTime.of(2024, 9, 1, 10, 30), appointment.getAppointmentDateTime());
        Assertions.assertEquals("Bring previous X-rays", appointment.getNotes());
    }

    @Test
    public void testCreateAppointmentWithoutNotes() {
        Appointment appointment = builder.build();

        Assertions.assertEquals("John Doe", appointment.getPatientName());
        Assertions.assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(AppointmentType.MONTHLY_CHECK_UP, appointment.getAppointmentType());
        Assertions.assertEquals("Jane Doe", appointment.getMadeBy());
        Assertions.assertEquals("123-456-7890", appointment.getClinicContactNumber());
        Assertions.assertEquals(LocalDateTime.of(2024, 9, 1, 10, 30), appointment.getAppointmentDateTime());
        Assertions.assertNull(appointment.getNotes());
    }

    @Test
    public void testCreateToothExtractionAppointment() {
        Appointment appointment = builder.appointmentType(AppointmentType.TOOTH_EXTRACTION).build();

        assertEquals(AppointmentType.TOOTH_EXTRACTION, appointment.getAppointmentType());
    }

    @Test
    public void testCreateDeviceInstallationAppointment() {
        Appointment appointment = builder.appointmentType(AppointmentType.DEVICE_INSTALLATION).build();

        assertEquals(AppointmentType.DEVICE_INSTALLATION, appointment.getAppointmentType());
    }

    @Test
    public void testCreateDeviceRemovalAppointment() {
        Appointment appointment = builder.appointmentType(AppointmentType.DEVICE_REMOVAL).build();

        assertEquals(AppointmentType.DEVICE_REMOVAL, appointment.getAppointmentType());
    }
}
