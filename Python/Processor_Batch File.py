import pandas as pd
from pathlib import Path

def batch_process(folder="./data", output_file="merged_output.csv"):
    """
    Scan a folder for all CSV files, load and tag each one,
    then merge them into a single output file.
    Useful when data arrives as monthly or regional splits.
    """
    all_dfs = []  # Collect each file's DataFrame here

    # Iterate over every .csv file in the target folder
    for file in Path(folder).glob("*.csv"):
        # Read the file into a DataFrame
        df = pd.read_csv(file)

        # Tag each row with its source filename so we can trace it later
        df["source_file"] = file.name

        all_dfs.append(df)
        print(f"Loaded: {file.name}  ({len(df)} rows)")

    # If no files were found, exit early with a warning
    if not all_dfs:
        print("No CSV files found in the specified folder.")
        return None

    # Concatenate all DataFrames vertically; reset index to avoid duplicates
    combined = pd.concat(all_dfs, ignore_index=True)
    combined.to_csv(output_file, index=False)
    print(f"\nMerge complete. Total rows: {len(combined)} → saved to {output_file}")
    return combined