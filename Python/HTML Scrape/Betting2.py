import requests

url = "https://scrapeninja.p.rapidapi.com/scrape"

payload = "{\"url\": \"https://www.oddschecker.com/horse-racing\"}"
headers = {
    'content-type': "application/json",
    'x-rapidapi-host': "scrapeninja.p.rapidapi.com",
    'x-rapidapi-key': "e36a5b82f4mshc24651f766981f8p19b8abjsn0b7183402eaa"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
