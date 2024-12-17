#Dvostruko olancane liste
class Node:
  def __init__(self,value):
    self.next = None
    self.prev = None
    self.value = value
  
class DoubleList:
  def __init__(self,head=None,tail=None):
    self.head = head
    self.tail = tail
  def append(self,element):
    if self.head is None:
      self.head = element
      self.tail = element
    else:
      current = self.tail
      current.next = element
      element.prev = current
      self.tail = element
  def get_list_length_from_tail(self):
    if self.head is None:
      return "Lista je prazna"
    else:
      current= self.tail
      duzina_liste = 0
      while current:
        duzina_liste+=1
        current = current.prev
      return duzina_liste
    
  def print_list(self):
    if self.head is None:
      return "Lista je prazna"
    else:
      current = self.head
      while current:
        print(current.value)
        current = current.next
  
  def delete_last(self):
    if self.head is None:
      return "Lista je prazna"
    elif self.get_list_length_from_tail() == 1:
      self.head = None
      self.tail = None
    else:
      current = self.tail
      self.tail = current.prev
      self.tail.next = None
      current.prev = None
    
    #metoda koja uklanja n-elemenata sa kraja liste
  def remove_n(self,N):
    list_length = self.get_list_length_from_tail()
    if list_length <= N:
      self.head = None
      self.tail = None
    else:
      while N:
        self.delete_last()
        N -= 1
      

node1 = Node(4)
node2 = Node(7)
node3 = Node(15)
node4 = Node(2)
node5 = Node(25)

doubleList = DoubleList()

doubleList.append(node1)
doubleList.append(node2)
doubleList.append(node3)
doubleList.append(node4)
doubleList.append(node5)
print(doubleList.get_list_length_from_tail())
doubleList.print_list()

doubleList.remove_n(2)
doubleList.print_list()
doubleList.delete_last()
doubleList.print_list()


