<<<<<<< HEAD
=======

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
        return math.prod(numbers)
    def twomult(x, y):
        return x*y

""" reorg_fishDICT = {}
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
    print(key, "→", value) """

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
# Loot selection with Multipliers
luckFACT = [1, 1]
def new_lootMULT(luckMULTIPLERS):
    rareWEIGHT = []
    nameLIST = []

    for item in data:
        rarety = item["chanceWEIGHT"]
        rareWEIGHT.append(rarety)

        for x in range(len(rareWEIGHT)):
            if rareWEIGHT[x] < 0.01:
                factors = [luckMULTIPLERS, rareWEIGHT[x]]
                result = calculator.mult(factors)      
                rareWEIGHT.remove(rareWEIGHT[x])      
                rareWEIGHT.append(round(result, 5))
    for item in data:
        name = item["name"]
        nameLIST.append(name)

    select = random.choices(nameLIST, weights=rareWEIGHT, k = 1)
    return select

fishSELECTED = new_lootMULT(calculator.mult(luckFACT))


def fishWEIGHT(fishSELECT):
    for count in range(data[-1]["id"]):
        if fishSELECT[0] in data[count]["name"]:
            weight = random.randint(data[count]["minWEIGHT"], data[count]["maxWEIGHT"])
            return weight
weightrand = fishWEIGHT(fishSELECTED)

def fishRARITY(fishSELECT):
    for count in range(data[-1]["id"]):
        if fishSELECT[0] in data[count]["name"]:
            rarity = data[count]["rarity"]
            return rarity
rareRAND = fishRARITY(fishSELECTED)

EXPfactor = [1, 1]
def expCALC(fishSELECT):
    baseEXP = 1
    for x in range(data[-1]["id"]):
        if fishSELECT[0] in data[x]["name"]:
            if data[x]["id"] <= 15:
                baseEXP += random.randint(1, 3)
            elif data[x]["id"] >= 16:
                baseEXP += random.randint(5, 10)
    givenEXP = round(calculator.twomult((weightrand/5), baseEXP), 3)
    multEXP = round(calculator.twomult(givenEXP, calculator.mult(EXPfactor)), 3)
    return multEXP
calcEXP = expCALC(fishSELECTED)
MONEYfactor = [1, 1]
def moneyCALC(fishSELECT):
    baseMONEY = round(random.uniform(1.5,5), 2)
    worth = 0
    for x in range(data[-1]["id"]):
        if fishSELECT[0] in data[x]["name"]:
            if data[x]["rarity"] == "COMMON":
                worth = baseMONEY*random.randint(1, 3)
            elif data[x]["rarity"] == "RARE":
                worth = baseMONEY*random.randint(5, 10)
            elif data[x]["rarity"] == "EPIC":
                worth = baseMONEY*random.randint(11, 14)
            elif data[x]["rarity"] == "MYTHIC":
                worth = baseMONEY*random.randint(15, 18)
            elif data[x]["rarity"] == "LEGENDARY":
                worth = baseMONEY ** 1.75 + baseMONEY*random.randint(2,5)
            finalWORTH = round(calculator.twomult(worth, calculator.mult(MONEYfactor)), 2)
            return finalWORTH
            
calcMONEY = moneyCALC(fishSELECTED)


print(f"You Caught a(n) {fishSELECTED}!")
print(f"It weighs {weightrand} pounds.")
print(f"It is {rareRAND}")
print(f"You gained {calcEXP} exp")
print(f"The fish is worth ${calcMONEY}")
print()
class EXPbar():
    def __init__(self,nxtLVL, curtLVL):
        self.nxtLVL= nxtLVL
        self.curtLVL = curtLVL
    def lvl0to10(nxtLVL, curtLVL):
        return nxtLVL ** 2 +(1.5 * curtLVL + 5)
    def lvl11to25(nxtLVL, curtLVL):
        return nxtLVL ** 2 + (3 * curtLVL + 7)
    def lvl26to50(nxtLVL, curtLVL):
        return nxtLVL ** 2.5 + (curtLVL ** 1.5 - 2 * curtLVL)
    def lvl51to75(nxtLVL, curtLVL):
        return nxtLVL ** 2.8 + (curtLVL ** 1.75 - 2 * curtLVL)
    def lvl76to99(nxtLVL, curtLVL):
        return nxtLVL ** 3.25 + (curtLVL ** 2.25 - 2 * curtLVL)
    def lvl99to100(nxtLVL, curtLVL):
        return nxtLVL ** 3.65 + (curtLVL ** 2.455 - 2 * curtLVL)




    



>>>>>>> main
