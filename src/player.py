# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.inventory = []

    def get_item(self, item):
        self.inventory.append(item)
        print(f"Added {item} to inventory")

    def drop_item(self, item):
        self.inventory.remove(item)
        print(f"Dropped {item}")    
