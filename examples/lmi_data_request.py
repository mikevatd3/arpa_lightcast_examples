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
    # ./request_payloads/lmi_data_request_software_development.json
    # ./request_payloads/lmi_data_request_all_jobs.json

    url = "https://agnitio.emsicloud.com/meta"
    response = requests.request("get", url, headers=headers)

    payload = json.loads(
        (
            EXAMPLE_DIR
            / "request_payloads"
            
            # Switch comments around to try different payloads
            / "lmi_data_request_software_development.json"
            #  / "lmi_data_request_all_jobs.json"
        ).read_text()
    )

    response = requests.request("post", url, headers=headers, json=payload)

    with open(EXAMPLE_DIR / "output" / "lmi_software_development.json", "w") as f:
        json.dump(response.json(), f, indent=4)

    ###########################################################################


if __name__ == "__main__":
    main()
