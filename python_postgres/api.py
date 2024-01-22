import requests
import json

dominio = "google.com"

url = f"https://www.virustotal.com/api/v3/domains/{dominio}/comments"

payload = {}
headers = {
  'x-apikey': '4960aca6e7a214e881c9b2743fbdb7f3836361074b5e74ace80ab0e5404f56ad'
}

response = requests.request("GET", url, headers=headers, data=payload)
response = json.loads(response.text)

print("Insert into table dominios: ", dominio, " hay ", response['meta']['count'])
print("Isert into table dominios:", dominio,"hay", response['data'][0]['attributes']['text'])