# implementation of heap class

class Heap:
    def __init__(self, A):
        self.size = len(A)
        self.A = A
        self.heap_sort()

    def insert(self, x):
        self.size += 1
        self.A.insert(self.size, x)
        self.heap_sort()

    # To heapify subtree rooted at index i.
    # n is size of heap
    def heapify(self, n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and self.A[i] < self.A[l]:
            largest = l

        # See if right child of root exists and is
        # greater than root
        if r < n and self.A[largest] < self.A[r]:
            largest = r

        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]  # swap
            self.heapify(n, largest)

    def heap_sort(self):
        n = len(self.A)

        for i in range(n, -1, -1):
            self.heapify(n, i)

        for i in range(n - 1, 0, -1):
            self.A[i], self.A[0] = self.A[0], self.A[i]  # swap
            self.heapify(i, 0)

    def delete_min(self):
        if self.size == 0:
            return None
        self.size -= 1
        return self.A.pop(0)

    def print_heap(self):
        for i in self.A:
            print(str(i))


