import json
fishDICT = open("./fishDICT.json", encoding="utf8")
data = json.load(fishDICT)

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

def lootSELECT():
    lootMULTIPLIER = []
    calculator.mult()