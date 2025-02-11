from data_loader import load_csv_data, load_pandas_df
from data_retrieval import retrieve_demographic_info, retrieve_medical_history, retrieve_treatment_details, retrieve_custom_info
from analysis import top_3_treatments, average_wbc_counts, average_smoking_packs, average_survival_by_stage
from visualization import plot_treatment_proportions, plot_smoking_packs_by_stage, plot_blood_pressure_by_treatment,plot_treatment_effectiveness_by_age

def main():
    data, file_path = load_csv_data()
    if not data:
        return
    
    df = load_pandas_df(file_path)
    if df is None:
        return

    while True:
        print("\nLung Cancer Data Analysis Menu:")
        print("1. Retrieve Demographic Info")  # Task A1
        print("2. Retrieve Medical History")  # Task A2
        print("3. Retrieve Treatment Details")  # Task A3
        print("4. Retrieve Custom Data (User-defined Conditions)")  # Task A4
        print("5. Identify Top 3 Treatments for an Ethnicity")  # Task B1
        print("6. Analyse Average White Blood Cell Count by Treatment")  # Task B2
        print("7. Analyse Average Smoking Packs by Treatment & Tumor Location")  # Task B3
        print("8. Average Survival by Stage")  # Task B4
        print("9. Visualize Treatment Proportion")  # Task C1
        print("10. Visualize Smoking Packs by Stage")  # Task C2
        print("11. Visualize Blood Pressure by Treatment")  # Task C3
        print("12. Visualize Treatment Effectiveness by Age")  # Task C4
        print("13. Exit")
                
        choice = input("Enter your choice: ")
        
        if choice == '1':
            retrieve_demographic_info(data)
        elif choice == '2':
            retrieve_medical_history(data)
        elif choice == '3':
            retrieve_treatment_details(data)
        elif choice == '4':
            retrieve_custom_info(data)
        elif choice == '5':
            top_3_treatments(df)
        elif choice == '6':
            average_wbc_counts(df)
        elif choice == '7':
            average_smoking_packs(df)
        elif choice == '8':
            average_survival_by_stage(df)
        elif choice == '9':
            plot_treatment_proportions(df)
        elif choice == '10':
            plot_smoking_packs_by_stage(df)
        elif choice == '11':
            plot_blood_pressure_by_treatment(df)
        elif choice == '12':
            plot_treatment_effectiveness_by_age(df)
        elif choice == '13':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()