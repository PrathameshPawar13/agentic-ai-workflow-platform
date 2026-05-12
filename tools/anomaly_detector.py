import pandas as pd


def detect_anomalies_iqr(df: pd.DataFrame) -> list:
    """
    Detect numeric anomalies using the IQR method.
    """
    anomalies = []
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()

    for column in numeric_columns:
        q1 = df[column].quantile(0.25)
        q3 = df[column].quantile(0.75)
        iqr = q3 - q1

        lower_bound = q1 - 1.5 * iqr
        upper_bound = q3 + 1.5 * iqr

        outlier_rows = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

        for index, row in outlier_rows.iterrows():
            anomalies.append({
                "row_index": int(index),
                "column": column,
                "value": float(row[column]),
                "lower_bound": float(lower_bound),
                "upper_bound": float(upper_bound),
                "method": "IQR"
            })

    return anomalies