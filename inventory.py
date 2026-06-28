"""
LifeQuest AI
Inventory System
"""

from collections import Counter


class Inventory:

    def __init__(self):

        self.items = Counter()

    # ------------------------------------
    # Add Item
    # ------------------------------------

    def add_item(self, item, quantity=1):

        self.items[item] += quantity

    # ------------------------------------
    # Remove Item
    # ------------------------------------

    def remove_item(self, item, quantity=1):

        if self.items[item] >= quantity:

            self.items[item] -= quantity

            if self.items[item] <= 0:
                del self.items[item]

            return True

        return False

    # ------------------------------------
    # Check Item
    # ------------------------------------

    def has_item(self, item):

        return item in self.items

    # ------------------------------------
    # Quantity
    # ------------------------------------

    def quantity(self, item):

        return self.items.get(item, 0)

    # ------------------------------------
    # Inventory List
    # ------------------------------------

    def get_items(self):

        return dict(self.items)

    # ------------------------------------
    # Clear Inventory
    # ------------------------------------

    def clear(self):

        self.items.clear()
