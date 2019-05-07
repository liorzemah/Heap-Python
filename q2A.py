# ~~~ This is a template for question 2  ~~~

##############Heap Class Implement##############

class Heap:
    def __init__(self, A):
        if (type(A) is not list):
            raise TypeError("A type is", type(A) ,", A need be from type 'list'")
        else:
            self.size = 0
            self.A = []
            for i in range(0, len(A), 1):
                self.insert(A[i])

    def insert(self, x):
        self.size += 1
        self.A.insert(self.size, x)

        pos = self.size - 1
        self.heapify(pos)

    def heapify(self, i):
        while i > 0 and self.A[int(i / 2)] > self.A[i]:
            self.A[i], self.A[int(i / 2)] = self.A[int(i / 2)], self.A[i]
            i = int(i / 2)

    def delete_min(self):
        if self.size == 0:
            return None
        self.size -= 1
        min = self.A.pop(0)
        for i in range(0, len(self.A), 1):
            self.heapify(i)
        return min

    def print_heap(self):
        for i in self.A:
            print(str(i))


######################End#######################

##############City Class Implement##############

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

######################End#######################

def get_next_city(arr, ignore_indexes):
    if len(arr) < 2:
        return None
    if (type(arr) is not list) or (type(arr[0]) is not City) or (type(ignore_indexes) is not list) or (len(ignore_indexes) > 0 and type(ignore_indexes[0]) is not int):
        raise TypeError("get_next_city need get list of elements from type city and list of element from type integer")
    heap = Heap(arr)
    city = heap.delete_min()
    while (city.id in ignore_indexes):
        city = heap.delete_min()
    return city

def is_valid_matrix(A):
    if type(A) is not list:
        raise TypeError("A is not matrix")
        return False
    rows = len(A)
    if rows == 0:
        raise ValueError("A is empty")
        return False
    for row in A:
        if type(row) is not list:
            raise TypeError("A is not matrix")
            return False
        cols = len(row)
        if cols != rows:
            raise ValueError("A is not valid matrix")
            return False
    return True

def greedy(A, begin_index):
    if is_valid_matrix(A):
        if type(A[0][0]) is not City:
            raise TypeError("A is not matrix of cities")
        if type(begin_index) is not int:
            raise TypeError("begin_index must be from type integer")
    visited_cities = []
    sum_dest = 0
    cur_index = begin_index
    old_indexes = []

    while len(visited_cities) < len(A) - 1:
        old_indexes.append(cur_index)
        city = get_next_city(A[cur_index], old_indexes)
        visited_cities.append(city)
        cur_index = city.id
        sum_dest += city.destination

    return visited_cities, sum_dest

if __name__ == '__main__':
    B = [[City(0, 0), City(1, 6), City(2, 13)],
          [City(0, 6), City(1, 0), City(2, 20)],
          [City(0, 13), City(1, 20), City(2, 0)]]

    visited, sum_dest = greedy(B, 0)
    print(sum_dest)
