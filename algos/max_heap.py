from typing import List


class MaxHeap:
    def __init__(self, k: int):
        self.k = k
        self.heap: List[int] = []

    def _bubble_down(self, i):
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        if l < len(self.heap) and self.heap[l] > self.heap[i]:
            largest = l
        if r < len(self.heap) and self.heap[r] > self.heap[largest]:
            largest = r

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._bubble_down(largest)

    def remove(self):
        if len(self.heap) == 0:
            raise IndexError("Can't remove element from empty heap")
        last = len(self.heap) - 1
        self.heap[0], self.heap[last] = self.heap[last], self.heap[0],

        self.heap.pop()
        if self.heap:
            self._bubble_down(0)

    def insert(self, val: int):
        self.heap.append(val)
        i = len(self.heap) - 1
        print(f"insert {val} at {i}")
        if i == 0:
            return
        parent_idx = (i - 1) // 2
        while parent_idx >= 0 and self.heap[i] > self.heap[parent_idx]:
            print(
                f"swap heap[{i}]={self.heap[i]} with heap[{parent_idx}]={self.heap[parent_idx]}"
            )
            self.heap[i], self.heap[parent_idx] = self.heap[parent_idx], self.heap[i]
            i = parent_idx
            parent_idx = (i - 1) // 2
            print(i, parent_idx)
        print(self.heap)

    def __str__(self):
        return f"{self.heap}"


max_heap = MaxHeap(3)
max_heap.insert(0)
max_heap.insert(1)
max_heap.insert(5)
max_heap.insert(4)
max_heap.insert(3)
max_heap.insert(2)
max_heap.insert(10)
max_heap.remove()
print(max_heap)
max_heap.remove()
print(max_heap)
max_heap.remove()
print(max_heap)
max_heap.remove()
print(max_heap)
