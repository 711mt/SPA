class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
class CircularLinkedList:
  def __init__(self, head=None):
    self.head=head
  def prepend(self, new_node):
    current=self.head
    new_node.next=self.head
    if not self.head:
      new_node.next=new_node
    else:
      while current.next != self.head:
        current=current.next
      current.next=new_node
    self.head=new_node
  #stampanje cirkularne liste
  def print_list(self):
    current=self.head
    while current:
      print(current.value)
      current=current.next
      if current==self.head:
        break

clista=CircularLinkedList()
n1=Node(1)
n2=Node(2)
clista.prepend(n1)
clista.prepend(n2)
clista.print_list() # Output --> 2,1