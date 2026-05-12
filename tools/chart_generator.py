import os
import pandas as pd
import matplotlib.pyplot as plt


def generate_charts(df: pd.DataFrame, output_dir: str = "outputs/charts") -> list:
    """
    Generate simple trend charts for numeric columns.
    """
    os.makedirs(output_dir, exist_ok=True)

    chart_paths = []
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    for column in numeric_columns:
        plt.figure()
        df[column].plot(kind="line", title=f"{column} Trend")
        plt.xlabel("Index")
        plt.ylabel(column)

        chart_path = os.path.join(output_dir, f"{column}_trend.png")
        plt.savefig(chart_path, bbox_inches="tight")
        plt.close()

        chart_paths.append(chart_path)

    return chart_paths