import pandas as pd


def generate_statistics(df: pd.DataFrame) -> dict:
    """
    Generate descriptive statistics for numeric columns.
    """
    numeric_df = df.select_dtypes(include=["number"])

    if numeric_df.empty:
        return {}

    stats = numeric_df.describe().to_dict()

    clean_stats = {}
    for column, values in stats.items():
        clean_stats[column] = {
            key: float(value)
            for key, value in values.items()
        }

    return clean_stats