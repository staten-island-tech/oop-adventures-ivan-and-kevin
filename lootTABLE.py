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


rareWEIGHT = []
for item in data:
    rarety = item["chanceWEIGHT"]
    rareWEIGHT.append(rarety)

nameLIST = []
for item in data:
    name = item["name"]
    nameLIST.append(name)

select = random.choices(nameLIST, weights=rareWEIGHT, k = 1)
print(select)

def lootSELECT(luckMULTIPLIER):

lootSELECT()