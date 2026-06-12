import json
import random
import math

fishDICT = open("./fishDICT.json", encoding="utf8")
rodDICT = open("./rodDICT.json", encoding="utf8")
baitDICT = open("./baitDICT.json", encoding="utf8")
mapDICT = open("./mapDICT.json", encoding="utf8")

data = json.load(fishDICT)
rodDATA = json.load(rodDICT)
baitDATA = json.load(baitDICT)
mapDATA = json.load(mapDICT)
from lootTABLE import EXPbar
from lootTABLE import new_lootMULT
from lootTABLE import fishWEIGHT
from lootTABLE import fishRARITY
from lootTABLE import expCALC
from lootTABLE import moneyCALC
from lootTABLE import calculator
from lootTABLE import dictROD
from lootTABLE import displayMAPS
from lootTABLE import displayRODSHOP
from lootTABLE import dictBAIT
from lootTABLE import displayBAITSHOP

class Fisherman:
    def __init__(self, name, money, experience, inventory, level):
        self.name = name
        self.money = money
        self.experience = experience
        self.inventory = inventory
        self.level = level
    def fish(self, experience_gained, fish_caught):
        self.experience += experience_gained 
        self.inventory[fish_caught] = self.inventory.get(fish_caught, 0) + 1 
        print(f"You caught a {fish_caught}! (+{experience_gained} EXP)") 
        cur = self.level
        nxt = self.level + 1

        if cur <= 10:   req = nxt**2 + (1.5 * cur + 5)
        elif cur <= 25: req = nxt**2 + (3 * cur + 7)
        elif cur <= 50: req = nxt**2.5 + (cur**1.5 - 2 * cur)
        elif cur <= 75: req = nxt**2.8 + (cur**1.75 - 2 * cur)
        elif cur <= 98: req = nxt**3.25 + (cur**2.25 - 2 * cur)
        else: req = nxt**3.65 + (cur**2.455 - 2 * cur)

        if self.experience >= req and self.level < 100:
            self.experience -= req
            self.level += 1
            print(f"LEVEL UP! You are now Level {self.level}! ")

    def sell_fish(self, fish_sold, money):
        self.money += money
        self.inventory.remove(fish_sold)
        print(f"{self.name} has sold {fish_sold} fish for {money}")
    def openIN(self):
        print("INVENTORY:")
        for item, count in self.inventory.items():
            print(f"{item}: {count}")
    def buy_equipment(self, cost, item):
        if self.money >= cost:
            self.money -= cost
            print(f"{self.name} has bought a {item}.")
        else:
            print(f"{self.name} does not have enough money to buy the equipment.")

        
    
  


