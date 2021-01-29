# Implement a class to hold room information. This should have name and
# description attributes.
# get the folder and then class call
from item import Item

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = list()
#pick up
    def addItems(self, item):
        self.items.append(item)
#on hand
    def __str__(self):
        return f"Room: {self.name} Description: {self.description} Item: {self.items}"
#yeet items
    def deleteItems(self, item):
        self.items.remove(item)
        