import argparse
import os
import sys

import requests
from dotenv import load_dotenv
import json


# Project configurations, all initialisaion and env settings can be done here
def proj_configure():
    load_dotenv()


def get_logitude_latitude(session, ip):
    """Takes in IP address and session and returns json data
    for logitude and latitude"""

    url = f"http://api.ipstack.com/{ip}?access_key={os.getenv('access_key')}"
    response = session.get(url)
    data = response.json()
    reuired_data = {
        "longitude": data["longitude"],
        "latitude": data["latitude"]
    }
    return json.dumps(reuired_data)


def main(args=None):
    if args is None:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(description="Get IP Information")
    parser.add_argument(
        "--ip",
        help=(
            "script needs ip address to query longitude and latitude"
        ),
        default="",
        required=True
    )
    # Read args
    args = parser.parse_args()

    # Configurarions
    proj_configure()

    # Requests IP location
    s = requests.session()
    print(get_logitude_latitude(s, args.ip))


if __name__ == "__main__":
    main()
