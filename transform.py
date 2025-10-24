import pandas as pd

def transform_data(df):
    
    df = df.dropna()
    df['total_price'] = df['quantity'] * df['unit_price']
    print("Transformation complete.")
    return df
