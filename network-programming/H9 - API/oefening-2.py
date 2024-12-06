import requests
import json

url = "https://api.thedogapi.com/v1/images/search?format=json&limit=10"

payload = {}
headers = {
  'Content-Type': 'application/json',
  'x-api-key': 'live_EkeBDqBZiudyO8MCcarPm11TGqe1bYeyYey0F9CtRZxhB9pfA47VinIZxUohmgSo'
}

response = requests.request("GET", url, headers=headers)

dict = response.json()
print(json.dumps(dict,indent=3))


# API-GET request : response = request.get(url)
# Statuscode : response.status_code
# Ruwe tekst : response.txt
# Omzetten naar dict/list : response.json()
# output printen : print(json.dumps(dict,indent=3))