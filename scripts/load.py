import os

def load_to_local(df):
    # ensure 'output' folder exists
    os.makedirs('output', exist_ok=True)

    output_path = os.path.join('output', 'final_output.csv')
    df.to_csv(output_path, index=False)

    print(f" Data successfully saved to: {output_path}")
    print(df.head())  # show preview of saved data


if __name__ == "__main__":
    from extract import extract_data
    from transform import transform_data

    df = extract_data()
    df = transform_data(df)
    load_to_local(df)

