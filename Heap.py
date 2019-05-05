# implementation of heap class
max_size = 10


class Heap:
    def __init__(self, A):
        self.size = len(A)
        self.A = A
        self.heapSort()

    def insert(self, x):
        if self.size is max_size:
            return "Overflow"
        self.size += 1
        self.A.insert(self.size, x)
        self.heapSort()

    # To heapify subtree rooted at index i.
    # n is size of heap
    def heapify(self,n, i):
        largest = i  # Initialize largest as root
        l = 2 * i + 1  # left = 2*i + 1
        r = 2 * i + 2  # right = 2*i + 2

        # See if left child of root exists and is
        # greater than root
        if l < n and self.A[i] < self.A[l]:
            largest = l

            # See if right cHeap2hild of root exists and is
        # greater than root
        if r < n and self.A[largest] < self.A[r]:
            largest = r

            # Change root, if needed
        if largest != i:
            self.A[i], self.A[largest] = self.A[largest], self.A[i]  # swap

            # Heapify the self.A, root.
            self.heapify(n, largest)

        # The mainHeap function to sort an array of given size


    def heapSort(self):
        n = len(self.A)

        # Build a maxheap.
        for i in range(n, -1, -1):
            self.heapify(n, i)

            # One by one extract elements
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
            print(i)

# if __name__ == '__main__':
#     arr = [12, 11, 13, 5, 6, 7]
#     heap = Heap(arr)
#     heap.print_heap()
#     print ("-----------------")
#     heap.insert(8)
#     heap.print_heap()
#     print("-----------------")
#     heap.delete_min()
#     heap.print_heap()


