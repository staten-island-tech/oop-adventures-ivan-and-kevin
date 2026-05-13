import json
FishItem = open("./BuyDICT.json", encoding="utf-8")
data = json.load(FishItem)
FishItem.close()

def item(rod, bait):
    item=input("What item do you want to buy?").lower()
    for item in data:
        if item("rod"):
            print("Rod List:")
        elif item("bait"):
            print("Bait List:")
