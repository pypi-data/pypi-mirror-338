import pandas as pd

def load_catalog(filepath: str):
    """
    Load a catalog from a CSV file into a DataFrame.

    Parameters:
        filepath (str): Path to the catalog CSV file.

    Returns:
        pd.DataFrame: DataFrame containing the catalog data.
    """
    df = pd.read_csv(filepath)
    return df
