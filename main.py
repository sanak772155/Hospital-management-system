from hospital import Hospital
def print_menu():
    print("\n" + "="*30)
    print("   HOSPITAL MANAGEMENT SYSTEM")
    print("="*30)
    print("1. Add New Patient")
    print("2. View All Patients")
    print("3. Add New Doctor")
    print("4. View All Doctors")
    print("5. Book Appointment")
    print("6. View Appointments")
    print("7. Exit")
    print("="*30)

def main():
    # Initialize the Hospital System
    hospital = Hospital()

    while True:
        print_menu()
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            # Add Patient
            print("\n--- Register New Patient ---")
            name = input("Enter Name: ")
            age = input("Enter Age: ")
            gender = input("Enter Gender: ")
            phone = input("Enter Phone: ")
            hospital.create_patient(name, age, gender, phone)

        elif choice == '2':
            # View Patients
            hospital.list_patients()

        elif choice == '3':
            # Add Doctor
            print("\n--- Register New Doctor ---")
            name = input("Enter Doctor Name: ")
            spec = input("Enter Specialization: ")
            phone = input("Enter Phone: ")
            hospital.create_doctor(name, spec, phone)

        elif choice == '4':
            # View Doctors
            hospital.list_doctors()

        elif choice == '5':
            # Book Appointment
            print("\n--- Book Appointment ---")
            # Show lists first so user knows the IDs
            hospital.list_patients()
            hospital.list_doctors()
            
            try:
                p_id = int(input("\nEnter Patient ID: "))
                d_id = int(input("Enter Doctor ID: "))
                date = input("Enter Date/Time (e.g., 2023-10-25 10:00 AM): ")
                reason = input("Reason for visit: ")
                hospital.book_appointment(p_id, d_id, date, reason)
            except ValueError:
                print("Error: IDs must be numbers.")

        elif choice == '6':
            # View Appointments
            hospital.list_appointments()

        elif choice == '7':
            print("Exiting system...")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()