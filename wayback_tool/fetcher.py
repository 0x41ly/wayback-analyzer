import requests
from wayback_tool.db.db_operations import DBOperations
from wayback_tool.db.db_handler import MongoHandler
from wayback_tool.utils import logger

# Initialize DB handler and operations (only used here for fetching and saving data)
mongo_handler = MongoHandler()
db_operations = DBOperations(mongo_handler)

def fetch_wayback_urls(domain):
    """
    Fetches URLs for the given domain from the Wayback Machine using its CDX API.

    Args:
        domain (str): The domain to fetch URLs for (e.g., example.com).

    Returns:
        list: A list of URLs fetched from the Wayback Machine.
    """
    # Construct the Wayback Machine CDX API URL for the given domain
    url = f"https://web.archive.org/cdx/search/cdx?url={domain}/*&output=text&fl=original&collapse=urlkey"
    
    try:
        # Log the request attempt
        logger.info(f"Fetching URLs for domain: {domain}")

        # Send the GET request to the Wayback Machine API
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Split the response into individual URLs (one per line)
        urls = response.text.strip().splitlines()

        # Log the number of URLs fetched
        logger.info(f"Fetched {len(urls)} URLs for domain: {domain}")
        
        # Return the list of URLs
        return urls

    except requests.RequestException as e:
        # Log the error with details
        logger.error(f"Error fetching URLs for {domain}: {e}")
        return []

def fetch_urls_and_save_to_db(domain: str):
    """
    Fetches URLs from the Wayback Machine and saves them into the database.
    
    Args:
        domain (str): The domain to fetch URLs for and save to the database.
    """
    # Step 1: Fetch URLs from the Wayback Machine
    urls = fetch_wayback_urls(domain)

    if not urls:
        return

    # Step 2: Save the URLs to the database
    db_operations.save_endpoints(domain, urls)
    logger.info(f"Saved {len(urls)} URLs for domain: {domain} into the database.")
