class Stack:
    def __init__(self):
        self.stack = []
        
    def is_empty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.append(data)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            return None
    
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            return None
        
    def size(self):
        return len(self.stack)
    
    def print_stack(self):
        print(self.stack)
        
    def contains(self, item):
        return item in self.stack