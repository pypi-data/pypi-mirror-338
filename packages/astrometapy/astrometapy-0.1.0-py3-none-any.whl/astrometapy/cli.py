import typer
from astrometapy.readers import fits_reader
from astrometapy.exporters import to_json
from astrometapy.cleaners import validator

app = typer.Typer()

@app.command()
def read_fits(file: str, output: str = None):
    """
    Read FITS metadata from a file and optionally export as JSON.
    """
    header = fits_reader.load_fits_header(file)
    typer.echo("FITS Header:")
    for key, val in header.items():
        typer.echo(f"{key}: {val}")

    # Validate header (example check)
    valid, missing = validator.validate_fits_keywords(header)
    if not valid:
        typer.echo("Missing required keywords: " + ", ".join(missing))
    else:
        typer.echo("All required keywords are present.")

    if output:
        to_json.export_to_json(header, output)
        typer.echo(f"Header exported to {output}")

def main():
    app()

if __name__ == "__main__":
    main()
