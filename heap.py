from typing import List

class Heap:

    def __init__(self, list_: List[int]) -> List[int]:
        self._heap = list_
        self._heapify()

    @property
    def length(self):
        return len(self._heap)

    def _swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

    def _is_leaf(self, index):
        return index * 2  >= self.length

    def _is_root(self, index):
        return index == 0

    def _heapify(self):
        for index in reversed(range(self.length)):
            while not self._is_leaf(index):
                largest_index = index
                left_index = index * 2
                if self._heap[left_index] > self._heap[largest_index]:
                    largest_index = left_index
                right_index = left_index + 1
                if (
                        right_index < self.length
                        and self._heap[right_index] > self._heap[largest_index]
                ):
                    largest_index = right_index
                if largest_index != index:
                    self._swap(index, largest_index)
                    index = largest_index
                else:
                    break

    def push(self, number: int):
        self._heap.append(number)
        index = self.length - 1
        while not self._is_root(index):
            parent_index = index // 2
            if self._heap[parent_index] < self._heap[index]:
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def pop(self):
        number = self.peek()
        self._swap(0, -1)
        self._heap = self._heap[:-1]
        index = 0
        while not self._is_leaf(index):
            child_index = index * 2
            if (
                    child_index + 1 < self.length
                    and self._heap[child_index] < self._heap[child_index + 1]
            ):
                child_index = child_index + 1
            if self._heap[index] < self._heap[child_index]:
                self._swap(index, child_index)
                index = child_index
            else:
                break
        return number

    def peek(self):
        return self._heap[0]

def heapsort(numbers: List[int]) -> List[int]:
    for index in range(len(numbers)):
        numbers[index:] = Heap(numbers[index:])._heap
    return numbers
