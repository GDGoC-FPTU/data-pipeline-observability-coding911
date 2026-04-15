"""
==============================================================
Day 10 Lab: Build Your First Automated ETL Pipeline
==============================================================
Student ID: AI20K-2A202600182
Name: Nguyễn Minh Trí

Nhiem vu:
   1. Extract:   Doc du lieu tu file JSON
   2. Validate:  Kiem tra & loai bo du lieu khong hop le
   3. Transform: Chuan hoa category + tinh gia giam 10%
   4. Load:      Luu ket qua ra file CSV

Cham diem tu dong:
   - Script phai chay KHONG LOI (20d)
   - Validation: loai record gia <= 0, category rong (10d)
   - Transform: discounted_price + category Title Case (10d)
   - Logging: in so record processed/dropped (10d)
   - Timestamp: them cot processed_at (10d)
==============================================================
"""

import json
import pandas as pd
import os
import datetime

# --- CONFIGURATION ---
SOURCE_FILE = 'raw_data.json'
OUTPUT_FILE = 'processed_data.csv'


def extract(file_path):
    """
    Task 1: Doc du lieu JSON tu file.
    """
    print(f"Extracting data from {file_path}...")
    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Khong tim thay file: {file_path}")
            
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    except Exception as e:
        print(f"Error during extraction: {e}")
        return None

def validate(data):
    """
    Task 2: Kiem tra chat luong du lieu.
    """
    valid_records = []
    dropped_count = 0  

    for record in data:
        price = record.get('price', 0)
        category = record.get('category', "")

        if price > 0 and category and str(category).strip() != "":
            valid_records.append(record)
        else:
            dropped_count += 1
    print(f"Validation complete. Processed: {len(data)}, Dropped: {dropped_count} invalid records.")
    
    return valid_records

def transform(data):
    """
    Task 3: Ap dung business logic.
    - discounted_price = price * 0.9
    - category -> Title Case
    - processed_at = timestamp
    """
    if not data:
        return None

    # Tao DataFrame
    df = pd.DataFrame(data)
    df['discounted_price'] = df['price'] * 0.9
    df['category'] = df['category'].str.title()
    df['processed_at'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return df


def load(df, output_path):
    """
    Task 4: Luu DataFrame ra file CSV.
    """
    try:
        df.to_csv(output_path, index=False)
        print(f"Data successfully saved to {output_path}")
    except Exception as e:
        print(f"Error during loading: {e}")


# ============================================================
# MAIN PIPELINE
# ============================================================
if __name__ == "__main__":
    print("=" * 50)
    print("ETL Pipeline Started...")
    print("=" * 50)

    # 1. Extract
    raw_data = extract(SOURCE_FILE)

    if raw_data is not None:
        # 2. Validate
        clean_data = validate(raw_data)

        if clean_data:
            # 3. Transform
            final_df = transform(clean_data)

            # 4. Load
            if final_df is not None:
                load(final_df, OUTPUT_FILE)
                print("=" * 50)
                print(f"SUCCESS: Pipeline completed! {len(final_df)} records processed.")
            else:
                print("\nTransform returned None. Check your transform() function.")
        else:
            print("\nNo valid records found after validation.")
    else:
        print("\nPipeline aborted: No data extracted.")