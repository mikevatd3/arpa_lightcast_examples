from pathlib import Path
import json
import datetime
import requests
from auth import retrieve_auth

today = datetime.date.today().strftime("%Y%M%d")


def main():
    auth = retrieve_auth()
    headers = {
        "Authorization": f"Bearer {auth['access_token']}",
        "Content-Type": "application/json"
    }

    ###########################################################################
    # EXAMPLES
    ###########################################################################
    
    # Main metadata call (returns a list of endpoints and available versions)

    url = "https://agnitio.emsicloud.com/meta"
    response = requests.request("get", url, headers=headers)

    with open(Path.cwd() / "output" / "lmi_metadata.json", "w") as f:
        json.dump(response.json(), f, indent=4)

    # Get more information about the items in the list from the call above
    # (though basically only a 'description' and 'title' field.

    url = "https://agnitio.emsicloud.com/meta/definitions"
    response = requests.request("get", url, headers=headers)

    with open(Path.cwd() / "output" / "lmi_definitions.json", "w") as f:
        json.dump(response.json(), f, indent=4)

    # Then for dataset-specific information like 'metrics' and 'dimensions' 
    # request the dataset itself. Use .../meta/dataset/<dataset name>/<version>

    url = "https://agnitio.emsicloud.com/meta/dataset/EMSI.us.Staffing/2025.3"
    response = requests.request("get", url, headers=headers)

    with open(Path.cwd() / "output" / "lmi_staffing_meta.json", "w") as f:
        json.dump(response.json(), f, indent=4)

    ###########################################################################


if __name__ == "__main__":
    main()
