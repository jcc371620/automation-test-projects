import pandas as pd

def clean_data(filepath):
    """
    Automatically clean a CSV file:
    - Remove rows with too many missing values
    - Fill remaining missing values with median
    - Remove duplicate rows
    - Standardize column names
    """
    # Load raw CSV data into a DataFrame
    df = pd.read_csv(filepath)
    print(f"Original data: {len(df)} rows, {len(df.columns)} columns")

    # Drop rows where more than 50% of values are missing
    threshold = len(df.columns) * 0.5
    df.dropna(thresh=threshold, inplace=True)

    # Fill missing numeric values with the median of each column
    # (median is more robust than mean when outliers exist)
    df.fillna(df.median(numeric_only=True), inplace=True)

    # Remove exact duplicate rows to avoid double-counting
    df.drop_duplicates(inplace=True)

    # Standardize column names:
    # strip whitespace → lowercase → replace spaces with underscores
    # e.g. "  First Name " → "first_name"
    df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')

    # Save the cleaned data to a new file (keep original untouched)
    df.to_csv('cleaned_data.csv', index=False)
    print(f"Cleaning complete. Remaining rows: {len(df)}")
    return df