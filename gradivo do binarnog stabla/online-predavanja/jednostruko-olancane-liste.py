#klasa koja predstavlja čvor 
class Node:
  def __init__(self,value):
    self.value=value
    self.next=None #pokazivac next je none, imamo jedan cvor

#klasa koja predstavlja jednostruko olancane liste
class LinkedList:
  def __init__(self,head=None):
    self.head=head
  #prepend - dodavanje cvora na pocetak liste
  def prepend(self, new_element):
    new_element.next = self.head
    self.head=new_element
  #append --> teza od prepend, dodavanje cvora na kraj liste
  def append(self, new_element):
    current= self.head
    if self.head:
      while current.next:
        current = current.next
      current.next=new_element
    else:
      self.head=new_element
  #funkcija za stampanje liste 
  def print_list(self):
    current=self.head
    if self.head:
      while current.next:
        print(current.value)
        current = current.next
  #brisanje prvog elementa
  def delete_first(self):
    if not self.head: #ako je lista prazna
      return None
    else:
      self.head = self.head.next
  #brisanje zadnjeg elementa
  def delete_last(self):
    current=self.head
    while current.next:
      prev=current
      current = current.next
    prev.next = None
  #funkcija za uzimanje vrednosti elementa sa neke pozicije
  def get_value_from_position(self,position):
    counter=1
    current=self.head
    if position<1:
      return None
    while current and counter <= position:
      if counter==position:
        return current
      current=current.next
      counter+=1
    return None
  #stampanje(vracanje) elemenata sa svake druge pozicije liste
  def svaka_druga(self):
    current=self.head
    i=0
    while current:
      if i%2==0:
        print(current.data)
        current=current.next
        i+=1
  #insert
  def insert_on_position(self,new_element,position):
    counter=1
    current=self.head
    if position>1:
      while current and counter < position:
        if counter == position-1:
          new_element.next = current.next
          current.next=new_element
        current=current.next
        counter+=1
      return None
    elif position == 1:
      new_element.next=self.head
      self.head=new_element
    else:
      return None
  # funkcija za brisanje odredjene vrednosti
  def del_val(self,value):
    current=self.head
    prev=None
    while current.value != value and current.next:
      prev=current
      current=current.next
    if current.value == value:
      if prev: #ako postoji prev
        prev.next = current.next
      else:
        self.head = current.next
  # delete from the position
  def delete_from_position(self, position):
    current=self.head
    if position == 1:
      self.head = current.next
      current - None
    prev = None
    counter=0
    while current and counter != position:
      prev=current
      current=current.next
      counter+=1
    if current is None:
      return None
    prev.next = current.next
    current=None
  #funkcija koja racuna duzinu liste
  #prvi nacin
  def len_iterative(self):
    count=0
    current=self.head
    while current:
      current=current.next
      count+=1
    return count
  # drugi nacin - rekurzivno
  def getCountRec(self,node):
    if not node:
      return 0
    else:
      return 1+self.getCountRec(node.next)
  #
  def len_recursive(self):
    return self.getCountRec(self.head)
  #stampanje elemenata koji su samo parni
  def parni(self):
    current=self.head
    while current:
      if current.value %2 == 0:
        print(current.value)
      current = current.next
'''
  #za svakog takmicara imamo score, kao rezultat je potrebno prikazati skoro sve takmicare ciji je rezultat 15% veci od proseka
  # svih takmicara i trebamo iskoristiti jednostruku olancanu listu
  def average(self):
     current=self.head
     value=0
     broj=0
     while current:
       value+=current.value
       broj+=1
       current=current.next
     return value/broj
    #drugi dio zadatka - stampanje vrednosti cvorova koji su vexi 15% od prosecnog
    if current.value> average*1.15:
    print(current.data)
    current=current.next
  
    
'''

# a) Input: 5 -> 4 -> 3 -> 8 -> 2; Output: 16 -> 64 -> 4
def parni_kvadrati(self):
        l2 = LinkedList()
        current = self.head
        while current:
            if current.value % 2 == 0:
                cvor = Node(current.value ** 2)
                l2.append(cvor)
            current = current.next
        
        l2.print_list()

# b) Input: 5 -> 4 -> 3 -> 8 -> 2; Output: 5 -> 3 -> 2
def delete_every_second(self):
        current = self.head
        current2 = current.next
        while current.next:
            current_2 = current.next
            current.next = current_2.next
            current = current.next
        self.print_list()
# jednostruko olancana lista je najjednostavnija struktura



n1=Node(5) #prvi cvor
n2=Node(7)
n3=Node(3)
n4=Node(2)
l1=LinkedList() #prazna
l1.prepend(n4) # --> 2    ^
l1.prepend(n3) # --> 3   /
l1.prepend(n2) # --> 7  /
l1.prepend(n1) # --> 5 /
print("Vrijednost prvog cvora je: " + str(n1.value)) #output 5
print("Stampanje liste: ") 
l1.print_list()
l1.delete_first()
l1.print_list()
print(l1.get_value_from_position(2).value) #vraca nam Node poziciju u memoriji, output --> 3


