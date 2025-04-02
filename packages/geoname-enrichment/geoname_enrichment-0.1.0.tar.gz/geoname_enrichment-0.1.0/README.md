# Geoname Enrichment

This Python script reads placenames from CSV files and queries a custom API on top of geonames data to enrich the geoname identifier. The API and geonames database are available under Open Licenses at:

- [Geonames Lookup API](https://github.com/kbrbe/geonames-lookup) [![DOI](https://zenodo.org/badge/14883863.svg)](https://zenodo.org/badge/latestdoi/14883863)
- [Geonames MySQL database](https://github.com/GeoNames-MySQL-DataImport) [![DOI](https://zenodo.org/badge/14883685.svg)](https://zenodo.org/badge/latestdoi/14883685)

## Usage via the command line

Create and activate a Python virtual environment
```bash

# Create a new Python virtual environment
python3 -m venv py-geo-env

# Activate the virtual environment
source py-geo-env/bin/activate

# Install dependencies
pip -r requirements.txt

# install the tool
pip install .
```

Available options

```
usage: geoname_enrichment.py [-h] -c CONFIG_FILE -p PLACENAME_COLUMN
                             --countryname-column COUNTRYNAME_COLUMN
                             --id-column ID_COLUMN -o OUTPUT_FILE
                             [-l LOG_FILE] [-L LOG_LEVEL]
                             inputFile

This script reads names of places, possibly in combination with countries, and
looks up the values in a local geonames-based API

positional arguments:
  inputFile             The input file containing CSV records

optional arguments:
  -h, --help            show this help message and exit
  -c CONFIG_FILE, --config-file CONFIG_FILE
                        The config file with instructions how to enrich the
                        location data
  -p PLACENAME_COLUMN, --placename-column PLACENAME_COLUMN
                        The name of the column in the input CSV that contains
                        the name of the place
  --countryname-column COUNTRYNAME_COLUMN
                        The name of the column in the input CSV that contains
                        the country name
  --id-column ID_COLUMN
                        The name of the column in the input CSV that contains
                        the row identifier
  -o OUTPUT_FILE, --output-file OUTPUT_FILE
                        The output CSV file containing descriptive keys based
                        on the key composition config
  -l LOG_FILE, --log-file LOG_FILE
                        The optional name of the logfile
  -L LOG_LEVEL, --log-level LOG_LEVEL
                        The log level, default is INFO
```
