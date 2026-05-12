import pandas as pd
from app.schemas import DatasetSummary


def inspect_schema(df: pd.DataFrame) -> DatasetSummary:
    """
    Inspect dataset schema and return a structured summary.
    """
    numeric_columns = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_columns = df.select_dtypes(exclude=["number"]).columns.tolist()

    return DatasetSummary(
        rows=df.shape[0],
        columns=df.shape[1],
        column_names=df.columns.tolist(),
        numeric_columns=numeric_columns,
        categorical_columns=categorical_columns,
    )