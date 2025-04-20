import logging
from wayback_tool.cli import get_domain_from_args
from wayback_tool.fetcher import fetch_urls_and_save_to_db
from wayback_tool.parser import parse_endpoints
from wayback_tool.analyzer import analyze_endpoints
from wayback_tool.db.db_operations import DBOperations
from wayback_tool.db.db_handler import MongoHandler

# Initialize the logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize DB handler and operations (only used here for coordination)
mongo_handler = MongoHandler()
db_operations = DBOperations(mongo_handler)

def main():
    # Step 1: Get the domain name from command-line arguments
    domain = get_domain_from_args()

    # Step 2: Fetch URLs from Wayback Machine for the given domain and save them to the DB
    logger.info(f"Fetching URLs for domain: {domain}")
    fetch_urls_and_save_to_db(domain)

    # Step 3: Retrieve and process the URLs from the database
    logger.info("Retrieving URLs from the database...")
    endpoints = db_operations.get_endpoints(domain)

    # Step 4: Parse and analyze each endpoint
    logger.info(f"Parsing and analyzing {len(endpoints)} endpoints...")
    for endpoint in endpoints:
        # Parse parameters for each endpoint
        params = parse_endpoints(endpoint.url)
        db_operations.save_params(domain, params)

        # Analyze the endpoint
        analyze_endpoints(endpoint)

        # Update the process status of the endpoint in the DB
        db_operations.update_process_status(endpoint.url, "processed")

    # Step 5: Final status update
    logger.info(f"Processing completed for domain: {domain}")
    mongo_handler.close()

if __name__ == "__main__":
    main()
