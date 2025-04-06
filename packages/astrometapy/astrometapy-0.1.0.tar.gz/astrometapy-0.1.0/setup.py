import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="astrometapy",
    version="0.1.0",
    author="Whiteflakes",
    author_email="whiteflakesdev@gmail.com",
    description="A Python package for reading, cleaning, and exporting astronomical metadata.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/whiteflakes/astrometapy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    install_requires=[
        "astropy",
        "pandas",
        "jsonschema",
        "typer",
    ],
    entry_points={
        "console_scripts": [
            "astrometapy=astrometapy.cli:main"
        ]
    },
)
