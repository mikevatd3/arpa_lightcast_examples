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

    url = "https://emsiservices.com/career-pathways/meta"
    response = requests.get(url, headers=headers)

    with open(EXAMPLE_DIR / "output" / f"cp_metadata.json", "w") as f:
       json.dump(response.json(), f, indent=4)

    # Get the list of dimensions

    url = "https://emsiservices.com/career-pathways/dimensions"
    response = requests.get(url, headers=headers)

    with open(EXAMPLE_DIR / "output" / f"cp_dimensions.json", "w") as f:
       json.dump(response.json(), f, indent=4)

    # Show details of the soc dimension (no codes unforch)

    url = "https://emsiservices.com/career-pathways/dimensions/soc"
    response = requests.get(url, headers=headers)

    with open(EXAMPLE_DIR / "output" / f"cp_soc.json", "w") as f:
       json.dump(response.json(), f, indent=4)


    ###########################################################################


if __name__ == "__main__":
    main()
