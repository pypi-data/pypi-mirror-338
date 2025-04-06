import pandas as pd
from astrometapy.utils.logger import get_logger

logger = get_logger(__name__)

def unify_catalog_columns(df: pd.DataFrame) -> pd.DataFrame:
    """
    Unify column names of a catalog DataFrame according to a standard mapping.

    Parameters:
        df (pd.DataFrame): Input DataFrame with original column names.

    Returns:
        pd.DataFrame: DataFrame with unified column names.
    """
    mapping = {
        'ra': 'RA',
        'RAJ2000': 'RA',
        'dec': 'DEC',
        'DECJ2000': 'DEC',
    }
    original_columns = df.columns.tolist()
    df = df.rename(columns=lambda col: mapping.get(col, col))
    updated_columns = df.columns.tolist()
    
    logger.info(f"Original columns: {original_columns}")
    logger.info(f"Unified columns: {updated_columns}")
    
    return df
