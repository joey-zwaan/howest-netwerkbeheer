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
url = data[0]["url"]
print(url)