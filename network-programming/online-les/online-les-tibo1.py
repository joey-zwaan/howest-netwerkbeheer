import requests

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
test = data["data"]
print(test)