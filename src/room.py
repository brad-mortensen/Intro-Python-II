# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items):
        self.name = name
        self.description = description
        self.items = items
    def __repr__(self):
        return f"{self.name}. {self.description} Items in room: {self.items}"
    def add_to_room(self, item):
        self.items.append(item)

    def remove_from_room(self, item):
        self.items.remove(item)    