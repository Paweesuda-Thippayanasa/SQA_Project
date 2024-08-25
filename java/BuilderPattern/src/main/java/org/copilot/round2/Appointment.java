package org.copilot.round2;
// Appointment.java
import java.time.LocalDateTime;

public class Appointment {
    private final String patientName;
    private final String doctorName;
    private final AppointmentType appointmentType;
    private final String appointmentMakerName;
    private final String clinicContactNumber;
    private final LocalDateTime appointmentDateTime;
    private final String notes;

    private Appointment(AppointmentBuilder builder) {
        this.patientName = builder.patientName;
        this.doctorName = builder.doctorName;
        this.appointmentType = builder.appointmentType;
        this.appointmentMakerName = builder.appointmentMakerName;
        this.clinicContactNumber = builder.clinicContactNumber;
        this.appointmentDateTime = builder.appointmentDateTime;
        this.notes = builder.notes;
    }

    public static class AppointmentBuilder {
        private final String patientName;
        private final String doctorName;
        private final AppointmentType appointmentType;
        private final String appointmentMakerName;
        private final String clinicContactNumber;
        private final LocalDateTime appointmentDateTime;
        private String notes;

        public AppointmentBuilder(String patientName, String doctorName, AppointmentType appointmentType,
                                  String appointmentMakerName, String clinicContactNumber, LocalDateTime appointmentDateTime) {
            this.patientName = patientName;
            this.doctorName = doctorName;
            this.appointmentType = appointmentType;
            this.appointmentMakerName = appointmentMakerName;
            this.clinicContactNumber = clinicContactNumber;
            this.appointmentDateTime = appointmentDateTime;
        }

        public AppointmentBuilder setNotes(String notes) {
            this.notes = notes;
            return this;
        }

        public Appointment build() {
            return new Appointment(this);
        }
    }

    // Getters for all fields can be added here if needed

}

enum AppointmentType {
    TOOTH_EXTRACTION,
    DEVICE_INSTALLATION,
    MONTHLY_CHECKUP,
    DEVICE_REMOVAL
}