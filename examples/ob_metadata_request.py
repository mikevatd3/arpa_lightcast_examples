from pathlib import Path
import json
import requests
from auth import retrieve_auth


EXAMPLE_DIR = Path(__file__).parent


def main():
    auth = retrieve_auth()
    headers = {
        "Authorization": f"Bearer {auth['access_token']}",
        "Content-Type": "application/json"
    }
    
    ###########################################################################
    # CALL EXAMPLES
    ###########################################################################
    
    # Main metadata call (returns summary of everything)

    url = "https://emsiservices.com/occupation-benchmark/meta"
    response = requests.get(url, headers=headers)

    with open(EXAMPLE_DIR / "output" / f"ob_metadata.json", "w") as f:
       json.dump(response.json(), f, indent=4)

    ###########################################################################


if __name__ == "__main__":
    main()
