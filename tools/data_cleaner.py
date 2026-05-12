import pandas as pd


def summarize_missing_values(df: pd.DataFrame) -> dict:
    """
    Return missing value count per column.
    """
    return df.isnull().sum().to_dict()


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Basic cleaning:
    - Fill numeric missing values with median.
    - Fill categorical missing values with mode or 'Unknown'.
    """
    cleaned_df = df.copy()

    for column in cleaned_df.columns:
        if cleaned_df[column].isnull().sum() == 0:
            continue

        if cleaned_df[column].dtype.kind in "biufc":
            cleaned_df[column] = cleaned_df[column].fillna(cleaned_df[column].median())
        else:
            mode_values = cleaned_df[column].mode()
            fill_value = mode_values.iloc[0] if not mode_values.empty else "Unknown"
            cleaned_df[column] = cleaned_df[column].fillna(fill_value)

    return cleaned_df