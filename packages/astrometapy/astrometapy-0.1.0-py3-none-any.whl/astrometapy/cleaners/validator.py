from astrometapy.utils.logger import get_logger

logger = get_logger(__name__)

def validate_fits_keywords(header: dict, required_keywords: list = None):
    """
    Validate a FITS header for required keywords.

    Parameters:
        header (dict): FITS header dictionary.
        required_keywords (list, optional): List of required keywords.
            Defaults to ['RA', 'DEC', 'DATE-OBS'].

    Returns:
        tuple: (bool, list) where bool indicates if header is valid,
               and list contains any missing keywords.
    """
    if required_keywords is None:
        required_keywords = ['RA', 'DEC', 'DATE-OBS']

    missing = [key for key in required_keywords if key not in header]
    valid = len(missing) == 0

    if valid:
        logger.info("All required FITS keywords are present.")
    else:
        logger.warning(f"Missing FITS keywords: {missing}")

    return valid, missing
