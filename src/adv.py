from room import Room
from player import Player
from item import Item
# Declare all the rooms and items

item = {
    'sword': Item("sword", "An Old Broadsword"),
    'shield': Item("shield", "For Protection"),
    'bone': Item("bone", "A Spooky Skeleton Bone"),
    'candy': Item("skittles", "Some Skittles"),
    'gold': Item("gold", "A Buncha Dabloons"),
}

room = {
    'outside':  Room("Outside Cave Entrance", "North of you, the cave mount beckons.", [item["bone"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [item["sword"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", [item["candy"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item["shield"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [item["gold"]]),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new player object that is currently in the 'outside' room.
player = Player(None, room['outside'])
# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# Handles user Inputs
def handle_input(length, command):
    if length == 1:
        handle_movement(command)
    elif length == 2:
        handle_grab_drop(command)
    else: 
        print(f"{command} is not a valid input")

def handle_movement(command):
    attribute = command + "_to"
    if hasattr(player.current_room, attribute):
        room_attribute = getattr(player.current_room, attribute)
        player.current_room = room_attribute
    elif cmd == "i":
        print(f"{player.name} inventory:", player.inventory)
    else:
        print("that movement is not allowed.") 

def handle_grab_drop(command):
    split = command.lower().split(" ")
    if split[0] == 'grab' and split[1] == player.current_room.items[0].name:
        player.get_item(player.current_room.items[0])
        player.current_room.remove_from_room(player.current_room.items[0])
    elif split[0] == 'drop' and split[1] == player.inventory[0].name:
        player.current_room.add_to_room(player.inventory[0]) 
        player.drop_item(player.inventory[0])
        
    else:
        print(f"{split[1]} aint there")       

# Main Loop
while True:
    if player.name == None:
        player.name = input("Hello traveler, what is your name?")
    print(f"{player.current_room}")
    cmd = input(f"\nWhat do you want to do {player.name}?")
    length = len(cmd.split(" "))
    if cmd == "q":
        print("thanks for playing")
        break        
    handle_input(length, cmd)
