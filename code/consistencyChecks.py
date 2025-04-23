# consistencyChecks.py
import pandas as pd
import numpy as np

def perform_consistency_checks(file_path):
    """
    Perform data consistency checks on the dataset including:
    - Missing values check
    - Duplicates check
    - Data types check
    - Outliers detection using IQR
    """
    # Load dataset
    df = pd.read_csv(file_path)
    
    # Initialize results dictionary
    results = {
        'missing_values': None,
        'duplicates': None,
        'data_types': None,
        'outliers': {}
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
        outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)]  # Fixed the condition here
        
        results['outliers'][col] = {
            'count': outliers.shape[0],
            'lower_bound': lower_bound,
            'upper_bound': upper_bound
        }
    
    return results

def print_consistency_results(results):
    """Print the results of the consistency checks in a readable format"""
    print("=== Data Consistency Check Results ===")
    
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

if __name__ == "__main__":
    # When run directly, perform checks on the default dataset
    file_path = "../data/publicmicrodatateachingsample.csv"
    results = perform_consistency_checks(file_path)
    print_consistency_results(results)