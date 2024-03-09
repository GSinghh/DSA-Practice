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
    def min_value(self) -> int:
        curr = self.root
        
        while curr.left is not None:
            curr = curr.left
        return curr.value
    
    # Find Maximum value
    def max_value(self) -> int:
        curr = self.root
        
        while curr.right is not None:
            curr = curr.right
        return curr.value
    
    # Preorder traversal: Root -> Left -> Right
    def preorder(self, node) -> None:
        if node is not None:
            return
        print(node.value, end=" ")
        self.preorder(node.left)
        self.preorder(node.right)
        
    # Inorder traversal: Left -> Root -> Right    
    def inorder(self, node) -> None:
        if node is not None:
            return
        self.inorder(node.left)
        print(node.value, end=" ")
        self.inorder(node.right)
        
    # Postorder traversal: Left -> Right -> Root
    def postorder(self, node) -> None:
        if node is not None:
            return
        self.postorder(node.left)
        self.postorder(node.right)
        print(node.value, end=" ")
        
        
    # Depth first search recursive implementation    
    
    def dfs_recursive(self, node):
        if node:
            print(node.value, end=" ")
            self.dfs_recursive(node.left)
            self.dfs_recursive(node.right)
    
    # Depth first search iterative implementation
    
    def dfs_iterative(self):
        stack = [self.root]
        while stack:
            node = stack.pop()
            if node:
                print(node.value, end=" ")
                stack.append(node.right)
                stack.append(node.left)
                
    # Breadth first search iterative implementation
    
    def bfs_iterative(self):
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if node:
                print(node.value, end=" ")
                queue.append(node.left)
                queue.append(node.right)
                
    #Breadth first search recursive implementation
    
    def bfs_recursive(self, queue):
        queue = [self.root]
        self._bfs_recursive(queue)
        
    # Breadth first search recursive helper    
    
    def _bfs_recursive(self, queue):
        if not queue:
            return
        
        node = queue.pop(0)
        print(node.value, end=" ")
        
        if node.left:
            queue.append(node.left)
        if node.right: 
            queue.append(node.right)
        
        self._bfs_recursive(queue)
                