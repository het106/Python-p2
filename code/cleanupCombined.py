# Combined version of cleanup.py and consistncyChecks.py

# data_quality_checks.py
import pandas as pd
import numpy as np

def make_valid_array(max_valid):
    """Helper function to create arrays of valid values"""
    return [-8] + list(range(1, (max_valid + 1)))

def perform_consistency_checks(file_path):
    """
    Perform data consistency checks on the dataset including:
    - Missing values check
    - Duplicates check
    - Data types check
    - Outliers detection using IQR
    - Validity checks against predefined value ranges
    """
    # Load dataset
    df = pd.read_csv(file_path)

    print("=== Data Quality Check Results ===")
    print(f"\nLenght of orignal dataset: {len(df)}")

    # Initialize results dictionary
    results = {
        'missing_values': None,
        'duplicates': None,
        'data_types': None,
        'exclusive_values': {},
        'invalid_values': {}
    }
    
    # 1. Checking for missing values
    missing_values = df.isnull().sum()
    results['missing_values'] = missing_values
    df = df.dropna()
    
    # 2. Check for duplicates
    duplicates = df.duplicated().sum()
    results['duplicates'] = duplicates
    df = df.drop_duplicates()
    
    # 3. Check for inconsistent data types
    data_types = df.dtypes
    results['data_types'] = data_types
    
    # 4. Check for mutually exlusive values
    # Full time students whose economic category should exclude students
    student_exclusive = df.loc[(df["in_full_time_education"] == 1) & (df["economic_activity_status_10m"] >= 1) & (df["economic_activity_status_10m"] <= 3) & (df["economic_activity_status_10m"] != -8)]
    # Married people who are below the legal age of marriage
    married_age_exclusive = df.loc[(df["resident_age_7d"] == 1) & (df["legal_partnership_status_6a"] == 2)]
    results['exclusive_values'] = pd.concat((student_exclusive, married_age_exclusive), axis=1)
    
    # 5. Check for invalid values based on predefined valid ranges
    # Define valid value arrays for each column
    valid_social_grades = make_valid_array(4)
    valid_birth_country = make_valid_array(2)
    valid_econ_activity = make_valid_array(9)
    valid_ethnic_group = make_valid_array(5)
    valid_health = make_valid_array(5)
    valid_family_type = make_valid_array(5)
    valid_hours_worked = make_valid_array(4)
    valid_in_education = make_valid_array(2)
    valid_industry = make_valid_array(9)
    valid_iol = ["-8", "E13000001", "E13000002"]
    valid_partner_status = make_valid_array(5)
    valid_occupation = make_valid_array(9)
    valid_region = ["E12000001", "E12000002", "E12000003", "E12000004", 
                   "E12000005", "E12000006", "E12000007", "E12000008", 
                   "E12000009", "W92000004", "N99999999", "S99999999"]
    valid_religion = make_valid_array(9)
    valid_residence = [1, 2]
    valid_age = make_valid_array(7)
    valid_sex = make_valid_array(2)
    valid_usual_short_student = make_valid_array(3)

    # Map each column to its valid values
    validity_mapping = {
        "approx_social_grade": valid_social_grades,
        "country_of_birth_3a": valid_birth_country,
        "economic_activity_status_10m": valid_econ_activity,
        "ethnic_group_tb_6a": valid_ethnic_group,
        "health_in_general": valid_health,
        "hh_families_type_6a": valid_family_type,
        "hours_per_week_worked": valid_hours_worked,
        "in_full_time_education": valid_in_education,
        "industry_10a": valid_industry,
        "iol22cd": valid_iol,
        "legal_partnership_status_6a": valid_partner_status,
        "occupation_10a": valid_occupation,
        "region": valid_region,
        "religion_tb": valid_religion,
        "residence_type": valid_residence,
        "resident_age_7d": valid_age,
        "sex": valid_sex,
        "usual_short_student": valid_usual_short_student
    }
    
    # Skip the resident_id_m column as it is an identifier
    columns_to_check = [col for col in df.columns if col != "resident_id_m"]
    
    for col in columns_to_check:
        if col in validity_mapping:
            invalid_mask = ~df[col].isin(validity_mapping[col])
            invalid_count = invalid_mask.sum()
            results['invalid_values'][col] = {
                'count': invalid_count,
                'invalid_values': df[col][invalid_mask].unique().tolist() if invalid_count > 0 else None
            }
            df = df.drop(df[invalid_mask].index)
    
    print(f"Length of cleaned dataset: {len(df)}")

    df.to_csv("../data/cleaned_data.csv")
    return results

def print_consistency_results(results):
    """Print the results of the consistency checks in a readable format"""
    
    print("\n1. Missing Values:")
    print(results['missing_values'])
    
    print("\n2. Duplicate Rows:")
    print(f"Number of duplicate rows: {results['duplicates']}")
    
    print("\n3. Data Types:")
    print(results['data_types'])
    
    print("\n4. Mutually Exclusive Values Rows: ")
    if (len(results['exclusive_values']) == 0): 
        print("None")
    else:
        for index, row in results['exclusive_values'].iterrows():
            print(f"Index: {index}") 

    print("\n5. Invalid Values Check:")
    for col, data in results['invalid_values'].items():
        print(f"\nColumn: {col}")
        print(f"Number of invalid values: {data['count']}")
        if data['count'] > 0:
            print(f"Invalid values found: {data['invalid_values']}")

if __name__ == "__main__":
    # When run directly, perform checks on the default dataset
    file_path = "../data/invalidCensus.csv"
    results = perform_consistency_checks(file_path)
    print_consistency_results(results)