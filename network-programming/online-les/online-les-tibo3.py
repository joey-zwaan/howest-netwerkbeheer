import requests
import json

url = "https://192.168.60.9:8006"

# API token information
api_token_id = "root@pam!python"
api_token = "13393692-3168-41de-a9be-9e88dcaca249"

# Headers for authentication
headers = {
    "Authorization": f"PVEAPIToken={api_token_id}={api_token}"
}

# Make the GET request to fetch nodes
response = requests.get(f"{url}/api2/json/nodes", headers=headers, verify=False)

# Check if the response is successful
if response.status_code != 200:
    print(f"Error: {response.status_code}, {response.text}")
    input("press enter to exit")
    exit()

# Parse the response JSON
response_json = response.json()
print(json.dumps(response_json, indent=4))  # Print the full response for debugging

#specifieke value
node_name = response.json()["data"][0]["node"]
print(node_name)
    # Extract and print node information


nodes = response.json()["data"]
for node in nodes:
        print(f"node: {node['node']} - Status: {node['status']}")

