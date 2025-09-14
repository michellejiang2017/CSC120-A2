"""
Filename: computer.py
Description: The computer class for resale shop. 
Author: Michelle Jiang
Date: 2025-09-11
"""

# Imports everything from oo_resale_shop.py
from oo_resale_shop import *

class Computer:

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    def __init__(self, 
                description: str,
                processor_type: str,
                hard_drive_capacity: int,
                memory: int,
                operating_system: str,
                year_made: int,
                price: int):
        
        self.description = description
        self.processor_type = processor_type
        self.hard_drive_capacity = hard_drive_capacity
        self.memory = memory
        self.operating_system = operating_system
        self.year_made = year_made
        self.price = price
        
        """
        Takes in an item_id and a new price, updates the price of the associated
        computer if it is the inventory, prints error message otherwise
        """
        def update_price(self, inventory ResaleShop.inventory, item_id: int, new_price: int):
            if inventory[item_id] is not None:
                inventory[item_id]["price"] = new_price
            else:
                print("Item", item_id, "not found. Cannot update price.")

        
        """
        What am I confused by? 
        1. all the functions in the procedural code require both inventory and computer classes 
        
        import computer class into resale shop--need to check if compt is in inventory --> import both into main
        2. I don't know where to put the main function or any of the other functions 
        
        can add main functions to class files or can use main.py to test the object 
        
        3. If I'm supposed to separate the methods, how am I supposed to do that when every time I update the computer I need to check against the inventory
        --> don't separate the methods import them into one another 
        What do I need to do? 
       
         1. rewrite the functions so that they are able to work in the oo framework 
        2. put the main function into one of the classes? so that it's the main class. I think it should be in the resale shop one but the main.py has it in a separate file. 
        """