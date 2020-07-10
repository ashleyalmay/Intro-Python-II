# Write a class to hold player information, e.g. what room they are in
# currently.
#build of Player
class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.current_items = list()
#add items
    def addItem(self, item):
        self.current_items.append(item)
#yeet items
    def deleteItems(self, item):
        self.current_items.remove(item)