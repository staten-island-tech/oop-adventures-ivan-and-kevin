<<<<<<< HEAD
import json
Fish_file = open("./fishDICT.json", encoding="utf8")
Bait_file = open("./baitDICT.json", encoding="utf8")
rod_file = open("./rodDICT.json", encoding="utf8")
data = json.load(Fish_file)
data2 = json.load(Bait_file)
data3 = json.load(rod_file)

class Fisherman:
    def __init__(self, name, money, experience, inventory):
        self.name = name
        self.money = money
        self.experience = experience
        self.inventory = inventory

=======
class Fisherman:
    def __init__(self, name, money, experience, inventory):
        self.name = name
        self.money = money
        self.experience = experience
        self.inventory = inventory

>>>>>>> main
    def fish(self, experience_gained, fish_caught):
        self.experience += experience_gained
        print(f"{self.name} has gained {experience_gained} experience points.")
        print(f"{self.name} has caught {fish_caught} fish.")
    
    def sell_fish(self, fish_sold, money):
        self.money += money
<<<<<<< HEAD
        print(f"{self.name} has sold {fish_sold} fish for {money}")
=======

>>>>>>> main

    def buy_equipment(self, cost, rod, bait):
        if self.money >= cost:
            self.money -= cost
<<<<<<< HEAD
            print(f"{self.name}['rod'] has bought a ['name'].")
        elif bait:
            print(f"{self.name}['bait'] has bought ['name'].")
        else:
            print(f"{self.name} does not have enough money to buy the equipment.")

    name=input("Enter the name of the fisherman: ")
=======
            print(f"{self.name} has bought a {rod}.")
        elif bait:
            print(f"{self.name} has bought {bait}.")
        else:
            print(f"{self.name} does not have enough money to buy the equipment.")

    print=input("Enter the name of the fisherman: ")
>>>>>>> main
    Fisherman = Fisherman(name, money=100, experience=0, inventory=[])


    while True:
<<<<<<< HEAD
        action = input("What would you like to do? (sell/market/exit/map): ")
        if action == "sell":
            fish_sold = int(input("Enter the number of fish sold: "))
            money = int(input("Enter the amount of money earned from selling the fish: "))
            Fisherman.sell_fish(fish_sold, money)
        elif action == "map":
            print("You can fish in the following locations: Medeiterranian Sea, Atlantic Ocean, Pacific Ocean")
        elif action == "market":
=======
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
>>>>>>> main
            print ("You can buy the following equipment: Rods or Bait:")
            cost = int(input("Enter the cost of the equipment: "))
            rod = input("Enter the type of rod you want to buy: ")
            bait = input("Enter the type of bait you want to buy: ")
            Fisherman.buy_equipment(cost, rod, bait)
        elif action == "exit":
            print(f"{Fisherman.name} has {Fisherman.money} money and {Fisherman.experience} experience points.")
            break
        else:
<<<<<<< HEAD
            print("Invalid action. Please try again.")
=======
            print("Invalid action. Please try again.")
>>>>>>> main
