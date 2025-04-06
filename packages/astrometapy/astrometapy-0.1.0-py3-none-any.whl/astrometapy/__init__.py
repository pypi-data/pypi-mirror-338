# astrometapy/__init__.py

__version__ = "0.1.0"

# Optionally, expose some key functions or submodules
from .readers import fits_reader, votable_reader, catalog_reader
from .cleaners import schema_unifier, validator
from .exporters import to_csv, to_json, to_votable
