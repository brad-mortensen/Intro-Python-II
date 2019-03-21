# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def __repr__(self):
        return f"\033[1;35;40m \n\n{self.name}.\n\n{self.description}\n\n \033[1;32;40m Items in room: {self.items}\n\n"
    def add_to_room(self, item):
        self.items.append(item)

    def remove_from_room(self, item):
        self.items.remove(item)    