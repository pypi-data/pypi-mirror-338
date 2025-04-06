import pandas as pd
from astrometapy.utils.logger import get_logger

logger = get_logger(__name__)

def export_to_csv(data, output_path: str):
    """
    Export data to a CSV file.

    Parameters:
        data (dict or pd.DataFrame): Data to export.
        output_path (str): File path for output CSV.

    Raises:
        ValueError: If the data is neither a dict nor a DataFrame.
        IOError: If saving to CSV fails.
    """
    try:
        if isinstance(data, dict):
            df = pd.DataFrame([data])
        elif isinstance(data, pd.DataFrame):
            df = data
        else:
            logger.error("Data must be a dict or a pandas DataFrame.")
            raise ValueError("Data must be a dict or a pandas DataFrame.")
        
        df.to_csv(output_path, index=False)
        logger.info(f"Data successfully exported to CSV at {output_path}")
    except Exception as e:
        logger.error(f"Error exporting data to CSV at {output_path}: {e}")
        raise IOError(f"Error exporting data to CSV: {e}")
