import pandas as pd

def extract_data():
    # Simulated extraction from CSV or API
    df = pd.read_csv('data/sample_data.csv')
    print(f"Extracted {len(df)} records.")
    return df
