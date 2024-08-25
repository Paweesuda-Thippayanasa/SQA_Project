package com.template.maven.example.gemini15pro.round3;
import org.junit.jupiter.api.*;
import java.time.LocalDateTime;

import static org.junit.jupiter.api.Assertions.*;

class AppointmentTest {

    private static final String PATIENT_NAME = "John Doe";
    private static final String DOCTOR_NAME = "Dr. Smith";
    private static final AppointmentType APPOINTMENT_TYPE = AppointmentType.MONTHLY_CHECK_UP;
    private static final String MADE_BY = "Jane Doe";
    private static final String CLINIC_CONTACT_NUMBER = "123-456-7890";
    private static final LocalDateTime APPOINTMENT_DATE_TIME = LocalDateTime.of(2024, 3, 15, 10, 0);
    private static final String NOTES = "Follow up on X-ray results";

    @Test
    void testCreateAppointment() {
        // Create an instance of a concrete Appointment class (e.g., NewPatientAppointment)
        Appointment appointment = new NewPatientAppointment(PATIENT_NAME, DOCTOR_NAME, APPOINTMENT_TYPE, MADE_BY,
                CLINIC_CONTACT_NUMBER, APPOINTMENT_DATE_TIME);
        appointment.setNotes(NOTES); 

        // Call the template method to create the appointment
        appointment.createAppointment();

        // Assertions to verify appointment details
        assertEquals(PATIENT_NAME, appointment.getPatientName());
        assertEquals(DOCTOR_NAME, appointment.getDoctorName());
        assertEquals(APPOINTMENT_TYPE, appointment.getAppointmentType());
        assertEquals(MADE_BY, appointment.getMadeBy());
        assertEquals(CLINIC_CONTACT_NUMBER, appointment.getClinicContactNumber());
        assertEquals(APPOINTMENT_DATE_TIME, appointment.getAppointmentDateTime());
        assertEquals(NOTES, appointment.getNotes());
    }
    @Test
    void testAppointmentTypes() {
        for (AppointmentType type : AppointmentType.values()) {
            Appointment appointment = new NewPatientAppointment(PATIENT_NAME, DOCTOR_NAME, type, MADE_BY, CLINIC_CONTACT_NUMBER, APPOINTMENT_DATE_TIME);
            appointment.createAppointment();
            assertEquals(type, appointment.getAppointmentType());
        }
    }
}

class NewPatientAppointment extends Appointment {

    public NewPatientAppointment(String patientName, String doctorName, AppointmentType appointmentType, String madeBy, String clinicContactNumber, LocalDateTime appointmentDateTime) {
        super(patientName, doctorName, appointmentType, madeBy, clinicContactNumber, appointmentDateTime);
    }

    @Override
    protected void setPatientName() {
        // Logic to set patient name
    }

    @Override
    protected void setDoctorName() {
        // Logic to set doctor name
    }

    @Override
    protected void setAppointmentType() {
        // Logic to set appointment type
    }

    @Override
    protected void setMadeBy() {
        // Logic to set who made the appointment
    }

    @Override
    protected void setClinicContactNumber() {
        // Logic to set the clinic contact number
    }

    @Override
    protected void setAppointmentDateTime() {
        // Logic to set appointment date and time
    }
}