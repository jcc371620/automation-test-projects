import pandas as pd
import matplotlib.pyplot as plt
import os

def auto_plot(df, output_dir="./charts"):
    """
    Automatically generate and save charts for every numeric column:
    - Histogram: shows value distribution
    - Box plot: highlights median, spread, and outliers
    Charts are saved as PNG files, one per column.
    """
    # Create the output directory if it doesn't already exist
    os.makedirs(output_dir, exist_ok=True)

    # Select only numeric columns (skip text/categorical columns)
    numeric_cols = df.select_dtypes(include='number').columns

    for col in numeric_cols:
        # Create a figure with two side-by-side subplots
        fig, axes = plt.subplots(1, 2, figsize=(12, 4))
        fig.suptitle(f"Column: {col}", fontsize=14, fontweight='bold')

        # Left plot: histogram to see the overall distribution shape
        df[col].hist(ax=axes[0], bins=30, color='steelblue', edgecolor='white')
        axes[0].set_title("Distribution (Histogram)")
        axes[0].set_xlabel(col)
        axes[0].set_ylabel("Frequency")

        # Right plot: box plot to spot outliers and see the IQR
        df[col].plot(kind='box', ax=axes[1], patch_artist=True,
                     boxprops=dict(facecolor='lightblue'))
        axes[1].set_title("Spread (Box Plot)")

        # Save the figure and close it to free memory
        chart_path = os.path.join(output_dir, f"{col}.png")
        plt.tight_layout()
        plt.savefig(chart_path, dpi=150)
        plt.close()
        print(f"Saved chart: {chart_path}")

    print(f"\nAll charts saved to: {output_dir}/")