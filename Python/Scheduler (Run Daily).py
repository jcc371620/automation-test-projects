import schedule
import time
import pandas as pd

def daily_pipeline():
    """
    Full daily data pipeline:
    1. Load raw data
    2. Clean it
    3. Generate a statistical report
    4. Save visualizations
    Run automatically every day at 08:00.
    """
    print("=" * 40)
    print("Daily pipeline started...")

    # Step 1: Load the latest raw data
    df = pd.read_csv("data.csv")

    # Step 2: Clean the data (reusing the function from script 1)
    df = clean_data("data.csv")

    # Step 3: Generate and save the statistical report
    generate_report(df, output_file="daily_report.txt")

    # Step 4: Save charts for all numeric columns
    auto_plot(df, output_dir="./daily_charts")

    print("Daily pipeline complete!")
    print("=" * 40)


# Schedule the pipeline to run every day at 08:00
schedule.every().day.at("08:00").do(daily_pipeline)

print("Scheduler running. Waiting for 08:00...")

# Keep the script alive; check for pending jobs every 60 seconds
while True:
    schedule.run_pending()
    time.sleep(60)