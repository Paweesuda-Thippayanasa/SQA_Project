package com.template.maven.example.chatgpt.round3;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class AppointmentTest {
    private ToothExtractionAppointment toothExtractionAppointment;
    private DeviceInstallationAppointment deviceInstallationAppointment;
    private MonthlyCheckupAppointment monthlyCheckupAppointment;
    private DeviceRemovalAppointment deviceRemovalAppointment;

    @BeforeEach
    void setUp() {
        toothExtractionAppointment = new ToothExtractionAppointment();
        deviceInstallationAppointment = new DeviceInstallationAppointment();
        monthlyCheckupAppointment = new MonthlyCheckupAppointment();
        deviceRemovalAppointment = new DeviceRemovalAppointment();
    }

    @Test
    void testToothExtractionAppointment() {
        toothExtractionAppointment.scheduleAppointment("John Doe", "Dr. Smith", AppointmentType.TOOTH_EXTRACTION, "Jane Doe", "123-456-7890", "2024-09-01 10:00 AM");
        assertEquals("John Doe", toothExtractionAppointment.getPatientName());
        assertEquals("Dr. Smith", toothExtractionAppointment.getDoctorName());
        assertEquals(AppointmentType.TOOTH_EXTRACTION, toothExtractionAppointment.getAppointmentType());
        assertEquals("Jane Doe", toothExtractionAppointment.getBookedBy());
        assertEquals("123-456-7890", toothExtractionAppointment.getClinicContactNumber());
        assertEquals("2024-09-01 10:00 AM", toothExtractionAppointment.getAppointmentDateTime());
        assertEquals("Patient should avoid eating hard food for 24 hours.", toothExtractionAppointment.getNotes());
    }

    @Test
    void testDeviceInstallationAppointment() {
        deviceInstallationAppointment.scheduleAppointment("John Doe", "Dr. Smith", AppointmentType.DEVICE_INSTALLATION, "Jane Doe", "123-456-7890", "2024-09-02 11:00 AM");
        assertEquals("John Doe", deviceInstallationAppointment.getPatientName());
        assertEquals("Dr. Smith", deviceInstallationAppointment.getDoctorName());
        assertEquals(AppointmentType.DEVICE_INSTALLATION, deviceInstallationAppointment.getAppointmentType());
        assertEquals("Jane Doe", deviceInstallationAppointment.getBookedBy());
        assertEquals("123-456-7890", deviceInstallationAppointment.getClinicContactNumber());
        assertEquals("2024-09-02 11:00 AM", deviceInstallationAppointment.getAppointmentDateTime());
        assertEquals("Patient should follow up after one week.", deviceInstallationAppointment.getNotes());
    }

    @Test
    void testMonthlyCheckupAppointment() {
        monthlyCheckupAppointment.scheduleAppointment("John Doe", "Dr. Smith", AppointmentType.MONTHLY_CHECKUP, "Jane Doe", "123-456-7890", "2024-09-03 12:00 PM");
        assertEquals("John Doe", monthlyCheckupAppointment.getPatientName());
        assertEquals("Dr. Smith", monthlyCheckupAppointment.getDoctorName());
        assertEquals(AppointmentType.MONTHLY_CHECKUP, monthlyCheckupAppointment.getAppointmentType());
        assertEquals("Jane Doe", monthlyCheckupAppointment.getBookedBy());
        assertEquals("123-456-7890", monthlyCheckupAppointment.getClinicContactNumber());
        assertEquals("2024-09-03 12:00 PM", monthlyCheckupAppointment.getAppointmentDateTime());
        assertEquals("Check for any discomfort with the device.", monthlyCheckupAppointment.getNotes());
    }

    @Test
    void testDeviceRemovalAppointment() {
        deviceRemovalAppointment.scheduleAppointment("John Doe", "Dr. Smith", AppointmentType.DEVICE_REMOVAL, "Jane Doe", "123-456-7890", "2024-09-04 01:00 PM");
        assertEquals("John Doe", deviceRemovalAppointment.getPatientName());
        assertEquals("Dr. Smith", deviceRemovalAppointment.getDoctorName());
        assertEquals(AppointmentType.DEVICE_REMOVAL, deviceRemovalAppointment.getAppointmentType());
        assertEquals("Jane Doe", deviceRemovalAppointment.getBookedBy());
        assertEquals("123-456-7890", deviceRemovalAppointment.getClinicContactNumber());
        assertEquals("2024-09-04 01:00 PM", deviceRemovalAppointment.getAppointmentDateTime());
        assertEquals("Patient should wear retainers after device removal.", deviceRemovalAppointment.getNotes());
    }
}
