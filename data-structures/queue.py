class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0
        
    def enqueue(self, item):
        self.queue.append(item)
        
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop()
        else:
            return None
            
    def size(self):
        return len(self.queue)
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.queue[-1]
    
    def contains(self, item):
        return item in self.queue