def retrieve_demographic_info(data):
    try:
        patient_id = input("Enter Patient ID: ")
        header, rows = data[0], data[1:]
        
        for row in rows:
            if row[header.index('Patient_ID')] == patient_id:
                result = {
                    "Age": row[header.index('Age')],
                    "Gender": row[header.index('Gender')],
                    "Smoking History": row[header.index('Smoking_History')],
                    "Ethnicity": row[header.index('Ethnicity')]
                }
                print(f"Patient Demographics: {result}")
                return

        print("Patient not found.")
    except KeyError as e:
        print(f"Error: Missing column {e} in the data.")
  
def retrieve_medical_history(data):
    try:
        ethnicity = input("Enter Ethnicity: ")
        header, rows = data[0], data[1:]
        results = []
        
        for row in rows:
            if row[header.index('Ethnicity')] == ethnicity:
                results.append({
                    "Family History": row[header.index('Family_History')],
                    "Diabetes": row[header.index('Comorbidity_Diabetes')], 
                    "Kidney Disease": row[header.index('Comorbidity_Kidney_Disease')], 
                    "Haemoglobin Level": row[header.index('Haemoglobin_Level')]
                })
        
        print(f"Medical History for Ethnicity '{ethnicity}': {results}")
    except KeyError as e:
        print(f"Error: Missing column {e} in the data.")
  
def retrieve_treatment_details(data):
    try:
        treatment = input("Enter Treatment Type: ")
        header, rows = data[0], data[1:]
        results = []
        
        for row in rows:
            if row[header.index('Treatment')] == treatment and int(row[header.index('Survival_Months')]) > 100:
                results.append({
                    "Age": row[header.index('Age')],
                    "Tumor Size": row[header.index('Tumor_Size_mm')],
                    "Tumor Location": row[header.index('Tumor_Location')],
                    "Tumor Stage": row[header.index('Stage')]
                })
        
        print(f"Patients with Treatment '{treatment}' and Survival > 100 months: {results}")
    except KeyError as e:
        print(f"Error: Missing column {e} in the data.")
    except ValueError:
        print("Error: Invalid data format in numeric fields.")

def retrieve_custom_info(data):
    try:
        header, rows = data[0], data[1:]
        results = []
        for row in rows:
            if float(row[header.index('White_Blood_Cell_Count')]) > 5:
                results.append({
                    "Blood Pressure Systolic": row[header.index('Blood_Pressure_Systolic')],
                    "Platelet Count": row[header.index('Platelet_Count')],
                    "Albumin Level": row[header.index('Albumin_Level')]
                })
        
        print(f"Patients with White_Blood_Cell_Count > 5: {results}")
    except KeyError as e:
        print(f"Error: Missing column {e} in the data.")
    except ValueError:
        print("Error: Invalid data format in numeric fields.")
   
