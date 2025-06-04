import requests

nombre = input('Write the name of the pokemon to know its info: ').lower()
URL = f"https://pokeapi.co/api/v2/pokemon/{nombre}"

respone = requests.get(URL)

if respone.status_code == 200:
    data = respone.json()
    print('Name: '+data["name"])
    tipos = [t["type"]["name"] for t in data["types"]]
    print("Type: " + ", ".join(tipos))
    height = data["height"] / 10
    print(f"Height: {height} m")
    weight = data["weight"] / 10
    print(f"Weight: {weight} kg")
else:
    print('Pokemon nof found')

