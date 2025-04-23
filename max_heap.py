# max_heap.py

class MaxHeap:
    def __init__(self):
        self.heap = []  # stores (key, value) tuples
        self.index_map = {}  # key -> index in heap for O(1) search

    def insert(self, key, value):
        # Add to end
        self.heap.append((key, value))
        index = len(self.heap) - 1
        self.index_map[key] = index
        self._heapify_up(index)

    def search(self, key):
        index = self.index_map.get(key)
        if index is not None:
            return self.heap[index][1]
        return None

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index][0] > self.heap[parent_index][0]:  # compare by key (priority)
                self._swap(index, parent_index)
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        size = len(self.heap)
        while index < size:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < size and self.heap[left][0] > self.heap[largest][0]:
                largest = left
            if right < size and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def _swap(self, i, j):
        self.index_map[self.heap[i][0]] = j
        self.index_map[self.heap[j][0]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    # Optional: for removing top element
    def extract_max(self):
        if not self.heap:
            return None
        max_item = self.heap[0]
        last_item = self.heap.pop()
        if self.heap:
            self.heap[0] = last_item
            self.index_map[last_item[0]] = 0
            self._heapify_down(0)
        del self.index_map[max_item[0]]
        return max_item[1]
