class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self) -> None:
        self.root = None
        
    # Returns True if the BST is empty, False otherwise
    def is_empty(self) -> bool: 
        return self.root == None
        
    # Insert a new node with the given value into the BST.
    def insert(self, value) -> None: 
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)
        
    # Insert helper function
    def _insert(self, value, node) -> None:
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert(value, node.left)
        elif value > node.value:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert(value, node.right)
        else:
            print("Value is already in the tree")
            
    #Searches for a node with a given value in the BST
    def search(self, value) -> bool:
        if self.root:
            return self._search(value, self.root)
        else:
            return False
        
    # Search helper function
    def _search(self, value, node) -> bool:
        if node.value == value:
            return True
        elif value < node.value:
            return self._search(value, node.left)
        elif value > node.value:
            return self._search(value, node.right)
        else:
            return False
        
    # Find minimum value
    
    def min_value(self):
        curr = self.root
        
        while curr.left is not None:
            curr = curr.left
        return curr.value
    
    # Find Maximum value
    
    def max_value(self):
        curr = self.root
        
        while curr.right is not None:
            curr = curr.right
        return curr.value
    
    # Preorder traversal: Root -> Left -> Right
    def preorder(self, node):
        if node is not None:
            return
        print(node.value, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
        
    # Inorder traversal: Left -> Root -> Right    
    def inorder(self, node):
        if node is not None:
            return
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)
        
    # Postorder traversal: Left -> Right -> Root
    def postorder(self, node):
        if node is not None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end=" ")
        
        
        
        