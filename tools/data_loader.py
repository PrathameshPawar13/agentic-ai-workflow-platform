import pandas as pd


def load_csv(file_path: str) -> pd.DataFrame:
    """
    Load a CSV file into a pandas DataFrame.
    """
    try:
        return pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Failed to load CSV file: {str(e)}")