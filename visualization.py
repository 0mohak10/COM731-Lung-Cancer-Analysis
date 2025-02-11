import matplotlib.pyplot as plt

def plot_treatment_proportions(df):
    try:
        ethnicity = input("Enter Ethnicity: ").strip()
        filtered_df = df[df['Ethnicity'] == ethnicity]
        
        if filtered_df.empty:
            print(f"No data found for ethnicity: {ethnicity}")
            return

        treatment_counts = filtered_df['Treatment'].value_counts()
        treatment_counts.plot(kind='pie', autopct='%1.1f%%', startangle=90, colormap='Set3')

        plt.title(f'Proportion of Treatments for {ethnicity}')
        plt.ylabel("")
        plt.show()
    except KeyError as e:
        print(f"Missing column: {e}")

def plot_smoking_packs_by_stage(df):
    try:
        ethnicity = input("Enter Ethnicity: ").strip()
        filtered_df = df[df['Ethnicity'] == ethnicity]
        
        if filtered_df.empty:
            print(f"No data found for ethnicity: {ethnicity}")
            return

        avg_smoking_packs = filtered_df.groupby('Stage')['Smoking_Pack_Years'].mean()
        avg_smoking_packs.plot(kind='line', marker='o', colormap='coolwarm')

        plt.title(f'Average Smoking Packs by Cancer Stage for {ethnicity}')
        plt.xlabel('Cancer Stage')
        plt.ylabel('Average Smoking Pack Years')
        plt.grid(True)
        plt.show()
    except KeyError as e:
        print(f"Missing column: {e}")


def plot_blood_pressure_by_treatment(df):
    try:
        treatment = input("Enter Treatment Type: ").strip()
        filtered_df = df[df['Treatment'] == treatment]
        
        if filtered_df.empty:
            print(f"No data found for treatment: {treatment}")
            return

        blood_pressures = ['Blood_Pressure_Systolic', 'Blood_Pressure_Diastolic', 'Blood_Pressure_Pulse']
        avg_bp = filtered_df[blood_pressures].mean()

        avg_bp.plot(kind='bar', colormap='coolwarm')
        plt.title(f'Average Blood Pressure for {treatment}')
        plt.xlabel('Blood Pressure Type')
        plt.ylabel('Average Value')
        plt.grid(axis='y')
        plt.show()
    except KeyError as e:
        print(f"Missing column: {e}")


def plot_treatment_effectiveness_by_age(df):
    try:
        df['Age_Group'] = df['Age'].apply(lambda x: (x // 10) * 10)
        
        treatment = input("Enter Treatment Type: ").strip()
        filtered_df = df[df['Treatment'] == treatment]

        if filtered_df.empty:
            print(f"No data found for treatment: {treatment}")
            return

        avg_survival = filtered_df.groupby('Age_Group')['Survival_Months'].mean()
        avg_survival.plot(kind='line', marker='o', colormap='coolwarm')

        plt.title(f'Treatment Effectiveness by Age Group for {treatment}')
        plt.xlabel('Age Group')
        plt.ylabel('Average Survival Months')
        plt.grid(True)
        plt.show()
    except KeyError as e:
        print(f"Missing column: {e}")
    except ValueError as e:
        print(f"Invalid data type: {e}")
