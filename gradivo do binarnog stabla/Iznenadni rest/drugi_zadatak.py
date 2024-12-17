#Dvostruko olančana lista
class knjigaNode:
  def __init__(self,naziv,autor, godina, ocjena, zanr, broj_stranica): #zanr,godina,ocjena):
    self.knjiga = {'naziv':naziv,'autor':autor,'godina':godina,'ocjena':ocjena, 'zanr': zanr, 'broj_stranica':broj_stranica}
    self.next=None
    self.prev=None

class DoubleLinkedList:
  def __init__(self,head=None):
    self.head=head

  def append(self,new_element):
    current=self.head
    if self.head:
      while current.next:
        current=current.next
      current.next=new_element
      new_element.prev=current
    else:
      self.head=new_element 

  def print_list(self):
    current=self.head
    while current:
      print(current.knjiga)
      current=current.next   

  def prepend(self,node):
    if self.head is None:
      self.head=node
      return
    node.next=self.head
    self.head.prev=node
    self.head=node

#prosjecna ocjena svih knjiga iz zadate godine
  def average_ocjena(self,godina):
    current=self.head
    sum=0
    brKnjiga=0
    while current:
      if current.knjiga['godina']==godina:
        sum+=1
        brKnjiga+=current.knjiga['ocjena']
      current=current.next
    if sum!=0:
      return f'Prosjecna ocjena za godinu {godina} je {brKnjiga/sum}'
    else:
      return None
    
#sve knjige cija je godina izdavanja veca ili jednaka zadatoj godini
  def godina_knjiga(self,min_godina):
    current=self.head
    while current:
      if current.knjiga['godina']>=min_godina:
        print(current.knjiga)
      current=current.next 

#za brojanje knjiga odredjenog zanra
  def zanr_counter(self,zanr):
    current=self.head
    counter=0
    while current:
      if current.knjiga['zanr']==zanr:
        counter+=1
      current=current.next
    return f'Knjiga zanra {zanr} ima {counter}'  
  
#brisanje knjige iz liste na osnovu naziva  
  def delete_by_naziv(self, naziv):
      current = self.head
      while current:
          if current.knjiga['naziv'] == naziv: 
              if current == self.head:
                self.head = current.next
                if self.head:
                    self.head.prev = None
                if current == self.tail:
                    self.tail = None
              elif current == self.tail:         
                  self.tail = current.prev
                  self.tail.next = None
              else:                               
                  current.prev.next = current.next
                  current.next.prev = current.prev
              return True
          current = current.next
      return False
  
#azuriranje ocjene knjige na osnovu naziva
  def id_set_Avg (self, naziv,nova_ocjena):
      current = self.head
      while current:
          if current.knjiga['naziv'] == naziv:
            current.knjiga['ocjena'] = nova_ocjena
            return True
          current = current.next
      return False   
  
#pronalazi i ispisuje sve knjige odredjenog autora
  def print_filmovi(self, autor):
        current = self.head
        while current:
            if current.knjiga['autor'] == autor:
                print(current.knjiga)
                current = current.next

#ispisivanje svih knjiga koje imaju vise od zadatog broja stranica
  def knjige_iznad_broja_stranica(self, broj_stranica):
      current = self.head
      while current:
          if current.knjiga['broj_stranica'] > broj_stranica:
              print(current.knjiga)
          current = current.next
#kreiranje knjiga kao cvor
knjiga1=knjigaNode('Beautiful Creatures','fiction',2002,8.7)
knjiga2=knjigaNode('The Fault in our stars','fiction',2002,9.5)  
knjiga3=knjigaNode('The little prince','fiction',1990,10)  


l=DoubleLinkedList()

l.append(knjiga1)
l.append(knjiga2)
l.append(knjiga3)

print(l.zanr_counter('fiction'))
print(l.average_ocjena())


