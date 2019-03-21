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
    'outside':  Room("Outside Cave Entrance", "(n) of you, the cave mount beckons.", [item["bone"]]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east. (n) to overlook, (e) to the narrow passage or (s) to head back outside""", [item["sword"]]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm. Only way out is the way you came (s).""", [item["candy"]]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [item["shield"]]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber!Get ur gold n git! The only exit is to the (s).""", [item["gold"]]),
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
    if cmd == "i" or cmd == "inventory":
        print(f"\033[1;30;40m {player.name}\'s inventory: {player.inventory}")
    elif hasattr(player.current_room, attribute):
        room_attribute = getattr(player.current_room, attribute)
        player.current_room = room_attribute
        print(f"_________________________________{player.current_room}")  
    else:
        print("\n\nthat movement is not allowed.\n\n") 

def handle_grab_drop(command):
    split = command.lower().split(" ")
    if split[0] == 'grab' and item[split[1]] in player.current_room.items:
        player.get_item(item[split[1]])
        print(f"\033[1;30;40m {player.name}\'s inventory: {player.inventory}")
        player.current_room.remove_from_room(item[split[1]])
    elif split[0] == 'drop' and item[split[1]] in player.inventory:
        player.current_room.add_to_room(item[split[1]]) 
        player.drop_item(item[split[1]])
        print(f"\033[1;31;40m Items in room: {player.current_room.items}\n\n")
    else:
        print(f"{split[1]} aint there")       

# Main Loop
while True:
    if player.name == None:        
        player.name = input("\033[1;31;40m \n\nHello traveler, what is your name?\n\n")
        print(f"_________________________________{player.current_room}")    
    cmd = input(f"\033[1;33;40m \nWhat do you want to do {player.name}?\n\n")
    length = len(cmd.split(" "))
    if cmd == "q":
        print("\033[1;36;40m \n\n Thanks for Playing \n\n")
        break        
    handle_input(length, cmd)