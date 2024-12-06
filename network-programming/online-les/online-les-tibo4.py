import requests
import json

url = "https://192.168.60.9:8006"

# API token information
api_token_id = "root@pam!python"
api_token = "13393692-3168-41de-a9be-9e88dcaca249"
node = "pve"

# Headers for authentication
# belangrijk hoofdlettergevoelig!!
headers = {
    "Authorization": f"PVEAPIToken={api_token_id}={api_token}"
}

# Make the GET request to fetch nodes
response = requests.get(f"{url}/api2/json/nodes/{node}/aplinfo", headers=headers, verify=False)

# Check if the response is successful
if response.status_code != 200:
    print(f"Error: {response.status_code}, {response.text}")
    input("press enter to exit")
    exit()

# Parse the response JSON
data = response.json()["data"]
#print(json.dumps(data, indent=4))  # Print the full response for debugging

for template in data:
    if "alpine" in template["package"]: # filter toepassen
        print(f"Name : {template['template']} - Infopagina : {template['infopage']}")