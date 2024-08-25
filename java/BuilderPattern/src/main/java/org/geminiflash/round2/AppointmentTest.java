package org.geminiflash.round2;

import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

class AppointmentTest {

    private String patientName = "John Doe";
    private String doctorName = "Dr. Smith";
    private String appointmentMakerName = "Jane Doe";
    private String clinicContactNumber = "123-456-7890";
    private LocalDateTime appointmentDateTime;

    @BeforeEach
    void setUp() {
        appointmentDateTime = LocalDateTime.of(2024, 2, 15, 10, 0);
    }

    @Test
    void testCreateAppointmentWithAllFields() {
        Appointment appointment = new Appointment.Builder(patientName, doctorName, Appointment.AppointmentType.TOOTH_EXTRACTION, appointmentMakerName, clinicContactNumber, appointmentDateTime)
                .withNotes("Please extract tooth #12").build();

        assertEquals(patientName, appointment.getPatientName());
        assertEquals(doctorName, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.TOOTH_EXTRACTION, appointment.getAppointmentType());
        assertEquals(appointmentMakerName, appointment.getAppointmentMakerName());
        assertEquals(clinicContactNumber, appointment.getClinicContactNumber());
        assertEquals(appointmentDateTime, appointment.getAppointmentDateTime());
        assertEquals("Please extract tooth #12", appointment.getNotes());
    }

    @Test
    void testCreateAppointmentWithoutNotes() {
        Appointment appointment = new Appointment.Builder(patientName, doctorName, Appointment.AppointmentType.DEVICE_INSTALLATION, appointmentMakerName, clinicContactNumber, appointmentDateTime).build();

        assertEquals(patientName, appointment.getPatientName());
        assertEquals(doctorName, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.DEVICE_INSTALLATION, appointment.getAppointmentType());
        assertEquals(appointmentMakerName, appointment.getAppointmentMakerName());
        assertEquals(clinicContactNumber, appointment.getClinicContactNumber());
        assertEquals(appointmentDateTime, appointment.getAppointmentDateTime());
        assertNull(appointment.getNotes());
    }

    @Test
    void testCreateAppointmentWithDifferentAppointmentTypes() {
        Appointment appointment1 = new Appointment.Builder(patientName, doctorName, Appointment.AppointmentType.MONTHLY_CHECK_UP, appointmentMakerName, clinicContactNumber, appointmentDateTime).build();
        Appointment appointment2 = new Appointment.Builder(patientName, doctorName, Appointment.AppointmentType.DEVICE_REMOVAL, appointmentMakerName, clinicContactNumber, appointmentDateTime).build();

        assertEquals(Appointment.AppointmentType.MONTHLY_CHECK_UP, appointment1.getAppointmentType());
        assertEquals(Appointment.AppointmentType.DEVICE_REMOVAL, appointment2.getAppointmentType());
    }
}