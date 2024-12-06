import requests
import json
url = "https://192.168.60.9:8006"

login_data = {
    "username": "root@pam",
    "password": "vS1XdX6QRwj8tAayNvzZ"
}

response = requests.post(f"{url}/api2/json/access/ticket", data=login_data, verify=False)

if response.status_code != 200:
    print(f"Error: {response.status_code}")
    exit()

data = response.json()
ticket = data["data"]["ticket"]
csrf_prevention_token=data["data"]["CSRFPreventionToken"]
test = data["data"]
print(test)
print (ticket)
print(csrf_prevention_token)
headers = {
    "CSRFPreventionToken": csrf_prevention_token,
    "Cookie": f"PVEAuthCookie={ticket}"
}

response = requests.get(f"{url}/api2/json/nodes", headers=headers, verify=False)
print(json.dumps(response.json(), indent=4))

nodes = response.json()["data"]
for node in nodes:
    print(f"node: {node['node']} - Status: {node['status']}")