def play(user_name):
    user_name = Fisherman(user_name, money=100, experience=0, inventory={}, level=1)
    mapSELECTED = ['Mediterranean Sea']
    
    while user_name.level != 100:
        print("Main Menu")
        print("1. Fishing")
        print("2. Go to the MARKET")
        print("3. Map Selection")
        print("4. Check STATS")
        print("5. Open Inventory")
        action = input("What would you like to do?")

        if int(action) == 1:
            calcEXP = 0
            calcMONEY = 0
            weightrand = 0
            rarerand = 0
            if mapSELECTED != 0:
                fishACT = input("1. Cast Your Rod 2. Select your bait 3. Leave")
                if int(fishACT) == 1:
                    luckFACTS = [Selected Rod, Selected Bait]
                    fishSELECTED = new_lootMULT(calculator.mult(luckFACTS))
                    weightrand = fishWEIGHT(fishSELECTED)
                    rarerand = fishRARITY(fishSELECTED)
                    calcEXP = expCALC(fishSELECTED)
                    calcMONEY = moneyCALC(fishSELECTED)
                    user_name.fish(calcEXP, fishSELECTED[0])
                    print( )
                elif int(fishACT) == 2:
                    user_name.openIN()
                    baitSELECT = input("What bait would you like to use?")
                    

        elif int(action) == 2:
            marketACT = input("What would you like to do at the market? 1. Buy 2. Sell")
            if int(marketACT) == 1:
                shopowner = []
                shopowner.append("[Shop Owner Fin Hook]: Wipe your boots, kid. You're tracking lake water all over my floor. Looking for a rod that won't snap on a real catch, or are you just wasting my daylight? ")
                shopowner.append("[Shop Owner Fin Hook]: Buy something useful today. If I see you fishing with a stick and string again, I will laugh.")
                shopowner.append("[Shop Owner Fin Hook]: Back from the water empty-handed, I see. Let me guess, the big one got away?")
                print(random.choice(shopowner))
                dialogue = input("Type 1 to view catolag. Type 2 to leave.")
                if int(dialogue) == 1:
                        print("RODS")
                        rodSHOP = dictROD(rodDATA)
                        displayRODSHOP(rodSHOP)
                        print("BAITS")
                        baitSHOP = dictBAIT(baitDATA)
                        displayBAITSHOP(baitSHOP)
                
                        buyACT = input("What would you like to buy? (Type 5 to end shopping): ")
                        while buyACT != "5":
                            if buyACT in rodSHOP:
                                item_data = rodSHOP[buyACT]  
                                item_cost = item_data['Price'] 
    
                                if user_name.buy_equipment(item_cost, buyACT):
                                    user_name.inventory.append(buyACT)
        
                            elif buyACT in baitSHOP:
                                item_data = baitSHOP[buyACT]  
                                item_cost = item_data['Price']  
    
                                if user_name.buy_equipment(item_cost, buyACT):
                                    user_name.inventory.append(buyACT)
                            else:
                                print("Invalid Please Try Again")
                            buyACT = input("What else would you like to buy? (Type 5 to end shopping): ")
                        if buyACT == "5":
                            print("Thank you for shopping!")
                        break
                elif int(dialogue) == 2:
                    print("You leave the shop and head back to the main area.")
            elif int(marketACT) == 2:
                seller = []
                seller.append("[Greedy Gill]: Let's see if you actually caught anything this time. No minnows! Only real fish!")
                seller.append("[Greedy Gill]: Ah, the local angler returns! Show me what you've hooked. Fresh fish brings fresh coin.")
                seller.append("[Greedy Gill]: Let me see the catch of the day. If it smells like a boot, I ain't paying for it. Lay 'em out on the table!")
                print(random.choice(seller))
                choiceACT = input("Enter 1 to sell. Enter 2 to leave.")
                if int(choiceACT) == 1:
                    user_name.openIN()
                    sellCHOICE = input("Type 1 to sell all")
                    if int(sellCHOICE) == 1:
                        inventoryVALUE = 0
                        for key, value in user_name.inventory.items():
                            inventoryVALUE += calculator.twomult(value, calcMONEY)
                        user_name.money += inventoryVALUE
                        user_name.inventory.clear()
                        print(f"You have {user_name.money} coins!")
                    else:
                        print("Invalid Number")


        elif int(action) == 3:
            displayMAPS(mapDATA)
            map_selection = input("Select A Map(Enter the Number)!")
            indexNUM = int(map_selection)-1

            if 0 <= indexNUM < len(mapDATA):
    
                if mapSELECTED:
                    mapSELECTED.pop(0)  
                    mapSELECTED.append(mapDATA[indexNUM])  
    
   
                current_map = mapSELECTED[0]
    
   
                if user_name.level >= current_map["LevelRequirement"]:
                    print(f"You have arrived at {current_map['Name']}")
        
                else:
                    print(f"You do not have the level required. You need level {current_map['LevelRequirement']}.")
                    mapSELECTED.pop(0) 
            else:
                print("Invalid number")
            
        elif int(action) == 4:
            choiceSTATS = input("What would you like to view? 1. LVL 2. COINS 3. EXP")
            if int(choiceSTATS) == 1:
                print(f"You are level {user_name.level}")
            elif int(choiceSTATS) == 2:
                print(f"You have {user_name.money} coins")
            elif int(choiceSTATS) == 3:
                print(f"You have {user_name.experience} points")
            else:
                print("INVALID NUMBER")
        elif int(action) == 5: 
            user_name.openIN()
play(input("Enter the name of the fisherman: "))

