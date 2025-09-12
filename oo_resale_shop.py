"""
Filename: oos_resale_shop.py 
Description: Object-oriented code to run a small computer resale shop
Author: Michelle Jiang
Date: 2025-09-11
"""
# Imports the Computer class
from computer import Computer

class ResaleShop:
    
    inventory: list = []

    def __init__(self, inventory: list = []):
        self.inventory = inventory
    # What methods will you need?
    def buy(self, Computer):
        self.inventory.append(Computer)
        return self.inventory.index(Computer) 