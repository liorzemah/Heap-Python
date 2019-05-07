# implementation of heap class

class Heap:
    def __init__(self, A):
        if (type(A) is not list):
            raise TypeError("A type is", type(A) ,", A need be from type 'list'")
        else:
            self.size = 0
            self.A = []
            print ("len(A)",len(A))
            for i in range(0, len(A), 1):
                print ("A[",i,"] = ", A[i])
                self.insert(A[i])

    def insert(self, x):
        self.size += 1
        self.A.insert(self.size, x)

        pos = self.size - 1
        self.heapify(pos)
        print(self.A)

    def heapify(self, i):
        while i > 0 and self.A[int(i / 2)] > self.A[i]:
            self.A[i], self.A[int(i / 2)] = self.A[int(i / 2)], self.A[i]
            i = int(i / 2)

    def delete_min(self):
        if self.size == 0:
            return None

        # pos = 0
        # while (pos*2+1 < self.size and self.A[pos] < self.A[pos*2+1]) or (pos*2+2 < self.size and self.A[pos] < self.A[pos*2+2]):
        #     if self.A[pos] < self.A[pos*2+1]:
        #         self.A[pos], self.A[pos*2+1] = self.A[pos*2+1], self.A[pos]
        #         pos = pos * 2 + 1
        #     else:
        #         self.A[pos], self.A[pos*2+2] = self.A[pos*2+2], self.A[pos]
        #         pos = pos * 2 + 2

        self.size -= 1
        min = self.A.pop(0)
        for i in range(0, len(self.A), 1):
            self.heapify(i)
        return min


    def print_heap(self):
        for i in self.A:
            print(str(i))


