#
# (c) 2024 Sven Lieber
# KBR Brussels
#
#import re
import os
import json
import logging
import requests
#import enchant
#import hashlib
import csv
from argparse import ArgumentParser
from tqdm import tqdm
from dotenv import load_dotenv
import geoname_enrichment.csv_logger as csv_logger
from geoname_enrichment.csv_logger import CSVFileHandler
import geoname_enrichment.utils as utils
#import stdnum

LOGGER_NAME = "GEONAME_ENRICHMENT"
logger = logging.getLogger(LOGGER_NAME)


# -----------------------------------------------------------------------------
def main(inputFilename, configFilename, idColumn, placenameColumn, countrynameColumn, outputFilename, logLevel='INFO', logFile=None):

  # read the config file
  #
  with open(configFilename, 'r') as configFile:
    config = json.load(configFile)  

  # load environment variables from .env file
  load_dotenv()

  verificationCertFilename = os.getenv('API_ROOT_CERTIFICATE')
  verificationCertNeeded = True if verificationCertFilename else False
  
  setupLogging(logLevel, logFile)

  # count number of input rows so we can show a progress bar
  # do not count the header
  with open(inputFilename, 'r') as inFile:
    numberRows = sum(1 for row in inFile) - 1

  with open(inputFilename, 'r') as inFile, \
       open(outputFilename, 'w') as outFile:

    inputReader = csv.DictReader(inFile)

    outputFields = [idColumn, 'geonameID', 'placename', 'countryCode']
    outputWriter = csv.DictWriter(outFile, fieldnames=outputFields, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    outputWriter.writeheader()

    enrichedCounter = 0
    multipleAPIResultsCounter = 0
    nothingFoundCounter = 0
    invalidPlacenameCounter = 0
    errorCounter = 0
    mappingFixedMultipleResultsCounter = 0
    pbar = tqdm(inputReader, total=numberRows)

    for row in pbar:

      pbar.set_description(f'#enriched: {enrichedCounter}; #multipleAPIResults: {multipleAPIResultsCounter} (resolved {mappingFixedMultipleResultsCounter}); #nothingFound: {nothingFoundCounter}; #invalidPlacename: {invalidPlacenameCounter}, #errors {errorCounter}')
      rowID = row[idColumn]
      placenameString = row[placenameColumn]

      if utils.needs_encoding_fixing(placenameString):
        placenameString = utils.fix_encoding(placenameString)
      placename = placenameString.strip() if '(' not in placenameString else placenameString.split('(')[0].strip()

      # for KMSKB data
      placename = placename.replace('[dut]','')
      placename = placename.split(',')[0] if ',' in placename else placename
      placename = placename.split(' / ')[0] if ' / ' in placename else placename


      if placenameString.startswith('-'):
        logger.warning(f'Invalid placename ({rowID}): "{placenameString}"', extra={'identifier': rowID, 'message_type': csv_logger.MESSAGE_TYPES['INVALID_VALUE']})
        invalidPlacenameCounter += 1
        pbar.update()
        continue


      countryNameString = row[countrynameColumn]

      if placenameString == '' and countryNameString == '':
        logger.warning(f'Empty place and country name ({rowID})', extra={'identifier': rowID})
        continue
      elif placenameString == '':
        logger.warning(f'Empty placename ({rowID}), only country provided ({countryNameString})', extra={'identifier': rowID})
        continue

      if utils.needs_encoding_fixing(countryNameString):
        countryNameString = utils.fix_encoding(countryNameString)
      placename = placenameString.strip() if '(' not in placenameString else placenameString.split('(')[0].strip()
      countryName = countryNameString if countryNameString else config["defaultCountry"]
 
      # perform the actual API request
      #
      requestURL = f'{config["apiURL"]}?{config["apiParameterPlace"]}={placename}&{config["apiParameterCountry"]}={countryName}'
      logger.debug(f'request: {requestURL}')
      try:
        if verificationCertNeeded:
          response = requests.get(requestURL, verify=verificationCertFilename)
        else:
          response = requests.get(requestURL)
        response.raise_for_status()

        res = response.json()
        if len(res) > 1:
          resultIdentifierStrings = []
          resultStrings = []
          for r in res:
            resultIdentifierStrings.append(f'{r["geonameId"]}')
            resultStrings.append(f'{r["name"]} ({r["country"]}, {r["geonameId"]}, population: {r["population"]})')

          logger.debug(f'multiple API results: {resultStrings}')
          foundIdentifiers = ', '.join(resultIdentifierStrings)
          if foundIdentifiers in config["hardcodedMappings"]:
            identifierFromMapping = config["hardcodedMappings"][foundIdentifiers][0]

            # take the result that matches with the provided identifier from the hardcoded mapping
            # comparison should properly compare string values, not string and int (https://github.com/MetaBelgica/geoname-enrichment-issues/1)
            matchedResult = next((item for item in res if str(item['geonameId']) == identifierFromMapping), None)
            geonameId, geonamePlacename, geonameCountryCode = getGeonameOutput(matchedResult, config)

            outputWriter.writerow({idColumn: rowID, "geonameID": geonameId, "placename": geonamePlacename, "countryCode": geonameCountryCode})
            mappingFixedMultipleResultsCounter += 1
            logger.warning(f'Multiple API results resolved for "{placename} ({countryName})" ({rowID}): ' +  f'chosen "{geonamePlacename} ({geonameCountryCode},{geonameId})" from ' + ', '.join(resultStrings) + f' based on mapping {identifierFromMapping}', extra={'identifier': rowID, 'message_type': csv_logger.MESSAGE_TYPES['MULTIPLE_API_RESULTS']}) 
          else:
            logger.warning(f'More than one API result for "{placename} ({countryName})" ({rowID}): ' + ', '.join(resultStrings), extra={'identifier': rowID, 'message_type': csv_logger.MESSAGE_TYPES['MULTIPLE_API_RESULTS']})
            multipleAPIResultsCounter += 1
        else:
          geonameId, geonamePlacename, geonameCountryCode = getGeonameOutput(res[0], config)
          logger.debug(f'single API result: {geonamePlacename} ({geonameId}))')
          outputWriter.writerow({idColumn: rowID, "geonameID": geonameId, "placename": geonamePlacename, "countryCode": geonameCountryCode})
          enrichedCounter += 1
          
      except requests.exceptions.HTTPError as e:
        logger.error(f'Nothing found for the provided placename ({rowID}): {placename} ({countryName})', extra={'identifier': rowID, 'message_type': csv_logger.MESSAGE_TYPES['EMPTY_API_RESPONSE']})
        nothingFoundCounter += 1
      except Exception as e:
        logger.error(f'API error ({rowID}): ' + str(e), extra={'identifier': rowID})
        errorCounter += 1



# -----------------------------------------------------------------------------
def getGeonameOutput(geonameJson, config):
  """This function takes the JSON object returned from the API and returns the geonames ID, placename and country code."""

  # if we got a single result, take the name in the specified language
  altNames = geonameJson["alternate_names"]
  if config["outputLanguage"] in altNames:
    geonamePlacename = altNames[config["outputLanguage"]][0]
  else:
    geonamePlacename = geonameJson["name"]

  geonameCountryCode = geonameJson["country"] 

  return geonameJson['geonameId'], geonamePlacename, geonameCountryCode
  


# -----------------------------------------------------------------------------
def setupLogging(logLevel, logFile):

  if logFile:
    logger = logging.getLogger(LOGGER_NAME)
    # Debug: Print current handlers
    csvHandler = CSVFileHandler(logFile, logLevel=logLevel, delimiter=',', filemode='w')
    logger.addHandler(csvHandler)
  else:
    logFormat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    logging.basicConfig(level=logLevel, format=logFormat)
    logger = logging.getLogger(LOGGER_NAME)



# -----------------------------------------------------------------------------
def parseArguments():

  parser = ArgumentParser(description='This script reads names of places, possibly in combination with countries, and looks up the values in a local geonames-based API')
  parser.add_argument('inputFile', help='The input file containing CSV records')
  parser.add_argument('-c', '--config-file', action='store', required=True, help='The config file with instructions how to enrich the location data')
  parser.add_argument('-p', '--placename-column', action='store', required=True, help='The name of the column in the input CSV that contains the name of the place')
  parser.add_argument('--countryname-column', action='store', required=True, help='The name of the column in the input CSV that contains the country name')
  parser.add_argument('--id-column', action='store', required=True, help='The name of the column in the input CSV that contains the row identifier')
  parser.add_argument('-o', '--output-file', action='store', required=True, help='The output CSV file containing descriptive keys based on the key composition config')
  parser.add_argument('-l', '--log-file', action='store', help='The optional name of the logfile')
  parser.add_argument('-L', '--log-level', action='store', default='INFO', help='The log level, default is INFO')
  args = parser.parse_args()

  return args


if __name__ == '__main__':
  args = parseArguments()
  main(args.inputFile, args.config_file, args.id_column, args.placename_column, args.countryname_column, args.output_file, logLevel=args.log_level, logFile=args.log_file)
