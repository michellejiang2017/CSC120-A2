"""
Filename: oos_resale_shop.py 
Description: Object-oriented code to run a small computer resale shop modified from procedural_resale_shop. The main code copied from main.py exists here as well. 
Author: Michelle Jiang
Date: 2025-09-11
"""
# Imports everything from the computer.py file
from computer import *
# Import a few useful containers from the typing module
from typing import Optional


"""
ResaleShop class which has an empty list initially as its attribute
"""
class ResaleShop:
    
    inventory: list = [] # empty list representing the inventory of the shop

    """
    Constructor for the ResaleShop class which sets up the object. 
    """
    def __init__(self, inventory: list = []):
        self.inventory = inventory

    """
    Takes in the ResaleShop object and the Computer object containing all the information about a computer,
    adds it to the inventory of the ResaleShop object, 
    returns the assigned item_id
    """
    def buy(self, computer: Computer):
        self.inventory.append(computer)
        return self.inventory.index(computer) 

    """
    Takes in the ResaleShop object, 
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

    """
    Takes in the ResaleShop object and an item_id, 
    removes the associated computer if it is the inventory, 
    prints error message otherwise
    """
    def sell(self, computer: Computer, item_id: int):
        if computer in self.inventory: 
            self.inventory.remove(computer)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """
    Takes in the ResaleShop object, the Computer object and a new price, 
    updates the price of the associated computer using the update price function from the computer.py file if it is the inventory, 
    prints error message otherwise
    """
    def update_price(self, computer: Computer, new_price: int): 
        if computer in self.inventory: 
            computer.update_price(new_price)
        else:
            print("Item not found. Cannot update price.")

    """
    Takes in the ResaleShop object, the Computer object and a new price, 
    updates the price of the associated computer using the update price function from the computer.py file if it is the inventory, 
    prints error message otherwise
    """
    def update_os(self, computer: Computer, new_OS: str):
        if computer in self.inventory: 
            computer.update_os(new_OS)
        else:
            print("Item not found. Cannot update operating system.") 

    """
    Takes in the ResaleShop object, the Computer object, an item id and optionally a new os, 
    refurbishes the computer by updating price and optionally os, 
    prints error message otherwise
    """
    def refurbish(self, computer: Computer, new_OS: Optional[str] = None):
        if computer in self.inventory:
            computer.refurbish(new_OS)
        else:
            print("Item not found. Please select another item to refurbish.")


# Main code
def main():

    # Make the resale shop 
    my_shop: ResaleShop = ResaleShop()


    # Create the example computer
    computer_one : Computer = Computer(
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
    print("Buying", computer_one.description)
    print("Adding to inventory...")
    computer_id = my_shop.buy(computer_one)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    my_shop.print_inventory()
    print("Done.\n")

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    my_shop.refurbish(computer_one, new_OS) 
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    my_shop.print_inventory()
    print("Done.\n")

    # Update the price
    print("Updating price...")
    my_shop.update_price(computer_one, 1000)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    my_shop.print_inventory()
    print("Done.\n")

    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    my_shop.sell(computer_one, computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    my_shop.print_inventory()
    print("Done.\n")
    

# Calls the main() function when this file is run
if __name__ == "__main__": 
    main()