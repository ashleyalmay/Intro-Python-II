class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description
#representation to get a string from an object
    def __repr__(self):
        return self.name

