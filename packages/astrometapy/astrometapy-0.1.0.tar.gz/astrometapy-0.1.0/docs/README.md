# AstroMetaPy Documentation

Welcome to the **AstroMetaPy** documentation. This guide covers everything you need to get started, use the package’s functionality, and even contribute to its development.

---

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [Module Overview](#module-overview)
  - [Command Line Interface (CLI)](#command-line-interface-cli)
  - [Readers](#readers)
    - [FITS Reader](#fits-reader)
    - [VOtable Reader](#votable-reader)
    - [Catalog Reader](#catalog-reader)
  - [Cleaners](#cleaners)
    - [Schema Unifier](#schema-unifier)
    - [Validator](#validator)
  - [Exporters](#exporters)
    - [CSV Exporter](#csv-exporter)
    - [JSON Exporter](#json-exporter)
    - [VOtable Exporter](#votable-exporter)
  - [Utilities](#utilities)
- [Examples and Tutorials](#examples-and-tutorials)
- [Contributing](#contributing)
- [Roadmap](#roadmap)
- [License](#license)
- [FAQ](#faq)

---

## Introduction

**AstroMetaPy** is a Python package designed to simplify the process of handling astronomical metadata. It provides tools to:
- **Read** metadata from various formats such as FITS files, VO tables, and CSV catalogs.
- **Clean and validate** metadata using industry standards.
- **Export** metadata to multiple formats, including CSV, JSON, and VOtable.

The package is aimed at astronomers, astrophysics researchers, and developers who need to streamline metadata processing in their workflows.

---

## Installation

AstroMetaPy is available via PyPI. Install it using pip:

```bash
pip install astrometapy
```

For development purposes, clone the repository and install dependencies with:

```bash
git clone https://github.com/yourusername/astrometapy.git
cd astrometapy
pip install -e .
```

---

## Quick Start

Once installed, you can use AstroMetaPy both from the command line and programmatically.

### Command Line Interface (CLI)

To read a FITS file and export its header to JSON:

```bash
astrometapy read-fits path/to/your_file.fits --output header.json
```

This command loads the FITS header, validates it, and exports it to a JSON file if requested.

### Programmatic Usage

Example Python script to load and validate a FITS header:

```python
from astrometapy.readers import fits_reader
from astrometapy.cleaners import validator

# Load FITS header
header = fits_reader.load_fits_header("path/to/your_file.fits")

# Validate header keywords
is_valid, missing = validator.validate_fits_keywords(header)
if is_valid:
    print("Header is valid!")
else:
    print(f"Missing keywords: {missing}")
```

---

## Module Overview

### Command Line Interface (CLI)

The CLI is built using Typer. It provides a simple command to access the package’s functionalities:

- **Command:** `read_fits`
- **Usage:** Reads a FITS file, prints the header, validates it, and optionally exports the header to JSON.

For more details, check the `astrometapy/cli.py` file.

---

### Readers

AstroMetaPy offers multiple modules to read different types of astronomical metadata.

#### FITS Reader

- **File:** `astrometapy/readers/fits_reader.py`
- **Function:** `load_fits_header(filepath: str) -> dict`
- **Description:** Loads a FITS file’s header using `astropy.io.fits`.  
- **Enhanced Features:**
  - Checks for file existence.
  - Catches errors during file reading.
  - Logs key events.

*Usage Example:*

```python
from astrometapy.readers import fits_reader
header = fits_reader.load_fits_header("file.fits")
```

#### VOtable Reader

- **File:** `astrometapy/readers/votable_reader.py`
- **Function:** `load_votable(filepath: str)`
- **Description:** Uses Astropy’s VOtable module to parse VOtable files.

*Usage Example:*

```python
from astrometapy.readers import votable_reader
votable_data = votable_reader.load_votable("file.xml")
```

#### Catalog Reader

- **File:** `astrometapy/readers/catalog_reader.py`
- **Function:** `load_catalog(filepath: str) -> pd.DataFrame`
- **Description:** Reads catalog data (e.g., CSV) into a Pandas DataFrame.

*Usage Example:*

```python
from astrometapy.readers import catalog_reader
df = catalog_reader.load_catalog("catalog.csv")
```

---

### Cleaners

These modules ensure that metadata conforms to expected standards.

#### Schema Unifier

- **File:** `astrometapy/cleaners/schema_unifier.py`
- **Function:** `unify_catalog_columns(df: pd.DataFrame) -> pd.DataFrame`
- **Description:** Standardizes column names in catalog data using a predefined mapping.

*Usage Example:*

```python
from astrometapy.cleaners import schema_unifier
df_unified = schema_unifier.unify_catalog_columns(df)
```

#### Validator

- **File:** `astrometapy/cleaners/validator.py`
- **Function:** `validate_fits_keywords(header: dict, required_keywords: list = None)`
- **Description:** Validates that the FITS header contains the required keywords (default: 'RA', 'DEC', 'DATE-OBS').
- **Enhanced Features:**
  - Logs validation results.
  - Returns a tuple of validation status and missing keywords.

*Usage Example:*

```python
from astrometapy.cleaners import validator
is_valid, missing = validator.validate_fits_keywords(header)
```

---

### Exporters

These modules allow exporting metadata into various formats.

#### CSV Exporter

- **File:** `astrometapy/exporters/to_csv.py`
- **Function:** `export_to_csv(data, output_path: str)`
- **Description:** Exports data (dictionary or DataFrame) to a CSV file.
- **Enhanced Features:**
  - Checks input data type.
  - Logs successful export or errors.

*Usage Example:*

```python
from astrometapy.exporters import to_csv
to_csv.export_to_csv(header, "header.csv")
```

#### JSON Exporter

- **File:** `astrometapy/exporters/to_json.py`
- **Function:** `export_to_json(data, output_path: str)`
- **Description:** Exports a dictionary to a JSON file with formatted output.
- **Enhanced Features:**
  - Logs operations and errors.

*Usage Example:*

```python
from astrometapy.exporters import to_json
to_json.export_to_json(header, "header.json")
```

#### VOtable Exporter

- **File:** `astrometapy/exporters/to_votable.py`
- **Function:** `export_to_votable(data, output_path: str)`
- **Description:** Exports data to a VOtable file. Supports Pandas DataFrames and Astropy Tables.
- **Enhanced Features:**
  - Converts data formats as needed.
  - Logs the export process.

*Usage Example:*

```python
from astrometapy.exporters import to_votable
to_votable.export_to_votable(df, "catalog.xml")
```

---

### Utilities

#### Logger

- **File:** `astrometapy/utils/logger.py`
- **Function:** `get_logger(name: str = __name__)`
- **Description:** Provides a standardized logger that outputs timestamps, module names, and log levels.

*Usage Example:*

```python
from astrometapy.utils import logger
log = logger.get_logger(__name__)
log.info("This is an info message.")
```

---

## Examples and Tutorials

To help you get started quickly, here are a few example scripts:

### Example 1: Reading and Validating a FITS File

```python
from astrometapy.readers import fits_reader
from astrometapy.cleaners import validator

file_path = "example.fits"
header = fits_reader.load_fits_header(file_path)
valid, missing = validator.validate_fits_keywords(header)

if valid:
    print("FITS header is complete.")
else:
    print(f"Missing keywords: {missing}")
```

### Example 2: Converting Catalog Data

```python
import pandas as pd
from astrometapy.readers import catalog_reader
from astrometapy.cleaners import schema_unifier
from astrometapy.exporters import to_csv, to_json

# Read catalog CSV
df = catalog_reader.load_catalog("catalog.csv")

# Unify column names
df_unified = schema_unifier.unify_catalog_columns(df)

# Export unified data
to_csv.export_to_csv(df_unified, "unified_catalog.csv")
to_json.export_to_json(df_unified.to_dict(orient='list'), "unified_catalog.json")
```

---

## Contributing

We welcome contributions to improve AstroMetaPy. If you’d like to contribute:

1. Fork the repository.
2. Create a feature branch.
3. Write tests for your changes.
4. Submit a pull request with a clear description of your changes.

For more details, see the [CONTRIBUTING.md](CONTRIBUTING.md) file.

---

## Roadmap

Future features and improvements include:

- Enhanced support for additional astronomical data formats.
- Integration with VO services via the `pyvo` library.
- A more extensive CLI with additional commands.
- Sphinx-based documentation with examples.
- Advanced validation using `jsonschema`.

Feel free to open issues or submit proposals for features.

---

## License

AstroMetaPy is released under the [MIT License](LICENSE).

---

## FAQ

**Q:** What versions of Python does AstroMetaPy support?  
**A:** AstroMetaPy supports Python 3.7 and above.

**Q:** How do I report a bug or request a feature?  
**A:** Please open an issue on our GitHub repository.

**Q:** Can I contribute documentation improvements?  
**A:** Absolutely! We welcome any improvements in documentation as well as code.

---

This documentation serves as a starting point and will evolve as the project grows. Please refer to the GitHub repository for the latest updates and additional resources.

