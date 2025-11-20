r"""
Bank Customer Data Processing Script
------------------------------------
This script demonstrates AI-assisted data cleaning on customer CSV records.
It performs the following tasks:
1. Cleans missing values by imputing or dropping.
2. Removes duplicate records.
3. Standardizes phone numbers into a consistent format: +91-XXXXXXXXXX

Author: THALLAPELLI SAVIN KUMAR
Date: 20-Nov-2025
"""

import pandas as pd
import re

# -------------------------------
# Function Definitions
# -------------------------------

def clean_missing_values(df, strategy="drop"):
    """
    Clean missing values in the DataFrame.
    
    Parameters:
    df (pd.DataFrame): Input DataFrame with potential missing values.
    strategy (str): Strategy for handling missing values:
                    - 'drop': Drop rows with any missing value
                    - 'fill': Fill missing values with default values
                      (example: empty string for object columns, 0 for numeric)
    
    Returns:
    pd.DataFrame: DataFrame with missing values handled.
    """
    if strategy == "drop":
        return df.dropna()
    elif strategy == "fill":
        for col in df.columns:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("")
            else:
                df[col] = df[col].fillna(0)
        return df
    else:
        raise ValueError("Invalid strategy. Choose 'drop' or 'fill'.")

def remove_duplicates(df):
    """
    Remove duplicate records based on all columns.
    """
    return df.drop_duplicates()

def standardize_phone_number(phone):
    """
    Standardize phone number to format: +91-XXXXXXXXXX
    """
    if pd.isna(phone):
        return ""
    digits = re.sub(r"\D", "", str(phone))  # remove non-digit characters
    if len(digits) == 10:
        return "+91-" + digits
    elif len(digits) == 12 and digits.startswith("91"):
        return "+91-" + digits[2:]
    else:
        return ""  # invalid number

def standardize_phone_numbers(df, phone_col="Phone"):
    """
    Apply phone number standardization to a DataFrame column.
    """
    if phone_col in df.columns:
        df[phone_col] = df[phone_col].apply(standardize_phone_number)
    else:
        print(f"Warning: Phone column '{phone_col}' not found.")
    return df

# -------------------------------
# Main Processing Script
# -------------------------------

def process_customer_csv():
    # Use raw strings for Windows file paths
    file_path = r"C:\Users\savin\OneDrive\Desktop\AIAC LAB\LAB_TEST_FINAL\customer_data.csv"
    output_path = r"C:\Users\savin\OneDrive\Desktop\AIAC LAB\LAB_TEST_FINAL\customer_data_cleaned.csv"
    
    # Load CSV
    df = pd.read_csv(file_path)
    print("Columns in CSV:", df.columns.tolist())
    print("Number of rows:", len(df))
    print("First 10 rows:\n", df.head(10), "\n")
    
    # Step 1: Clean missing values
    df_clean = clean_missing_values(df, strategy="fill")
    
    # Step 2: Remove duplicates
    df_unique = remove_duplicates(df_clean)
    
    # Step 3: Standardize phone numbers
    # Update 'Phone' if your CSV uses a different column name
    df_final = standardize_phone_numbers(df_unique, phone_col="Phone")
    
    # Save cleaned CSV
    df_final.to_csv(output_path, index=False)
    
    # Print cleaned data
    print(f"Cleaned data saved to: {output_path}")
    print("Cleaned Data Preview:\n", df_final.to_string())

# -------------------------------
# Run the script
# -------------------------------
if __name__ == "__main__":
    process_customer_csv()
