package com.template.maven.example.gemini15flash.round1;
//File: AppointmentTest.java
import org.junit.jupiter.api.Test;

import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.assertEquals;

class AppointmentTest {

    private static final String PATIENT_NAME = "John Doe";
    private static final String DOCTOR_NAME = "Dr. Smith";
    private static final String APPOINTMENT_MAKER = "Jane Doe";
    private static final String CLINIC_CONTACT_NUMBER = "123-456-7890";
    private static final LocalDateTime APPOINTMENT_DATE_TIME = LocalDateTime.of(2023, 10, 27, 10, 0, 0);

    @Test
    void testCreateAppointment_ToothExtraction() {
        Appointment.ToothExtractionAppointment appointment = new Appointment.ToothExtractionAppointment(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.TOOTH_EXTRACTION, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME);
        appointment.createAppointment();
        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.TOOTH_EXTRACTION, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals("Please bring a list of your current medications.", appointment.getNotes());
    }

    @Test
    void testCreateAppointment_DeviceInstallation() {
        Appointment.DeviceInstallationAppointment appointment = new Appointment.DeviceInstallationAppointment(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.DEVICE_INSTALLATION, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME);
        appointment.createAppointment();
        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.DEVICE_INSTALLATION, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals("Please bring your insurance card and ID.", appointment.getNotes());
    }

    @Test
    void testCreateAppointment_MonthlyCheckUp() {
        Appointment.MonthlyCheckUpAppointment appointment = new Appointment.MonthlyCheckUpAppointment(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.MONTHLY_CHECK_UP, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME);
        appointment.createAppointment();
        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.MONTHLY_CHECK_UP, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals("Please bring your previous X-rays.", appointment.getNotes());
    }

    @Test
    void testCreateAppointment_DeviceRemoval() {
        Appointment.DeviceRemovalAppointment appointment = new Appointment.DeviceRemovalAppointment(PATIENT_NAME, DOCTOR_NAME,
                Appointment.AppointmentType.DEVICE_REMOVAL, APPOINTMENT_MAKER, CLINIC_CONTACT_NUMBER,
                APPOINTMENT_DATE_TIME);
        appointment.createAppointment();
        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.DEVICE_REMOVAL, appointment.getAppointmentType());
        assertEquals(APPOINTMENT_MAKER, appointment.getAppointmentMaker());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals("Please bring your device removal form.", appointment.getNotes());
    }
}