package com.template.maven.example.chatgpt.round3;

 enum AppointmentType {
    TOOTH_EXTRACTION,
    DEVICE_INSTALLATION,
    MONTHLY_CHECKUP,
    DEVICE_REMOVAL
}

public abstract class Appointment {
    private String patientName;
    private String doctorName;
    private AppointmentType appointmentType;
    private String bookedBy;
    private String clinicContactNumber;
    private String appointmentDateTime;
    private String notes;

    // Main method for demonstration
    public static void main(String[] args) {
    }

    // Template Method
    public final void scheduleAppointment(String patientName, String doctorName, AppointmentType appointmentType, String bookedBy, String clinicContactNumber, String appointmentDateTime) {
        this.patientName = patientName;
        this.doctorName = doctorName;
        this.appointmentType = appointmentType;
        this.bookedBy = bookedBy;
        this.clinicContactNumber = clinicContactNumber;
        this.appointmentDateTime = appointmentDateTime;
        this.notes = addNotes();
    }

    // Concrete methods for setting mandatory fields
    public String getPatientName() { return patientName; }
    public String getDoctorName() { return doctorName; }
    public AppointmentType getAppointmentType() { return appointmentType; }
    public String getBookedBy() { return bookedBy; }
    public String getClinicContactNumber() { return clinicContactNumber; }
    public String getAppointmentDateTime() { return appointmentDateTime; }

    // Optional hook method for adding notes
    protected String addNotes() {
        return "";
    }

    public String getNotes() { return notes; }
}

class ToothExtractionAppointment extends Appointment {
    @Override
    protected String addNotes() {
        return "Patient should avoid eating hard food for 24 hours.";
    }
}

class DeviceInstallationAppointment extends Appointment {
    @Override
    protected String addNotes() {
        return "Patient should follow up after one week.";
    }
}

class MonthlyCheckupAppointment extends Appointment {
    @Override
    protected String addNotes() {
        return "Check for any discomfort with the device.";
    }
}

class DeviceRemovalAppointment extends Appointment {
    @Override
    protected String addNotes() {
        return "Patient should wear retainers after device removal.";
    }
}
