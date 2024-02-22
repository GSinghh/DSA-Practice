class Node:
    def __init__(self, val) -> None:
        self.val = val
        self.next = None
        
class LinkedList: 
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.numNodes = 0
        
          
    #Adds a new node to the end of the list
    def append(self, val) -> None:
        if not self.head:
            newNode = Node(val)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(val)
            self.tail.next = newNode
            self.tail = newNode
            
    #Adds a new node to the beginning of the list    
    def prepend(self, val) -> None:
        if not self.head:
            newNode = Node(val)
            self.head = newNode
            self.tail = newNode
        else:
            newNode = Node(val)
            newNode.next = self.head
            self.head = newNode
    # #Delets the first occurence of a node with the given value 
    # def delete(self, val):
        
    # #Deletes the node at the specified position
    # def deleteAtPosition(self, val):
        
    # #Returns the number of nodes within the list
    def get_length(self) -> int:
        return self.numNodes
    
    # #Searches the list and returns a true if value exists, else returns false
    # def search(self, val):
        
    # #Reverses the list, returns reversed list
    # def reverse(self):
    
    # #Returns a boolean indicating if list is empty or not
    # def isEmpty(self):
    #     return self.numNodes == 0
    
    # #Returns the value of nth node in list
    # def getNthNode(self):
    
    # #Returns the Nth Node from the End
    # def getNthFromEnd(self):
    
    # #Returns the middle node
    # def getMiddleNode(self):
    #Prints every value within the list
    def print(self) -> None:
        curr = self.head
        
        while curr:
            print(curr.val)
            curr = curr.next
        
        
list1 = LinkedList()
list1.print()