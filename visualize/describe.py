import pandas as pd
import sys
import os


def load(path: str) -> pd.DataFrame:
    """Load a csv file and return it's pandas.DataFrame object."""

    try:
        assert isinstance(path, str), "Wrong file path type."
        assert os.path.exists(path), "Data file not exists."
        assert path.endswith(".csv"), "Not csv data."

        df = pd.read_csv(path)
        df = df.drop(columns=['Index'])
        numeric_cols = df.select_dtypes(include=['number']).columns
        df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())
        return df

    except AssertionError as e:
        print("AssertionError:", e)
        return None

    except Exception as e:
        print("Error:", e)
        return None
