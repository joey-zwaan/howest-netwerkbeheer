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
storage1 = "nvme-1"
template = "alpine-3.20-default_20240908_amd64.tar.xz"
# Headers for authentication
# belangrijk hoofdlettergevoelig!!
headers = {
    "Authorization": f"PVEAPIToken={api_token_id}={api_token}"
}

body = {
    "vmid" : 9999,
    "hostname" : "npe-alphine-container",
    "ostemplate": f"{storage}:vztmpl/{template}",
    "memory": 512,
    "rootfs": f"{storage1}:8",
    "swap" : 512,
    "net0" : "name=eth0,bridge=vmbr0,ip=dhcp"
}
response = requests.post(f"{url}/api2/json/nodes/{node}/lxc", headers=headers, json=body, verify=False)
data = response.json()
check_response(response)
print(json.dumps(data, indent=4))