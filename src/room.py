# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
    
    def add_to_room(self, item):
        self.items.append(item)

    def remove_from_room(self, item):
        self.items.remove(item)    