import os
import setuptools

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setuptools.setup(
    name = "geoname_enrichment",
    version = "0.1.0",
    url = "https://github.com/metabelgica/geoname-enrichment",
    author = "Sven Lieber",
    author_email = "Sven.Lieber@kbr.be",
    description = ("A Python script to enrich placenames in a CSV file with geoname data from a custom API."),
    license = "MIT",
    keywords = "geonames CSV",
    packages=setuptools.find_packages(),
    long_description_content_type = "text/markdown",
    long_description=read('README.md')
)
