from pathlib import Path
import json
import requests
import datetime

"""
Use retreive_auth() to automatically update the auth token after it times out.
"""

BASE_DIR = Path(__file__).parent.parent


def refresh_auth():
    print("Refreshing Lightcast API token.")
    with open(BASE_DIR / "config.json") as f:
        config = json.load(f)

        CLIENT_ID = config["username"]
        CLIENT_SECRET = config["secret"]

    url = "https://auth.emsicloud.com/connect/token"

    payload = f"client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&grant_type=client_credentials&scope=career-pathways"
    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.request("POST", url, data=payload, headers=headers)

    with open("auth.json", "w") as f:
        auth_info = response.json()
        auth_info["received"] = datetime.datetime.now().isoformat()

        json.dump(auth_info, f)


def retrieve_auth():
    try:
        with open(BASE_DIR / "auth.json") as f:
            auth_info = json.load(f)

        # Check if token has expired
        received_time = datetime.datetime.fromisoformat(auth_info["received"])
        expires_in_seconds = auth_info["expires_in"]

        time_left = received_time + datetime.timedelta(
            seconds=(expires_in_seconds - 10) # Expire ten seconds early
        ) - datetime.datetime.now()

        print(f"{time_left} seconds remaining on auth token.")
        
        if datetime.datetime.now() > received_time + datetime.timedelta(
            seconds=(expires_in_seconds - 10) # Expire ten seconds early
        ):
            refresh_auth()
            with open(BASE_DIR / "auth.json") as f:
                auth_info = json.load(f)

        return auth_info

    except FileNotFoundError:
        print("creating new auth file")
        refresh_auth()
        with open("auth.json") as f:
            return json.load(f)
