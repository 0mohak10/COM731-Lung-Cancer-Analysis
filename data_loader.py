import pandas as pd
import csv

def load_csv_data():
    file_path = input("Enter the path of the CSV file: ").strip()
    try:
        with open(file_path, mode='r') as file:
            reader = csv.reader(file)
            data = [row for row in reader]
        return data, file_path
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return [], None

def load_pandas_df(file_path):
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
        return None
