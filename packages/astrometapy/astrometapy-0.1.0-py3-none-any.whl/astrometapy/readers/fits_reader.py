import os
from astropy.io import fits
from astrometapy.utils.logger import get_logger

logger = get_logger(__name__)

def load_fits_header(filepath: str) -> dict:
    """
    Load and return the header from a FITS file.

    Parameters:
        filepath (str): Path to the FITS file.

    Returns:
        dict: FITS header as a dictionary.

    Raises:
        FileNotFoundError: If the file does not exist.
        IOError: If the file is not a valid FITS file.
    """
    if not os.path.exists(filepath):
        logger.error(f"File not found: {filepath}")
        raise FileNotFoundError(f"File not found: {filepath}")
    
    try:
        with fits.open(filepath) as hdul:
            header = hdul[0].header
            logger.info(f"Successfully loaded header from {filepath}")
            return dict(header)
    except Exception as e:
        logger.error(f"Error reading FITS file {filepath}: {e}")
        raise IOError(f"Error reading FITS file {filepath}: {e}")
