from lootTABLE import new_lootMULT
from lootTABLE import fishWEIGHT
from lootTABLE import fishRARITY
from lootTABLE import expCALC
from lootTABLE import moneyCALC
from lootTABLE import calculator
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

    def buy_equipment(self, cost, rod, bait):
        if self.money >= cost:
            self.money -= cost
            print(f"{self.name}['rod'] has bought a ['name'].")
        elif bait:
            print(f"{self.name}['bait'] has bought ['name'].")
        else:
            print(f"{self.name} does not have enough money to buy the equipment.")
  

def startUP(user_name):
    user_name = Fisherman(user_name, money=100, experience=0, inventory={})
    actONE = ("First lets head to the market to buy a fishing rod! Press 1 to continue.")
    if int(actONE) == 1:
        
    return user_name
playerSTATS = startUP(input(" Welcome to x! Enter the name of your fisherman!"))
def play():

    
    while playerSTATS.experience != 100:
        action = input("What would you like to do? "  
        "  1: Fish"
        "  2: Go to Market"
        "  3: Map Select"
        "  4: Inspect Inventory"
        "  5: Select Rod")
        if int(action) == 1:
            luckFACTS = [Selected Rod, Selected Bait]
            print(f"You have arrived at {mapSELECTED}")
            fishACT = input("1. Cast Your Rod 2. Leave")
            if int(fishACT) == 1:
                fishSELECTED = new_lootMULT(calculator.mult(luckFACTS))
        elif int(action) == 2:
            marketACT = input("What would you like to do at the market? 1. Sell 2. Buy")
            if int(marketACT) == 1:
                print("You have arrived at the fish market! What would you like to sell?")

        elif int(action) == 3:
            print(3)
        elif int(action) == 4:
            print(4)


play(input("Enter the name of the fisherman: "))



