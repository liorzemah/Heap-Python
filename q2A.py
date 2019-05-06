# ~~~ This is a template for question 2  ~~~

from Heap import Heap
from City import City

def get_next_city(arr, ignore_indexes):
    heap = Heap(arr)
    city = heap.delete_min()
    while (city.id in ignore_indexes):
        city = heap.delete_min()
    print(city)
    return city

def greedy(A, begin_index):
    visited_cities = []
    sum_dest = 0
    cur_index = begin_index
    old_indexes = []

    while len(visited_cities) < len(A) - 1:
        heap = Heap(A[cur_index])
        old_indexes.append(cur_index)
        city = get_next_city(A[cur_index], old_indexes)
        visited_cities.append(city)
        cur_index = city.id
        sum_dest += city.destination

    return visited_cities, sum_dest

if __name__ == '__main__':
    h1 = Heap([1, 2, 4, 5])
    h1.print_heap()
    h1.insert(3)
    h1.print_heap()

    B = [[City(0, 0), City(1, 6), City(2, 13)],
          [City(0, 6), City(1, 0), City(2, 20)],
          [City(0, 13), City(1, 20), City(2, 0)]]

    visited, sum_dest = greedy(B, 0)
    print(sum_dest)
