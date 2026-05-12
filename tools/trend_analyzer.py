import pandas as pd
import numpy as np


def classify_trend(slope: float, values: pd.Series) -> str:
    """
    Classify trend direction using slope relative to data variability.
    """
    value_range = values.max() - values.min()

    if value_range == 0:
        return "stable"

    normalized_slope = slope / value_range

    if normalized_slope > 0.05:
        return "increasing"
    if normalized_slope > 0.01:
        return "slightly increasing"
    if normalized_slope < -0.05:
        return "decreasing"
    if normalized_slope < -0.01:
        return "slightly decreasing"

    return "stable"


def analyze_trends(df: pd.DataFrame) -> dict:
    """
    Analyze simple linear trends for numeric columns using row index as x-axis.
    """
    trends = {}
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    if df.empty:
        return trends

    x = np.arange(len(df))

    for column in numeric_columns:
        y = df[column].astype(float).values

        if len(y) < 2:
            trends[column] = {
                "slope": 0.0,
                "direction": "insufficient_data"
            }
            continue

        slope, _ = np.polyfit(x, y, 1)

        trends[column] = {
            "slope": float(slope),
            "direction": classify_trend(float(slope), df[column])
        }

    return trends