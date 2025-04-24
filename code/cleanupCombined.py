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
    
    # Initialize results dictionary
    results = {
        'missing_values': None,
        'duplicates': None,
        'data_types': None,
        'outliers': {},
        'invalid_values': {}
    }
    
    # 1. Checking for missing values
    missing_values = df.isnull().sum()
    results['missing_values'] = missing_values
    
    # 2. Check for duplicates
    duplicates = df.duplicated().sum()
    results['duplicates'] = duplicates
    
    # 3. Check for inconsistent data types
    data_types = df.dtypes
    results['data_types'] = data_types
    
    # 4. Check for outliers in numerical columns using IQR
    numerical_columns = df.select_dtypes(include=[np.number]).columns
    
    for col in numerical_columns:
        Q1 = df[col].quantile(0.25)
        Q3 = df[col].quantile(0.75)
        IQR = Q3 - Q1

        # Setting the IQR bounds
        lower_bound = Q1 - 1.5 * IQR
        upper_bound = Q3 + 1.5 * IQR
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]
        
        results['outliers'][col] = {
            'count': outliers.shape[0],
            'lower_bound': lower_bound,
            'upper_bound': upper_bound
        }
    
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
        "birth_country": valid_birth_country,
        "economic_activity_last_week": valid_econ_activity,
        "ethnic_group": valid_ethnic_group,
        "general_health": valid_health,
        "household_family_type": valid_family_type,
        "hours_worked_per_week": valid_hours_worked,
        "in_education": valid_in_education,
        "industry_current": valid_industry,
        "iol_region": valid_iol,
        "partner_status": valid_partner_status,
        "occupation_current": valid_occupation,
        "region": valid_region,
        "religion": valid_religion,
        "residence_type": valid_residence,
        "age": valid_age,
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
    
    return results

def print_consistency_results(results):
    """Print the results of the consistency checks in a readable format"""
    print("=== Data Quality Check Results ===")
    
    print("\n1. Missing Values:")
    print(results['missing_values'])
    
    print("\n2. Duplicate Rows:")
    print(f"Number of duplicate rows: {results['duplicates']}")
    
    print("\n3. Data Types:")
    print(results['data_types'])
    
    print("\n4. Outliers Detection (using IQR method):")
    for col, data in results['outliers'].items():
        print(f"\nColumn: {col}")
        print(f"Number of outliers: {data['count']}")
        print(f"Lower bound: {data['lower_bound']:.2f}")
        print(f"Upper bound: {data['upper_bound']:.2f}")
    
    print("\n5. Invalid Values Check:")
    for col, data in results['invalid_values'].items():
        print(f"\nColumn: {col}")
        print(f"Number of invalid values: {data['count']}")
        if data['count'] > 0:
            print(f"Invalid values found: {data['invalid_values']}")

if __name__ == "__main__":
    # When run directly, perform checks on the default dataset
    file_path = "../data/publicmicrodatateachingsample.csv"
    results = perform_consistency_checks(file_path)
    print_consistency_results(results)