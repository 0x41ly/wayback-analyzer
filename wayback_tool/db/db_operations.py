from .db_handler import mongo_handler
from pymongo import UpdateOne
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def save_url_with_params(url: str, params: dict):
    """
    Save the URL and associated parameters to the MongoDB collection.
    """
    collection = mongo_handler.get_collection("urls")
    
    # Check if the URL already exists
    existing_url = collection.find_one({"url": url})
    if existing_url:
        logger.info(f"URL '{url}' already exists in the database.")
    else:
        collection.insert_one({
            "url": url,
            "params": [params],
            "status": "pending",
            "process_status": "not_started",
            "response_status": "",
            "response_length": 0,
            "created_at": datetime.utcnow()
        })
        logger.info(f"URL '{url}' saved to the database.")

def update_url_status(url: str, status: str, process_status: str = None):
    """
    Update the status of the URL in the database.
    """
    collection = mongo_handler.get_collection("urls")
    result = collection.update_one(
        {"url": url},
        {"$set": {"status": status, "process_status": process_status}}
    )
    
    if result.modified_count > 0:
        logger.info(f"URL '{url}' status updated to '{status}'.")
        return True
    else:
        logger.error(f"Failed to update status for URL '{url}'.")
        return False

def update_param_set_status(url: str, params: dict, status: str, process_status: str = None):
    """
    Update the status of the parameter set in the database.
    """
    collection = mongo_handler.get_collection("urls")
    result = collection.update_one(
        {"url": url, "params": params},
        {"$set": {"params.$.status": status, "params.$.process_status": process_status}}
    )

    if result.modified_count > 0:
        logger.info(f"Parameter set for URL '{url}' updated to '{status}'.")
        return True
    else:
        logger.error(f"Failed to update parameter set for URL '{url}'.")
        return False

def get_urls_by_status(status: str):
    """
    Fetch URLs from the database by status.
    """
    collection = mongo_handler.get_collection("urls")
    return list(collection.find({"status": status}))

def get_urls_by_process_status(process_status: str):
    """
    Fetch URLs from the database by process status.
    """
    collection = mongo_handler.get_collection("urls")
    return list(collection.find({"process_status": process_status}))
