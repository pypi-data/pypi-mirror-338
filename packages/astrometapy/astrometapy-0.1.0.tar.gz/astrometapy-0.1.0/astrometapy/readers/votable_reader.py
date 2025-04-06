from astropy.io import votable

def load_votable(filepath: str):
    """
    Load and return a VOtable from a file.

    Parameters:
        filepath (str): Path to the VOtable file.

    Returns:
        VOTable: Parsed VOtable object.
    """
    votable_data = votable.parse(filepath)
    return votable_data
