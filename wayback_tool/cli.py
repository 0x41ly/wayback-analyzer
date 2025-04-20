import argparse

def get_args():
    parser = argparse.ArgumentParser(
        description="Wayback Recon Tool: Fetch, parse, and analyze URLs from the Wayback Machine."
    )

    parser.add_argument(
        "--domain",
        required=True,
        help="Target domain (e.g. example.com)"
    )

    parser.add_argument(
        "--delay",
        type=float,
        default=0.3,
        help="Delay between requests to avoid rate-limiting (default: 0.3)"
    )

    return parser.parse_args()
