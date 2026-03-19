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
        dup = df['Index'].duplicated().any()
        if dup is True:
            print("There are duplicates in the data set")
        else:
            print("No duplicates")
        print("Loading dataset of dimensions", df.shape)
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

def main():
    """Test of reading data and print it."""

    try:
        argv = sys.argv
        assert len(argv) == 2, "\033[33mWrong argument number. Usage: python3 describe.py <path_csv>\033[0m"

        pd.set_option('display.float_format', '{:.6f}'.format)
        df = load(argv[1])
        if df is None:
            sys.exit(1)
        print(df.describe())

    except KeyboardInterrupt:
        print("\033[33mStopped by user.\033[0m")
        sys.exit(1)

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
