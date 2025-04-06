from astropy.table import Table
import pandas as pd

def export_to_votable(data, output_path: str):
    """
    Export data to a VOtable file.

    Parameters:
        data (pd.DataFrame or astropy.table.Table): Data to export.
        output_path (str): File path for the VOtable.
    """
    try:
        from astropy.table import Table
    except ImportError:
        raise ImportError("astropy is required for VOtable export.")
    
    if hasattr(data, "to_table"):
        table = data.to_table()
    elif isinstance(data, Table):
        table = data
    else:
        if isinstance(data, pd.DataFrame):
            table = Table.from_pandas(data)
        else:
            raise ValueError("Data format not recognized for VOtable export.")
    
    table.write(output_path, format='votable', overwrite=True)
