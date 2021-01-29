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

branch=Item(name = "branch", description= 'cus you gotta protect yourself somehow...')
sandwich=Item(name = "sandwich", description= 'gives health and is really tasty but, low key who left this here...')
sword=Item(name = "sword", description= 'idk why you would need this at this time but cool wish it was the master sword though...')
shield=Item(name = "shield", description= 'ooh snap its like a real mmo now..')
necklace=Item(name = "necklace", description= 'This better give me good stats or im going to return it...')
boots=Item(name = "boots", description= 'papa needs a new pair of shoes or in this case boots...')

#items in the rooms
room['outside'].addItems(sandwich)
room['outside'].addItems(necklace)
room['foyer'].addItems(shield)
room['overlook'].addItems(sword)
room['narrow'].addItems(boots)
room['treasure'].addItems(sandwich)


#
# Main functionally for the game
#

# Make a new player object that is currently in the 'outside' room.
p = Player(name = 'Raymond',current_room = room['outside'])
p.addItem(branch)
 
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
        print("oof... I can't go this way, let me try that again...")
def pick_up(item_name):
    for item in p.current_room.items :
        if item_name == item.name:
            p.addItem(item)
            p.current_room.deleteItems(item)
            return

def drop_down(item_name):
    for item in p.current_items:
        if item_name == item.name:
            p.current_room.addItems(item)
            p.deleteItems(item)
            return            
# Write a loop that:
#
# * Prints the current room name
while True:
    print("\n")
    print('(Name)',p.name)
    print('(Location)',p.current_room.name)
    print(p.current_room.description)
    print('(Items in the area)',p.current_room.items)
    
    
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
    print("\n")
    answer= input("where do you want to go? n,e,s,w --- Did you want to pickup an item? get <name> --- Did you want to drop an item? drop <name> --- Show inventory? i --- To quit q>").lower().strip()
    print("\n")
    
    if answer in ['n','e','s','w'] :
        change_room(answer)
    if answer[0:3] in ['get']:
       try :
        pick_up(answer.split()[1])
       except:
        print('I didn\'t understand...') 

    if answer[0:4] in ['drop']:
        try:
         drop_down(answer.split()[1]) 
        except:
         print('I didn\'t understand...')   

    if answer in ['i']:
        print('----inventory----')
        for item in p.current_items:
            print('(Item)',item.name,'---',item.description)
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
    if answer == "q" :
        break