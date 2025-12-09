import sqlite3

DB_NAME = "hospital.db"

def get_db_connection():
    """Establishes a connection to the database."""
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

def initialize_db():
    """Creates the necessary tables if they do not exist."""
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        # 1. Create Patients Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS patients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT,
                phone TEXT UNIQUE
            )
        """)

        # 2. Create Doctors Table
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS doctors (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                specialization TEXT NOT NULL,
                phone TEXT UNIQUE
            )
        """)

        # 3. Create Appointments Table
        # Note: We use Foreign Keys to link to Patients and Doctors
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS appointments (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                patient_id INTEGER NOT NULL,
                doctor_id INTEGER NOT NULL,
                date_time TEXT NOT NULL,
                reason TEXT,
                FOREIGN KEY (patient_id) REFERENCES patients (id),
                FOREIGN KEY (doctor_id) REFERENCES doctors (id)
            )
        """)

        conn.commit()
        print("Database initialized successfully.")
    except sqlite3.Error as e:
        print(f"Error initializing database: {e}")
    finally:
        conn.close()

# --- Patient Operations ---

def add_patient(name, age, gender, phone):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO patients (name, age, gender, phone) VALUES (?, ?, ?, ?)", 
                       (name, age, gender, phone))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"Error: A patient with phone {phone} already exists.")
        return False
    except sqlite3.Error as e:
        print(f"Database Error: {e}")
        return False
    finally:
        conn.close()

def get_all_patients():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM patients")
    patients = cursor.fetchall()
    conn.close()
    return patients

# --- Doctor Operations ---

def add_doctor(name, specialization, phone):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO doctors (name, specialization, phone) VALUES (?, ?, ?)", 
                       (name, specialization, phone))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        print(f"Error: A doctor with phone {phone} already exists.")
        return False
    finally:
        conn.close()

def get_all_doctors():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM doctors")
    doctors = cursor.fetchall()
    conn.close()
    return doctors

# --- Appointment Operations ---

def schedule_appointment(patient_id, doctor_id, date_time, reason):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Verify if patient and doctor exist before booking
        cursor.execute("PRAGMA foreign_keys = ON") 
        cursor.execute("INSERT INTO appointments (patient_id, doctor_id, date_time, reason) VALUES (?, ?, ?, ?)", 
                       (patient_id, doctor_id, date_time, reason))
        conn.commit()
        return True
    except sqlite3.Error as e:
        print(f"Error scheduling appointment: {e}")
        return False
    finally:
        conn.close()

def get_all_appointments():
    conn = get_db_connection()
    cursor = conn.cursor()
    # Using JOIN to get names instead of just IDs
    query = """
        SELECT a.id, p.name as patient_name, d.name as doctor_name, a.date_time, a.reason 
        FROM appointments a
        JOIN patients p ON a.patient_id = p.id
        JOIN doctors d ON a.doctor_id = d.id
    """
    cursor.execute(query)
    appointments = cursor.fetchall()
    conn.close()
    return appointments