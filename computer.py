"""
Filename: computer.py
Description: The computer class for resale shop. 
Author: Michelle Jiang
Date: 2025-09-11
"""
# Import a few useful containers from the typing module
from typing import Optional


"""
Computer class which has atttributes description, processor type, hard drive capacity, memory, operating system, year made, and price. 
"""
class Computer:

    description: str 
    processor_type: str 
    hard_drive_capacity: int 
    memory: int 
    operating_system: str 
    year_made: int
    price: int 

    """
    Constructor for the computer class which initializes the computer object. 
    """
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
    Takes in the computer object and a new price, 
    updates the price of the associated computer.   
    """
    def update_price(self, new_price: int):
        self.price = new_price
    
    """
    Takes in the computer object and a new os, 
    updates the os of the computer. 
    """
    def update_os(self, new_OS: str): 
        self.operating_system = new_OS

    """
    Takes in the computer object and optionally a new os system, 
    checks the age of the computer to determine a new price and optionally updates the os. 
    """
    def refurbish(self, new_OS: Optional[str] = None):
        if int(self.year_made) < 2000:
            self.price = 0 # too old to sell, donation only
        elif int(self.year_made) < 2012:
            self.price = 250 # heavily-discounted price on machines 10+ years old
        elif int(self.year_made) < 2018:
            self.price = 550 # discounted price on machines 4-to-10 year old machines
        else:
            self.price = 1000 # recent stuff

        if new_OS is not None:
            self.operating_system = new_OS # update details after installing new OS
        else:
            return

        