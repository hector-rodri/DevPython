import requests

URL = "https://pokeapi.co/api/v2/pokemon/"

respone = requests.get(URL)
data = respone.json()

print(data)