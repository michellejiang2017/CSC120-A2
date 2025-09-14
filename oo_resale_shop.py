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

    # What methods will you need?
    def buy(self, 
                description: str,
                processor_type: str,
                hard_drive_capacity: int,
                memory: int,
                operating_system: str,
                year_made: int,
                price: int):
        
        computer = 
        self.inventory.append(computer)
        return self.inventory.index(computer) 

    def main():

            # Make the resale shop 
        myShop: ResaleShop = ResaleShop()

            # Create a computer 
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
        return 
    
    if __name__ == "__main__": 
        main()
