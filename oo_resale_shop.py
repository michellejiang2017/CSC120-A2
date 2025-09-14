"""
Filename: oos_resale_shop.py 
Description: Object-oriented code to run a small computer resale shop modified from procedural_resale_shop. The main code copied from main.py exists here as well. 
Author: Michelle Jiang
Date: 2025-09-11
"""
# Imports everything from the computer.py file
from computer import *

class ResaleShop:
    
    inventory: list = []

    def __init__(self, inventory: list = []):
        self.inventory = inventory

    """
    Takes in the computer object containing all the information about a computer,
    adds it to the inventory, returns the assigned item_id
    """
    def buy(self, computer: Computer):
        self.inventory.append(computer)
        return self.inventory.index(computer) 
    
    """
    Takes in an item_id and a new price, updates the price of the associated
    computer if it is the inventory, prints error message otherwise
    """
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None:
            self.inventory[item_id]["price"] = new_price
        else:
            print("Item", item_id, "not found. Cannot update price.")

    
    """
    prints all the items in the inventory (if it isn't empty), prints error otherwise
    """
    def print_inventory(self):
        # If the inventory is not empty
        if self.inventory:
            # For each item
            for item in self.inventory:
                # Print its details
                print(f'Item ID: {self.inventory.index(item)} : {item.__dict__}') # converts object to dictionary & prints attributes
        else:
            print("No inventory to display.")

def main():

        # Make the resale shop 
    myShop: ResaleShop = ResaleShop()

        # Create the example computer
    computerA : Computer = Computer(
    "Mac Pro (Late 2013)",
    "3.5 GHc 6-Core Intel Xeon E5",
    1024, 64,
    "macOS Big Sur", 2013, 1500
        )

        # Print a little banner
    print("-" * 21)
    print("COMPUTER RESALE STORE")
    print("-" * 21)

    # Add it to the resale store's inventory
    print("Buying", computerA.description)
    print("Adding to inventory...")
    computer_id = myShop.buy(computerA)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    myShop.print_inventory()
    print("Done.\n")

    
    return 

if __name__ == "__main__": 
    main()
