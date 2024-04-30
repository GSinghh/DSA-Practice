class TrieNode:
    def __init__(self, char = None) -> None:
        self.char = char
        self.next = None
        self.is_end_of_word = False
        
class Trie:
    def __init__(self) -> None:
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for char in word:
            if node.next is None:
                node.next = TrieNode(char)
            node = node.next
        node.is_end_of_word = True
        
    def search(self, word):
        node = self.root
        for char in word:
            if node.next.val != char:
                return False
            node = node.next
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char != node.char:
                return False
            node = node.next
        return True
    
trie = Trie()
trie.insert("Apple")
print(trie.search("Apple"))