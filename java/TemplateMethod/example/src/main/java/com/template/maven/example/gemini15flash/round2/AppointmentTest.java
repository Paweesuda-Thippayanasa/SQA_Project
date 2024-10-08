package com.template.maven.example.gemini15flash.round2;
//File: AppointmentTest.java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.time.LocalDateTime;

public class AppointmentTest {

    private static final String PATIENT_NAME = "John Doe";
    private static final String DOCTOR_NAME = "Dr. Smith";
    private static final String APPOINTMENT_MAKER = "Jane Doe";
    private static final String CLINIC_CONTACT_NUMBER = "123-456-7890";
    private static final LocalDateTime APPOINTMENT_DATE_TIME = LocalDateTime.of(2024, 3, 15, 10, 0);

    @Test
    void testCreateAppointmentWithNotes() {
        Appointment appointment = new AppointmentWithNotes(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.TOOTH_EXTRACTION, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME, "Please bring your insurance card.");

        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.TOOTH_EXTRACTION, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals("Please bring your insurance card.", appointment.getNotes());
    }

    @Test
    void testCreateAppointmentWithoutNotes() {
        Appointment appointment = new AppointmentWithoutNotes(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.DEVICE_INSTALLATION, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME);

        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.DEVICE_INSTALLATION, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertNull(appointment.getNotes());
    }

    @Test
    void testAllAppointmentTypes() {
        Appointment appointment1 = new AppointmentWithNotes(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.TOOTH_EXTRACTION, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME, "Notes");
        Appointment appointment2 = new AppointmentWithNotes(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.DEVICE_INSTALLATION, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME, "Notes");
        Appointment appointment3 = new AppointmentWithNotes(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.MONTHLY_CHECK_UP, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME, "Notes");
        Appointment appointment4 = new AppointmentWithNotes(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.DEVICE_REMOVAL, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME, "Notes");

        assertNotNull(appointment1);
        assertNotNull(appointment2);
        assertNotNull(appointment3);
        assertNotNull(appointment4);
    }
}