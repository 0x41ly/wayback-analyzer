import requests
import logging
from time import sleep
from random import uniform

logger = logging.getLogger(__name__)

def analyze_endpoints(data: dict, delay: tuple = (0.2, 0.6)):
    """
    Enrich the parsed URL data with status code and content length.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (WaybackAnalyzer)"
    }

    for endpoint, info in data.items():
        responses = []

        logger.info(f"[+] Analyzing {len(info['urls'])} URLs under: {endpoint}")
        
        for url in info["urls"]:
            try:
                response = requests.get(url, headers=headers, timeout=7)
                status = response.status_code
                length = len(response.content)
            except requests.RequestException as e:
                logger.warning(f"[!] Failed to fetch {url} -> {e}")
                status = None
                length = None

            responses.append({
                "url": url,
                "status": status,
                "length": length
            })

            sleep(uniform(*delay))  # Respectful delay between requests

        info["responses"] = responses

    return data
