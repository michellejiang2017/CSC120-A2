"""
Filename: oos_resale_shop.py 
Description: Object-oriented code to run a small computer resale shop modified from procedural_resale_shop. The main code copied from main.py exists here as well. 
Author: Michelle Jiang
Date: 2025-09-11
"""
# Imports everything from the computer.py file
from computer import *

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
    Takes in the ResaleShop object, an item_id and a new price, 
    updates the price of the associated computer using the update price function from the computer.py file if it is the inventory, 
    prints error message otherwise 
    """ 
    def update_price(self, item_id: int, new_price: int):
        if self.inventory[item_id] is not None: 
            self.inventory[item_id].update_price(new_price) 
        else: 
            print("Item", item_id, "not found. Cannot update price.")
        
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
    def sell(self, item_id: int):
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")

    """
    Takes in the ResaleShop object, an item_id and a new price, 
    updates the price of the associated computer using the update price function from the computer.py file if it is the inventory, 
    prints error message otherwise
    """
    def update_price(self, item_id: int, new_price: int, computer: Computer):
        if self.inventory[item_id] is not None: 
            computer.update_price(new_price)
        else:
            print("Item", item_id, "not found. Cannot update price.")

    """
    Takes in the ResaleShop object, the Computer object, an item id and optionally a new os, 
    refurbishes the computer by updating price and optionally os, 
    prints error message otherwise
    """
    def refurbish(self, computer: Computer, item_id: int, new_os: Optional[str] = None):
        if self.inventory[item_id] is not None:
            computer.refurbish(new_os)
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")


# Main code
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

    # Now, let's refurbish it
    new_OS = "MacOS Monterey"
    print("Refurbishing Item ID:", computer_id, ", updating OS to", new_OS)
    print("Updating inventory...")
    myShop.refurbish(computerA, computer_id, new_OS)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    myShop.print_inventory()
    print("Done.\n")

    # Update the price
    print("Updating price...")
    myShop.update_price(0, 1000, computerA)
    print("Done.\n")

    # Make sure it worked by checking inventory
    print("Checking inventory...")
    myShop.print_inventory()
    print("Done.\n")

    # Now, let's sell it!
    print("Selling Item ID:", computer_id)
    myShop.sell(computer_id)
    
    # Make sure it worked by checking inventory
    print("Checking inventory...")
    myShop.print_inventory()
    print("Done.\n")
    

# Calls the main() function when this file is run
if __name__ == "__main__": 
    main()
