# Implement a class to hold room information. This should have name and
# description attributes.
# get the folder and then class call
from item import Item

class Room:
    def __init__(self, name, description, n_to, s_to, e_to, w_to, items=[]):
        self.name = name
        self.description = description
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.items = items

    def addItems(self, item):
        self.items.append(item)

    def __str__(self):
        return f"Room: {self.name} Description: {self.description} Item: {self.items}"

    def deleteItems(self, item):
        self.items.remove(item)