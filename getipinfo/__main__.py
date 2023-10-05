import argparse
import os
import sys

import requests
from dotenv import load_dotenv


# Project configurations, all initialisaion and env settings can be done here
def proj_configure():
    load_dotenv()


def get_logitude_latitude(session, ip):
    url = f"http://api.ipstack.com/{ip}?access_key={os.getenv('access_key')}"
    response = session.get(url)
    data = response.json()
    return data["longitude"], data["latitude"]


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
    longitude, latitude = get_logitude_latitude(s, args.ip)

    # This print may not be necessary....
    print(f"IP Location:Longitude={longitude},Latitude={latitude}")


if __name__ == "__main__":
    main()
