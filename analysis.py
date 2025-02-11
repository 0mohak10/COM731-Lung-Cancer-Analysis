def top_3_treatments(df):
    try:
        ethnicity = input("Enter the ethnicity: ")
        filtered_df = df[(df['Ethnicity'] == ethnicity) & (df['Survival_Months'] > 100)]
        treatment_counts = filtered_df['Treatment'].value_counts().nlargest(3)
        print(f"Top 3 treatments for {ethnicity} patients with survival > 100 months:\n{treatment_counts}")

    except KeyError as e:
        print(f"Error: Missing column {e} in the DataFrame.")
    
def average_wbc_counts(df):
    try:
        ethnicity = input("Enter the ethnicity: ")  
        treatments = input("Enter treatments (comma-separated): ").split(',')
        treatments = [t.strip() for t in treatments]
    
        filtered_df = df[(df['Ethnicity'] == ethnicity) & (df['Treatment'].isin(treatments))]
        average_wbc = filtered_df.groupby('Treatment')['White_Blood_Cell_Count'].mean()
        print(f"Average WBC counts for {ethnicity} patients receiving {', '.join(treatments)}:\n{average_wbc}")

    except KeyError as e:
        print(f"Error: Missing column {e} in the DataFrame.")

def average_smoking_packs(df):
    try:
        filtered_df = df[(df['Blood_Pressure_Pulse'] > 90) & (df['Tumor_Size_mm'] < 15.0)]
        average_smoking = filtered_df.groupby(['Treatment', 'Tumor_Location'])['Smoking_Pack_Years'].mean().unstack()
        print("Average smoking packs based on treatment and tumor location:")
        print(average_smoking)

    except KeyError as e:
        print(f"Error: Missing column {e} in the DataFrame.")
    
def average_survival_by_stage(df):
    try:
        filtered_df = df[df['Comorbidity_Diabetes'] == "Yes"]
        average_survival = filtered_df.groupby('Stage')['Survival_Months'].mean()
        print("Average survival months by stage for patients with diabetes:")
        print(average_survival)

    except KeyError as e:
        print(f"Error: Missing column {e} in the DataFrame.")
    