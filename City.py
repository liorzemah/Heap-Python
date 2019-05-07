class City:
    def __init__(self, id, destination):
        if (type(id) is not int) or (type(destination) is not int):
            raise TypeError("id and destination must be from type integer")
        else:
            self.id = id
            self.destination = destination

    def __eq__(self, other):
         if self.destination == other.destination:
            return True
         return False

    def __gt__(self, other):
         if self.destination > other.destination:
            return True
         return False

    def __lt__(self, other):
         if self.destination < other.destination:
            return True
         return False

    def __str__(self):
        ret = str(self.id)
        ret += " "
        ret += str(self.destination)
        return ret
