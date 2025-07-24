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
    # EXAMPLES
    ###########################################################################

    # Review payload structure:
    # ./request_payloads/cp_request.json
    
    # Dimensions available:
    # soc
    # onet
    # lotocc
    # lotspecocc

    url = "https://emsiservices.com/career-pathways/dimensions/soc/feederjobs"
    response = requests.request("get", url, headers=headers)

    payload = json.loads(
        (
            EXAMPLE_DIR
            / "request_payloads"
            / "cp_data_request_data_scientist.json"
        ).read_text()
    )

    response = requests.request("post", url, headers=headers, json=payload)

    with open(EXAMPLE_DIR / "output" / "cp_response.json", "w") as f:
        json.dump(response.json(), f, indent=4)

    ###########################################################################


if __name__ == "__main__":
    main()
