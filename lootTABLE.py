import json
fishDICT = open("./fishDICT.json", encoding="utf8")
data = json.load(fishDICT)

import random
import math
class calculator():
    def mult(numbers):
        print(math.prod(numbers))
numberLIST = [5, 2, 3]
calculator.mult(numberLIST)
""" rareWEIGHT = []
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
    rareWEIGHT = []
    for item in data:
        rarety = item["chanceWEIGHT"]
        rareWEIGHT.append(rarety)
        lootMULTIPLIER = [2,3]
    calculator.mult(lootMULTIPLIER)
lootSELECT() """