import requests

response = requests.get('https://api64.ipify.org/?format=json')
print(response.text)

print(response.status_code)
print(response.headers)

