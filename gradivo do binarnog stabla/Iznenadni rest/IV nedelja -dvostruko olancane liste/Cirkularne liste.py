# Python code of insert node at begin in 
# doubly Circular linked list.

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
        self.prev = None

def insertAtBeginning(head, newData):
    newNode = Node(newData)
    
    if head is None:
      
        # List is empty
        newNode.next = newNode.prev = newNode
        head = newNode
    else:
      
        # List is not empty
        last = head.prev 

        # Insert new node
        newNode.next = head
        newNode.prev = last
        head.prev = newNode
        last.next = newNode
        
        # Update head
        head = newNode
    
    return head

def printList(head):
    if not head:
        return
    curr = head
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == head:
            break
    print()

# Linked List : 10<->20<->30
head = Node(10)
head.next = Node(20)
head.next.prev = head
head.next.next = Node(30)
head.next.next.prev = head.next
head.next.next.next = head
head.prev = head.next.next

head = insertAtBeginning(head, 5)
printList(head)
#Time Complexity: O(1), Since we are not traversing the list.
'''
Insertion at the End in Doubly Circular Linked List – O(1) Time and O(1) Space:
To insert a new node at the end of doubly circular linked list,

Allocate memory for the new node.
If the list is empty, set the new node’s next and prev pointers to point to itself, and update the head to this new node.
For a non-empty list, insert the new node:
Find the current last node (the node whose next pointer points to the head).
Set the new node’s next pointer to point to the head.
Set the new node’s prev pointer to point to the current last node.
Update the current last node’s next pointer to point to the new node.
Update the head’s prev pointer to point to the new node.
'''
# Python code of insert node at End in 
# doubly Circular linked list.

class Node:
    def __init__(self, x):
        self.data = x
        self.next = self.prev = None

def insert_at_end(head, new_data):
    new_node = Node(new_data)
    
    if head is None:
      
        # List is empty
        new_node.next = new_node.prev = new_node
        head = new_node
    else:
      
        # List is not empty
        last = head.prev 
        
        # Insert new node at the end
        new_node.next = head
        new_node.prev = last
        last.next = new_node
        head.prev = new_node
    
    return head

def print_list(head):
    if head is None:
        return
    curr = head
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == head:
            break
    print()

if __name__ == "__main__":
  
    # Linked List : 10<->20<->30
    head = Node(10)
    head.next = Node(20)
    head.next.prev = head
    head.next.next = Node(30)
    head.next.next.prev = head.next
    head.next.next.next = head
    head.prev = head.next.next

    head = insert_at_end(head, 5)
    print_list(head)

'''
Insertion after a given node in Doubly Circular Linked List – O(n) Time and O(1) Space:
To insert a new node after a given node in doubly circular linked list,

Allocate memory for the new node.
Traverse the list to locate given node.
Insert the newNode:
Set newNode->next to given node’next.
Set newNode->prev to givenNode.
Update givenNode->next->prev to newNode.
Update givenNode->next to newNode.
If givenNode is the last node (i.e., points to head), update head->prev to newNode.
'''
# Python code to insert a node after a given node 
# in a doubly circular linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

# Function to insert a node after a given node in 
# the doubly circular linked list
def insertAfterNode(head, newData, givenData):
    newNode = Node(newData)
    
    # If the list is empty, return None
    if not head:
        return None
    
    # Find the node with the given data
    curr = head
    while True:
        if curr.data == givenData:
            
            # Insert the new node after the given node
            newNode.next = curr.next
            newNode.prev = curr

            curr.next.prev = newNode
            curr.next = newNode

            # If the given node was the last node,
            # update head's prev
            if curr == head.prev:
                head.prev = newNode
            
            # Return the updated head
            return head

        curr = curr.next
        if curr == head:
            break

    return head

def printList(head):
    if not head:
        return
    curr = head
    while True:
        print(curr.data, end=" ")
        curr = curr.next
        if curr == head:
            break
    print()

if __name__ == "__main__":
  
    # Linked List : 10<->20<->30
    head = Node(10)
    head.next = Node(20)
    head.next.prev = head
    head.next.next = Node(30)
    head.next.next.prev = head.next
    head.next.next.next = head
    head.prev = head.next.next

    head = insertAfterNode(head, 5, 10)
    printList(head)
