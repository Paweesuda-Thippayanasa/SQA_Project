package org.geminiflash.round1;

import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.assertEquals;

public class AppointmentTest {

    private static final String PATIENT_NAME = "John Doe";
    private static final String DOCTOR_NAME = "Dr. Smith";
    private static final String APPOINTMENT_MAKER = "Jane Doe";
    private static final String CLINIC_CONTACT_NUMBER = "123-456-7890";
    private static final LocalDateTime APPOINTMENT_DATE_TIME = LocalDateTime.of(2023, 12, 25, 10, 0);
    private static final String NOTES = "Please bring X-rays.";

    @Test
    void testCreateAppointmentWithAllFields() {
        Appointment appointment = new Appointment.Builder(PATIENT_NAME, DOCTOR_NAME, Appointment.AppointmentType.MONTHLY_CHECK_UP, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER, APPOINTMENT_DATE_TIME)
                .withNotes(NOTES)
                .build();

        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.MONTHLY_CHECK_UP, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals(NOTES, appointment.getNotes());
    }

    @Test
    void testCreateAppointmentWithoutNotes() {
        Appointment appointment = new Appointment.Builder(PATIENT_NAME, DOCTOR_NAME, Appointment.AppointmentType.TOOTH_EXTRACTION, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER, APPOINTMENT_DATE_TIME)
                .build();

        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.TOOTH_EXTRACTION, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals(null, appointment.getNotes());
    }

    @Test
    void testCreateAppointmentWithDifferentAppointmentType() {
        Appointment appointment = new Appointment.Builder(PATIENT_NAME, DOCTOR_NAME, Appointment.AppointmentType.DEVICE_INSTALLATION, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER, APPOINTMENT_DATE_TIME)
                .build();

        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.DEVICE_INSTALLATION, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals(null, appointment.getNotes());
    }

    @Test
    void testCreateAppointmentWithDeviceRemoval() {
        Appointment appointment = new Appointment.Builder(PATIENT_NAME, DOCTOR_NAME, Appointment.AppointmentType.DEVICE_REMOVAL, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER, APPOINTMENT_DATE_TIME)
                .build();

        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.DEVICE_REMOVAL, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals(null, appointment.getNotes());
    }
}