class Heap:
    def __init__(self) -> None:
        self.heap = []
        
    def parent(self, index):
        return (index - 1) // 2
    
    def insert(self, data):
        self.heap.append(data)
        self.percolate_up(len(self.heap) - 1)
        
    def percolate_up(self, index):
        if index <= 0:
            return
        parent_index = self.parent(index)
        if self.heap[parent_index] < self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self.percolate_up(parent_index)
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def delete(self):
        if self.is_empty():
            return None
        max_val = self.heap[0]
        self.heap[0] = self.heap[len(self.heap) - 1]
        self.heap.pop()
        self.heapify(0)
        return max_val
        
    def heapify(self, index):
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        largest = index
        if not self.is_empty() and left_index < len(self.heap) and self.heap[left_index] > self.heap[largest]:
            largest = left_index
        if not self.is_empty and right_index < len(self.heap) and self.heap[right_index] > self.heap[largest]:
            largest = right_index
        if largest != index:
            self.heap[largest], self.heap[index] = self.heap[index], self.heap[largest]
            self.heapify(largest)
            