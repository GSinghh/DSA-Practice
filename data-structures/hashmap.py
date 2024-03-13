class HashMap:
    def __init__(self):
        self.size = 10
        self.map = [None] * self.size
        self.load_factor = 0.7
    
    def get_hash(self, key):
        hash_val = 0
        for char in str(key):
            hash_val += ord(char)
        return hash_val % self.size
    
    def add(self, key, val):
        key_hash = self.get_hash(key)
        key_val = [key, val]
        
        if self.map[key_hash] is None:
            self.map[key_hash] = [key_val]
            return True
        else:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    pair[1] = val
                    return True
            self.map[key_hash].append(key_val)
            return True
    
    def get(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for pair in self.map[key_hash]:
                if pair[0] == key:
                    return pair[1]
        return None
    
    def delete(self, key):
        key_hash = self.get_hash(key)
        if self.map[key_hash] is not None:
            for i in range(len(self.map[key_hash])):
                if self.map[key_hash][i][0] == key:
                    self.map[key_hash].pop(i)
                    return True
        return False
    
    def display(self):
        for index, item in enumerate(self.map):
            if item is not None:
                print(f"Bucket {index}")
                for pair in item:
                    print(f"{pair[0]}:{pair[1]}")
                    
    def rehash(self):
        old_map = self.map
        self.size *= 2
        self.map = [None] * self.size
        for bucket in old_map:
            if bucket is not None:
                for pair in bucket:
                    self.add(pair[0], pair[1])
                    
    