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
    def __init__(self, name, money, experience, inventory):
        self.name = name
        self.money = money
        self.experience = experience
        self.inventory = inventory

    def fish(self, experience_gained, fish_caught):
        self.experience += experience_gained
        print(f"{self.name} has gained {experience_gained} experience points.")
        print(f"{self.name} has caught {fish_caught} fish.")
    
    def sell_fish(self, fish_sold, money):
        self.money += money
        self.inventory.remove(fish_sold)


        print(f"{self.name} has sold {fish_sold} fish for {money}")

    def buy_equipment(self, cost, item):
        if self.money >= cost:
            self.money -= cost
            print(f"{self.name} has bought a {item}.")
        else:
            print(f"{self.name} does not have enough money to buy the equipment.")
  


def play(user_name):
    user_name = Fisherman(user_name, money=100, experience=0, inventory={})
    mapSELECTED = ["NONE"]
    while user_name.experience != 100:
        print("Main Menu")
        print("1. Fishing")
        print("2. Go to the MARKET")
        print("3. Map Selection")
        print("")
        action = input("What would you like to do?")

        if int(action) == 1:
            if mapSELECTED != "NONE":
                print(f"You have arrived at {mapSELECTED}")
                fishACT = input("1. Cast Your Rod 2. Select your bait 3. Leave")
                if int(fishACT) == 1:
                    luckFACTS = []
                    fishSELECTED = new_lootMULT(calculator.mult(luckFACTS))
            else:
                print("Please Select a map first")
        elif int(action) == 2:
            marketACT = input("What would you like to do at the market? 1. Buy 2. Sell")
            if int(marketACT) == 1:
                print("RODS")
                rodSHOP = dictROD(rodDATA)
                displayRODSHOP(rodSHOP)
                print("BAITS")
                baitSHOP = dictBAIT(baitDATA)
                displayBAITSHOP(baitSHOP)
                buyACT = input("What would you like to buy? (Type 5 to end shopping): ")
                while buyACT != 5:
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
                if buyACT == "5":
                    print("Thank you for shopping!")
                break
                
            elif int(marketACT) == 2:
                sellACT = input("You have arrived at the fish market! What would you like to sell?")


        elif int(action) == 3:
            displayMAPS(mapDATA)
            map_selection = input("Select A Map(Enter the Number)!")
            indexNUM = int(map_selection) - 1

            if 0 <= indexNUM < len(mapDATA):
                mapSELECTED.remove[0]
                mapSELECTED.append[mapDATA[indexNUM]]

                print(f"You ahve arrived at {mapSELECTED[0]['name']}")
            else:
                print("Invalid number")
        elif int(action) == 4:
            print(4)
        elif int(action) == 5:
            print(5)
play(input("Enter the name of the fisherman: "))



