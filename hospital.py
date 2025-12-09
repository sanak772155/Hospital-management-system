import database

class Patient:
    """Represents a Patient entity."""
    def __init__(self, name, age, gender, phone, p_id=None):
        self.id = p_id
        self.name = name
        self.age = age
        self.gender = gender
        self.phone = phone

    def __str__(self):
        return f"ID: {self.id} | Name: {self.name} | Age: {self.age} | Phone: {self.phone}"


class Doctor:
    """Represents a Doctor entity."""
    def __init__(self, name, specialization, phone, d_id=None):
        self.id = d_id
        self.name = name
        self.specialization = specialization
        self.phone = phone

    def __str__(self):
        return f"ID: {self.id} | Dr. {self.name} | Spec: {self.specialization} | Phone: {self.phone}"


class Hospital:
    """
    The main controller class.
    This acts as the bridge between the User Interface (main.py)
    and the Data Layer (database.py).
    """

    def __init__(self):
        # Ensure the database tables exist when the system starts
        database.initialize_db()

    # --- Patient Management ---
    def create_patient(self, name, age, gender, phone):
        """Creates a Patient object and saves it to the DB."""
        # Simple validation
        if not name or not phone:
            print("Error: Name and Phone are required.")
            return False
        
        # Call database to save
        if database.add_patient(name, age, gender, phone):
            print(f"Patient {name} added successfully.")
            return True
        return False

    def list_patients(self):
        """Retrieves all patients from DB and displays them."""
        raw_data = database.get_all_patients()
        print("\n--- List of Patients ---")
        if not raw_data:
            print("No patients found.")
            return

        for row in raw_data:
            # Convert raw DB row to Patient Object for display
            p = Patient(row['name'], row['age'], row['gender'], row['phone'], row['id'])
            print(p)

    # --- Doctor Management ---
    def create_doctor(self, name, specialization, phone):
        if not name or not specialization:
            print("Error: Name and Specialization are required.")
            return False
            
        if database.add_doctor(name, specialization, phone):
            print(f"Dr. {name} added successfully.")
            return True
        return False

    def list_doctors(self):
        raw_data = database.get_all_doctors()
        print("\n--- List of Doctors ---")
        if not raw_data:
            print("No doctors found.")
            return

        for row in raw_data:
            d = Doctor(row['name'], row['specialization'], row['phone'], row['id'])
            print(d)

    # --- Appointment Management ---
    def book_appointment(self, patient_id, doctor_id, date_time, reason):
        if database.schedule_appointment(patient_id, doctor_id, date_time, reason):
            print("Appointment booked successfully.")
            return True
        else:
            print("Failed to book appointment. Please check IDs.")
            return False

    def list_appointments(self):
        raw_data = database.get_all_appointments()
        print("\n--- Scheduled Appointments ---")
        if not raw_data:
            print("No appointments found.")
            return

        for row in raw_data:
            print(f"ID: {row['id']} | Patient: {row['patient_name']} | "
                  f"Dr. {row['doctor_name']} | Time: {row['date_time']} | Reason: {row['reason']}")