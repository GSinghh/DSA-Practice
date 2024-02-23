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
            
        self.numNodes += 1
        
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
            
        self.numNodes += 1
    
    #Delets the first occurence of a node with the given value 
    def delete(self, val):
        if self.isEmpty():
            return
        else:
            curr, prev = self.head, None
            while curr:
                if curr.val == val and prev == None:
                    self.head = self.head.next
                elif curr.val == val and curr.next == None:
                    self.tail = prev
                    prev.next = None
                else:
                    prev.next = curr.next
                prev = curr
                curr = curr.next
        self.numNodes -= 1
        
    #Deletes the node at the specified position
    def deleteAtPosition(self, position):
        if self.isEmpty():
            return "List is Empty"
        if position > self.get_length():
            return "Index out of bounds"
        if position == 1:
            self.head = self.head.next
            return
        
        curr, prev, index = self.head, None, 1
        
        while curr and index != position:
            if position == index and curr.next == None:
                self.tail = prev
                prev.next = None
            else:
                prev.next = curr.next
            prev = curr
            curr = curr.next
            index += 1
            
        self.numNodes -= 1
        
    #Returns the number of nodes within the list
    def get_length(self) -> int:
        return self.numNodes
    
    #Searches the list and returns a true if value exists, else returns false
    def search(self, val) -> bool:
        curr = self.head
        
        while curr:
            if curr.val == val:
                return True
            curr = curr.next
        return False
        
    #Reverses the list, returns head of reversed list
    def reverse(self):
        curr, prev = self.head, None
        
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        return self.printList(prev)
    
    #Returns a boolean indicating if list is empty or not
    def isEmpty(self) -> None:
        return self.head == None
    
    #Returns the value of nth node in list
    def getNthNode(self, position):
        if self.isEmpty:
            return "List is Empty"
        if position > self.get_length():
            return "Index out of bounds"
        
        curr = self.head
        while position > 0 and curr:
            curr = curr.next
            position -= 1
            
        return curr.val
            
    #Returns the value of the Nth Node from the End
    def getNthFromEnd(self, position):
        if self.isEmpty():
            return "List is Empty"
        if position > self.get_length():
            return "Index out of bounds"
        
        slow, fast = self.head, self.head
        
        while position > 0:
            fast = fast.next
            position -= 1
            
        while fast:
            slow = slow.next
            fast = fast.next
        return slow.val
    
    #Returns the value of the middle node
    def getMiddleNode(self) -> int:
        slow, fast = self.head, self.head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.val
        
    #Prints every value within the list
    def print(self) -> None:
        curr = self.head
        
        while curr:
            print(curr.val)
            curr = curr.next
        
    #Prints value in the list when head is given as parameter
    def printList(self, head) -> None:
        curr = head
        
        while curr:
            print(curr.val)
            curr = curr.next
            
        
list1 = LinkedList()
list1.print()