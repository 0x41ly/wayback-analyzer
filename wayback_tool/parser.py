import logging
from urllib.parse import urlparse, parse_qs

logger = logging.getLogger(__name__)

def extract_endpoint_and_params(url: str):
    parsed = urlparse(url)
    endpoint = parsed.path
    params = parse_qs(parsed.query)

    # Convert query param values from lists to single values if needed
    params = {k: v for k, v in params.items()}

    return endpoint, params


def parse_urls(urls: list[str]) -> dict:
    """
    Group URLs by endpoint and collect unique param values.
    """
    grouped = {}

    for url in urls:
        endpoint, params = extract_endpoint_and_params(url)

        if endpoint not in grouped:
            grouped[endpoint] = {
                "params": {},
                "urls": [],
                "responses": []
            }

        grouped[endpoint]["urls"].append(url)

        for key, values in params.items():
            existing_values = grouped[endpoint]["params"].setdefault(key, [])
            for val in values:
                if val not in existing_values:
                    existing_values.append(val)

    logger.info(f"Parsed {len(grouped)} unique endpoints.")
    return grouped
