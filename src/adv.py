from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together blueprint for set up

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#list of items in the game
branch=Item(name = "branch", description= 'cus you gotta protect your self some how...')
sandwich=Item(name = "sandwich", description= 'gives health and is really tasty but, low key who left this here...')
sword=Item(name = "sword", description= 'idk why you would need this at this time but cool wish it was the master sword though...')
shield=Item(name = "shield", description= 'ooh snap we going full knight now?')
necklace=Item(name = "necklace", description= 'This better give me good stats or im going to return it...')
boots=Item(name = "boots", description= 'papa needs a new pair of shoes or in this case boots...')

#items in the rooms
room['outside'].addItems(sandwich)
room['foyer'].addItems(shield)
room['overlook'].addItems(sword)
room['narrow'].addItems(boots)
room['treasure'].addItems(necklace)


#
# Main functionally for the game
#

# Make a new player object that is currently in the 'outside' room.
p = Player(name = 'Raymond',current_room = room['outside'],current_item= [branch])
 
def change_room(direction):
    try:
        if direction == "n":
            p.current_room = p.current_room.n_to
        elif direction == "s":
            p.current_room = p.current_room.s_to
        elif direction == "e":
            p.current_room = p.current_room.e_to
        elif direction == "w":
            p.current_room = p.current_room.w_to
    except:
        print("try again")
    

# Write a loop that:
#
# * Prints the current room name
while True:
    print('(name)',p.name)
    print('(Location)',p.current_room.name)
    print('(item(s))',p.current_item.current_item)
    print(p.current_room.description)
    
    
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    answer= input("where do you want to go? n,e,s,w or hit q to quit.>").lower().strip()
    print("\n")
    # answer = answer[0]
    
    if answer in ['n','e','s','w'] :
        change_room(answer)
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if answer == "q" :
        break