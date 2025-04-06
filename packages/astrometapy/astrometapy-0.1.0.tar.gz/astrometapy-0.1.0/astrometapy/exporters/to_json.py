import json
from astrometapy.utils.logger import get_logger

logger = get_logger(__name__)

def export_to_json(data, output_path: str):
    """
    Export data to a JSON file.

    Parameters:
        data (dict): Data to export.
        output_path (str): File path for output JSON.

    Raises:
        IOError: If the file cannot be written.
    """
    try:
        with open(output_path, 'w') as f:
            json.dump(data, f, indent=4)
        logger.info(f"Data successfully exported to JSON at {output_path}")
    except Exception as e:
        logger.error(f"Failed to export data to JSON at {output_path}: {e}")
        raise IOError(f"Failed to export data to JSON: {e}")
