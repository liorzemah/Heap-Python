class City:
    def __init__(self, id, destination):
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

    def __print__(self):
        print(self.id , self.destination)
