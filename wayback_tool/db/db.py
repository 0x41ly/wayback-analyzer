from .db_handler import mongo_handler  # MongoDB connection handler
from .db_operations import save_url_with_params, update_url_status, update_param_set_status, get_urls_by_status, get_urls_by_process_status

def save_endpoints(domain: str, endpoints: list):
    """
    Save the given endpoints for a domain.
    """
    for endpoint in endpoints:
        save_url_with_params(domain, endpoint)

def save_params(domain: str, params: list):
    """
    Save the given parameters for a domain.
    """
    for param in params:
        # Update or save parameters for the given domain (assumes params are structured correctly)
        save_url_with_params(domain, param)

def save_responses(domain: str, responses: list):
    """
    Save the responses for the given domain.
    """
    for response in responses:
        # Store or update responses for the given domain
        pass  # Logic for saving responses can be added here

def get_urls_by_status(status: str):
    """
    Get URLs by status from the database.
    """
    return get_urls_by_status(status)

def get_urls_by_process_status(process_status: str):
    """
    Get URLs by process status from the database.
    """
    return get_urls_by_process_status(process_status)

def close_db():
    """
    Close the MongoDB connection.
    """
    mongo_handler.close()
