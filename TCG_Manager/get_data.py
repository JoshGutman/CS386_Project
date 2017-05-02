import json, requests

resp = requests.get(url="https://api.pokemontcg.io/v1/cards?page=5&pageSize=500")
data = json.loads(resp.text)

f = open("pokemon.txt", "w")
for card in data["cards"]:
    try:
        f.write("{}: {}\n".format(card["name"], card["imageUrl"]))
    except UnicodeEncodeError:
        continue
f.close()
