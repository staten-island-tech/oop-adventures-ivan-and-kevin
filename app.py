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

    def buy_equipment(self, cost, rod, bait):
        if self.money >= cost:
            self.money -= cost
            print(f"{self.name} has bought a {rod}.")
        elif bait:
            print(f"{self.name} has bought {bait}.")
        else:
            print(f"{self.name} does not have enough money to buy the equipment.")