package com.template.maven.example.gemini15pro.round2;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

import java.time.LocalDateTime;

class AppointmentTest {

    @Test
    void testCreateAppointment() {
        Appointment appointment = new Appointment() {}; // Anonymous class for testing
        LocalDateTime appointmentTime = LocalDateTime.of(2024, 3, 28, 10, 0);
        appointment.createAppointment("John Doe", "Dr. Smith", Appointment.AppointmentType.DEVICE_INSTALLATION, 
                "Jane Doe", "123-456-7890", appointmentTime);

        assertEquals("John Doe", appointment.getPatientName());
        assertEquals("Dr. Smith", appointment.getDoctorName());
        assertEquals(Appointment.AppointmentType.DEVICE_INSTALLATION, appointment.getAppointmentType());
        assertEquals("Jane Doe", appointment.getMadeBy());
        assertEquals("123-456-7890", appointment.getClinicContactNumber());
        assertEquals(appointmentTime, appointment.getAppointmentDateTime());
        assertNull(appointment.getNotes()); // Notes are null by default
    }

    @Test
    void testCreateAppointmentWithNotes() {
        Appointment appointment = new Appointment() {
            @Override
            protected void addNotes() {
                setNotes("Follow-up appointment needed.");
            }
        };
        LocalDateTime appointmentTime = LocalDateTime.of(2024, 3, 28, 10, 0);
        appointment.createAppointment("Alice Lee", "Dr. Brown", Appointment.AppointmentType.MONTHLY_CHECK_UP, 
                "Bob Lee", "987-654-3210", appointmentTime);
        
        assertEquals("Follow-up appointment needed.", appointment.getNotes());
    }

    @Test
    void testAllAppointmentTypes() {
        LocalDateTime appointmentTime = LocalDateTime.of(2024, 3, 28, 10, 0);
        createAndAssertAppointment("John Doe", "Dr. Smith", Appointment.AppointmentType.TOOTH_EXTRACTION, 
                "Jane Doe", "123-456-7890", appointmentTime);
        createAndAssertAppointment("Alice Lee", "Dr. Brown", Appointment.AppointmentType.DEVICE_INSTALLATION, 
                "Bob Lee", "987-654-3210", appointmentTime);
        createAndAssertAppointment("Charlie Brown", "Dr. Wilson", Appointment.AppointmentType.MONTHLY_CHECK_UP, 
                "Sally Brown", "555-123-4567", appointmentTime);
        createAndAssertAppointment("Lucy Van Pelt", "Dr. Schulz", Appointment.AppointmentType.DEVICE_REMOVAL, 
                "Linus Van Pelt", "111-222-3333", appointmentTime);
    }

    private void createAndAssertAppointment(String patientName, String doctorName, Appointment.AppointmentType appointmentType,
                                           String madeBy, String clinicContactNumber, LocalDateTime appointmentTime) {
        Appointment appointment = new Appointment() {}; 
        appointment.createAppointment(patientName, doctorName, appointmentType, madeBy, clinicContactNumber, appointmentTime);
        assertEquals(appointmentType, appointment.getAppointmentType());
    }
}