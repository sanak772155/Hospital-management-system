# utils.py
def save_patient_to_file(patient):
    with open('data/patients.txt', 'a') as file:
        file.write(f"{patient.patient_id},{patient.name},{patient.age},{patient.gender},{patient.disease}\n")

def load_patients_from_file():
    patients = []
    try:
        with open('data/patients.txt', 'r') as file:
            for line in file:
                patient_data = line.strip().split(',')
                patients.append({
                    "patient_id": int(patient_data[0]),
                    "name": patient_data[1],
                    "age": int(patient_data[2]),
                    "gender": patient_data[3],
                    "disease": patient_data[4]
                })
    except FileNotFoundError:
        print("No patient records found.")
    return patients
