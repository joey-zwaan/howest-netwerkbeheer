# Parsen van JSON

import requests
import json


with open("api.json") as f:
    api = json.load(f)
    api_key = api["api_key"]

url = "https://api.thedogapi.com/v1/images/search"
params = {"include_breeds": "true" , "breed_ids" : 50}
headers ={"x-api-key": api_key }
response = requests.get(url, params=params, headers=headers)
data = response.json()

 # print(data)

name = data[0]["breeds"][0]["name"]
# data[0] omdat het de eerste van de list is.
# Daarna komt de dictionary "breeds"
# dan is er terug een list
weight = data[0]["breeds"][0]["weight"]["metric"]
height = data[0]["breeds"][0]["height"]["metric"]

print(f"Het ras {name} wordt tussen {height} cm groot en tussen {weight} kg zwaar")