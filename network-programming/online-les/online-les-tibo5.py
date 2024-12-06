def check_response(response):
    if response.status_code != 200:
        print("Something went wrong!")
        print(f"Status Code: {response.status_code}")
        print(f"Error Message: {response.text}")
        input("Press Enter to exit...")
        exit()


import requests
import json

url = "https://192.168.60.9:8006"

# API token information
api_token_id = "root@pam!python"
api_token = "13393692-3168-41de-a9be-9e88dcaca249"
node = "pve"
storage = "local"

# Headers for authentication
# belangrijk hoofdlettergevoelig!!
headers = {
    "Authorization": f"PVEAPIToken={api_token_id}={api_token}"
}


body = {
    "template" : "alpine-3.20-default_20240908_amd64.tar.xz",
    "storage" : storage
}

# Make the GET request to fetch nodes
response = requests.post(f"{url}/api2/json/nodes/{node}/aplinfo", headers=headers, json=body, verify=False)

# Check if the response is successful
check_response(response)

# Parse the response JSON
data = response.json()["data"]
print(json.dumps(data, indent=4))  # Print the full response for debugging
print(data)


response = requests.get(f"{url}/api2/json/nodes/{node}/storage/{storage}/content", headers=headers, verify=False)

check_response(response)

data = response.json()["data"]
print(json.dumps(data, indent=4))