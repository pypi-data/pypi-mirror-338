# AstroMetaPy

AstroMetaPy is a Python package designed to streamline the handling of astronomical metadata. It provides tools to:

- Read metadata from FITS files, VO tables, and catalogs.
- Clean and validate metadata against standard schemas.
- Export metadata in various formats (CSV, JSON, VOtable).

## Installation

You can install AstroMetaPy via pip:

```bash
pip install astrometapy
```

## Usage

### Command Line Interface

After installation, you can run the CLI:

```bash
astrometapy read-fits path/to/file.fits --output header.json
```

### Programmatic Usage

```python
from astrometapy.readers import fits_reader

header = fits_reader.load_fits_header("path/to/file.fits")
print(header)
```

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License.