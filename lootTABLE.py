import json
fishDICT = open("./fishDICT.json", encoding="utf8")
rodDICT = open("./rodDICT.json", encoding="utf8")
baitDICT = open("./baitDICT.json", encoding="utf8")
data = json.load(fishDICT)
rodDATA = json.load(rodDICT)
baitDATA = json.load(baitDICT)
import random
import math
class calculator():
    def mult(numbers):
        print(math.prod(numbers))

reorg_fishDICT = {}
def dictFISH(fishes):
    for fish in fishes:
        if fish["name"] not in reorg_fishDICT:
            reorg_fishDICT[fish["name"]] = {
                "name":fish["name"]
            }
        if fish["rarity"] not in reorg_fishDICT:
            reorg_fishDICT[fish["name"]] = {
                "rarity":fish["rarity"],
                "chanceWEIGHT":fish["chanceWEIGHT"]
            }
    return reorg_fishDICT
dictFISH(data)
for key, value in reorg_fishDICT.items():
    print(key, "→", value)


rareWEIGHT = []
for item in data:
    rarety = item["chanceWEIGHT"]
    rareWEIGHT.append(rarety)

nameLIST = []
for item in data:
    name = item["name"]
    nameLIST.append(name)


select = random.choices(nameLIST, weights=rareWEIGHT, k = 10)
print(select)

luckFACTORS = [3, 1.2]
def lootSELECT(luckMULTIPLIER):
    for item in data:
        if int(reorg_fishDICT[item["chanceWEIGHT"]]) < 0.01:
            print(1)


lootSELECT(calculator.mult(luckFACTORS))


