class Set:
    def __init__(self) -> None:
        self.container = []
        
    def add(self, val):
        if val not in self.container:
            self.container.append()
    
    def remove(self, val):
        if self.contains(val):
            self.container.remove(val)
            
    def contains(self, val):
        return val in self.container if val else "Item not in set"
    
    def length(self):
        return len(self.container)
    
    def display(self):
        print(self.container, end=" ")