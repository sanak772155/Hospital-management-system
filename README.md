# Hospital-management-system
A simple and beginner-friendly Hospital Management System built in Python using SQLite. It helps manage patients, doctors, and basic hospital operations including adding records, updating details, searching data, and storing information securely in a local database.



Features:
Manage Patients

Add a new patient.
View all patients.
Search patients by name/ID.
Delete patient record.
Update patient information.
Manage Doctors

Add a new doctor.
View all doctors.
Search doctors by specialization/ID.
Delete doctor record.
Update doctor information.
Appointments

Schedule an appointment.
View all appointments.
Implementation:
hospital.py
This file defines the main OOP classes: Patient, Doctor, Hospital. Each class represents the core entities of the system.


database.py
This file handles the database operations using MYSQL (or any other DB). It can handle CRUD operations for patients, doctors, and appointments.



main.py
This is the entry point of the application that integrates all the functionalities, allowing the user to interact with the system through a command-line menu.


Additional Notes:
Use sqlite3 for the database backend (alternatively, MySQL/PostgreSQL can be used).
Add validation checks for user input.
You can extend the project to include more features such as billing, pharmacy management, etc.
