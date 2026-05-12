import json
fishDICT = open("./fishDICT.json", encoding="utf8")
data = json.load(fishDICT)

import random
import math
class calculator():
    def mult(numbers):
        print(math.prod(numbers))
        


lootDROPS = random.choices(data, rareity = data["chanceWEIGHT"], k = 1)