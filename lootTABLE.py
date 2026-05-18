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

# Selection Example
""" rareWEIGHT = []
for item in data:
    rarety = item["chanceWEIGHT"]
    rareWEIGHT.append(rarety)

nameLIST = []
for item in data:
    name = item["name"]
    nameLIST.append(name)


select = random.choices(nameLIST, weights=rareWEIGHT, k = 10)
print(select) """
luckFACT = [2, 3]
def new_lootMULT(luckMULTIPLERS):
    rareWEIGHT = []
    for item in data:
        rarety = item["chanceWEIGHT"]
        rareWEIGHT.append(rarety)
    for x in range(len(rareWEIGHT)):
        if rareWEIGHT[x] < 0.01:
            rareFISH = rareWEIGHT[x] < 0.01
            factors = [luckMULTIPLERS, rareFISH]
            result = calculator.mult(factors)
            print(result)
        else:
            print("hga")
new_lootMULT(calculator.mult(luckFACT))

