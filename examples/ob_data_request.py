from pathlib import Path
import json
import datetime
import requests
from auth import retrieve_auth

today = datetime.date.today().strftime("%Y%M%d")


EXAMPLE_DIR = Path(__file__).parent


def main():
    auth = retrieve_auth()
    headers = {
        "Authorization": f"Bearer {auth['access_token']}",
        "Content-Type": "application/json",
    }

    ###########################################################################
    # EXAMPLE
    ###########################################################################

    # Review payload structure:
    # ./request_payloads/ob_data_request_carpenter.json

    url = "https://emsiservices.com/occupation-benchmark/dimensions/soc"
    response = requests.request("get", url, headers=headers)

    payload = json.loads(
        (
            EXAMPLE_DIR
            / "request_payloads"
            / "ob_data_request_carpenter.json"
        ).read_text()
    )

    response = requests.request("post", url, headers=headers, json=payload)

    with open(EXAMPLE_DIR / "output" / "ob_carpenter.json", "w") as f:
        json.dump(response.json(), f, indent=4)

    ###########################################################################


if __name__ == "__main__":
    main()
