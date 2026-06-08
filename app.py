from lootTABLE import new_lootMULT
from lootTABLE import fishWEIGHT
from lootTABLE import fishRARITY
from lootTABLE import expCALC
from lootTABLE import moneyCALC

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


    def buy_equipment(self, cost, rod, bait):
        if self.money >= cost:
            self.money -= cost
            print(f"{self.name} has bought a {rod}.")
        elif bait:
            print(f"{self.name} has bought {bait}.")
        else:
            print(f"{self.name} does not have enough money to buy the equipment.")

def play(user_name):
    user_name = Fisherman(user_name, money=100, experience=0, inventory=[])
    while user_name.experience != 100:
        action = input("What would you like to do? (fish/sell/buy/exit): ")
        if action == "fish":
            experience_gained = int(input("Enter the experience gained from fishing: "))
            fish_caught = int(input("Enter the number of fish caught: "))
            Fisherman.fish(experience_gained, fish_caught)
        elif action == "sell":
            fish_sold = int(input("Enter the number of fish sold: "))
            money = int(input("Enter the amount of money earned from selling the fish: "))
            Fisherman.sell_fish(fish_sold, money)
        elif action == "buy":
            print ("You can buy the following equipment: Rods or Bait:")
            cost = int(input("Enter the cost of the equipment: "))
            rod = input("Enter the type of rod you want to buy: ")
            bait = input("Enter the type of bait you want to buy: ")
            Fisherman.buy_equipment(cost, rod, bait)
        elif action == "exit":
            print(f"{Fisherman.name} has {Fisherman.money} money and {Fisherman.experience} experience points.")
            break
        else:
            print("Invalid action. Please try again.")


play(input("Enter the name of the fisherman: "))