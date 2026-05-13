import json
FishItem = open("./BuyDICT.json", encoding="utf-8")
data = json.load(FishItem)
FishItem.close()

def item(rod, bait):
    item=input("What item do you want to buy?").lower()
    for item in data:

 
    print("1. Give me a selection of the Rods")
    print("2. Give me a selection of the Baits")
    