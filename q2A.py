# ~~~ This is a template for question 2  ~~~

from Heap import Heap
from City import City

# A = np.array([[City(0, 0), City(1, 6), City(2, 13)],
#               [City(0, 6), City(1, 0), City(2, 20)],
#               [City(0, 13), City(1, 20), City(2, 0)]])


def greedy(A, begin_index):
    arr = A[begin_index]
    heap = Heap(arr)
    heap.print_heap()


if __name__ == '__main__':
    h1 = Heap([1, 2, 4, 5])
    h1.print_heap()
    h1.insert(3)
    h1.print_heap()

    B = [[City(0, 0), City(1, 6), City(2, 13)],
          [City(0, 6), City(1, 0), City(2, 20)],
          [City(0, 13), City(1, 20), City(2, 0)]]

    greedy(B, 0)

