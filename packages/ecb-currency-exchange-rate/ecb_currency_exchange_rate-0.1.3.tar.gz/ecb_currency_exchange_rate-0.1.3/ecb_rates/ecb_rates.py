import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import requests
import logging
import os

# Set up logging configuration
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

namespaces = {'xmlns': 'http://www.ecb.int/vocabulary/2002-08-01/eurofxref'}
ecb_hist_rate_url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-hist.xml'
xml_file = f"eurofxref-hist-{datetime.today().strftime('%Y-%m-%d')}.xml"

def get_existing_xml_file():
    """Finds the latest existing eurofxref XML file in the current directory."""
    for file in os.listdir():
        if file.startswith("eurofxref-hist-") and file.endswith(".xml"):
            return file
    return None

def fetch_rates():
    """
    Downloads the latest historical exchange rate data from the ECB and saves it to a new dated XML file.
    Removes the previous XML file if found.
    """
    old_file = get_existing_xml_file()
    if old_file:
        os.remove(old_file)
        logging.info(f"Removed old file: {old_file}")

    logging.info(f"Downloading {xml_file}...")
    try:
        response = requests.get(ecb_hist_rate_url, stream=True)
        response.raise_for_status()

        with open(xml_file, "wb") as file:
            for chunk in response.iter_content(1024):
                file.write(chunk)
        
        logging.info(f"Downloaded and saved as {xml_file} successfully.")
    except requests.RequestException as e:
        logging.error(f"Failed to download {xml_file}. Error: {e}")

def update_historical_rates():
    """
    Checks if the latest XML file for today exists; if not, downloads a new one.
    """
    existing_file = get_existing_xml_file()
    if existing_file == xml_file:
        return
    
    logging.info("Today's exchange rate file not found. Fetching new rate file.")
    fetch_rates()

def get_exchange_rate(date, from_currency, to_currency):
    """
    Retrieves the exchange rate for the given date and currencies from the ECB historical XML file.
    If the date falls on a weekend or holiday, it uses the last available rate.

    :param date: Date in 'YYYY-MM-DD' format.
    :param from_currency: The base currency (e.g., 'USD').
    :param to_currency: The target currency (e.g., 'EUR').
    :return: Exchange rate as a float or None if not found.
    """
    update_historical_rates()

    try:
        tree = ET.parse(xml_file)
        root = tree.getroot()

        # Convert date to datetime format
        date_obj = datetime.strptime(date, "%Y-%m-%d")
        
        available_dates = sorted(
            [cube.attrib['time'] for cube in root.findall(".//xmlns:Cube/xmlns:Cube[@time]", namespaces)],
            reverse=True
        )
        
        while date_obj.strftime("%Y-%m-%d") not in available_dates:
            date_obj -= timedelta(days=1)  # Move to the previous day
        
        date_str = date_obj.strftime("%Y-%m-%d")

        for cube_time in root.findall(".//xmlns:Cube/xmlns:Cube[@time]", namespaces):
            if cube_time.attrib['time'] == date_str:
                rates = {rate.attrib['currency']: float(rate.attrib['rate']) for rate in cube_time.findall("xmlns:Cube", namespaces)}

                if from_currency == 'EUR':
                    return rates.get(to_currency)  # Return rate directly if from EUR
                elif to_currency == 'EUR':
                    return 1 / rates.get(from_currency) if rates.get(from_currency) else None
                elif from_currency in rates and to_currency in rates:
                    return rates[to_currency] / rates[from_currency]  # Cross-rate conversion

        logging.warning(f"Exchange rate for {from_currency} to {to_currency} on {date_str} not found.")
        return None

    except FileNotFoundError:
        logging.error(f"{xml_file} not found. Please fetch the latest data first.")
    except ET.ParseError:
        logging.error(f"Error parsing the XML file {xml_file}. Please check the file integrity.")
    except Exception as e:
        logging.error(f"An unexpected error occurred while retrieving the exchange rate: {e}")
    
    return None  # Return None if no rate found or an error occurs
