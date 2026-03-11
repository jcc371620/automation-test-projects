import pandas as pd
from datetime import datetime

def generate_report(df, output_file="report.txt"):
    """
    Generate a plain-text statistical summary report, including:
    - Basic shape info
    - Missing value counts per column
    - Descriptive statistics (mean, std, min, max, etc.)
    """
    # Capture the current timestamp for the report header
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Build a dict of sections to write into the report
    report = {
        "Report Generated At": timestamp,
        "Total Rows": len(df),
        "Total Columns": len(df.columns),
        "Column Names": list(df.columns),
        "Missing Values per Column": df.isnull().sum().to_dict(),
        "Descriptive Statistics": df.describe().to_dict(),
    }

    # Write each section to the output file
    with open(output_file, "w", encoding="utf-8") as f:
        f.write("=" * 50 + "\n")
        f.write("       DATA ANALYSIS REPORT\n")
        f.write("=" * 50 + "\n")

        for section, content in report.items():
            f.write(f"\n[ {section} ]\n")
            # If content is a dict, print each key-value pair on its own line
            if isinstance(content, dict):
                for k, v in content.items():
                    f.write(f"  {k}: {v}\n")
            else:
                f.write(f"  {content}\n")

    print(f"Report saved to: {output_file}")