class Node:
  def __init__(self, value):
    self.value=value
    self.prev=None
    self.next=None
class DoublyLinkedList:
  def __init__(self,head=None):
    self.head=head
  
  #stampanje liste
  def print_list(self):
    current=self.head
    while current:
      print(current.value)
      current=current.next
  #stampanje cvora na pocetak liste
  def prepend(self,new_node):
    if self.head is None:
      self.head=new_node
      return
    new_node.next=self.head
    self.head.prev=new_node
    self.head=new_node

  #brisanje sa pocetka
  def delete_first(self):
    if self.head is None:
      return "Lista je prazna"
    if self.head.next is None:
      self.head=None
    self.head=self.head.next
    self.prev=None
  #brisanje sa kraja
  def delete_last(self):
    if self.head is None:
      return "Lista je prazna"
    if self.head.next is None:
      self.head=None
    current=self.head
    while current.next: #is not None
      current=current.next
    current.prev.next=None
    current.prev=None
  #srednji element
  def get_middle_node(self):
    current_1=self.head #A
    current_2=self.head 
    while current_1:
      current_1=current_1.next.next #element C
      current_2=current_2.next #element B
    return current_2
  #dve liste iste?
  def __eq__(self,other): #l1,l2
    current_1 = self.head
    current_2=other.head
    while current_1 and current_2:
      if current_1.value == current_2.value:
        current_1=current_1.next
        current_2=current_2.next
    if not current_1 and not current_2:
      return True
    else:
      return False
  #funkcija koja mice duplikate iz liste
  def remove_duplicates(self):
    current_1=self.head
    current_2=self.head
    while current_1.next:
      while current_2.next:
        if current_2.next.value == current_1.value:
          current_2.next=current_2.next.next
        else:
          current_2=current_2.next
      current_1 = current_1.next
      current_2=current_1
  

  """
   def link_lists(self, l2):
        
        current_1 = self.head
        while current_1.next:
            current_1 = current_1.next
        current_1.next = l2.head
        self.print_list()

    def delete_val(self, value, key):
        current = self.head
        prev = None
        while current.value[key] != value and current.next:
            prev = current
            current = current.next
        if current.value[key] == value:
            if prev:
                prev.next = current.next
            else:
                self.head = current.next

    def __contains__(self, data):
        if self.head == None:
            return False
        else:
            current = self.head
            while current:
                if current.value['cijena'] == data:
                    return True
                current = current.next
            return False
    def remove_largest_elements(self):
        maximum = -1
        current = self.head
        while current != None:
            if maximum < current.value['cijena']:
                maximum = current.value['cijena']
            current = current.next
        while maximum in self:
            self.delete_val(maximum, 'cijena')

    def remove_smallest_elements(self):
        minimum = 1000
        current = self.head
        while current:
            if minimum > current.value['cijena']:
                minimum = current.value['cijena']
            current = current.next
        self.delete_val(minimum, 'cijena')
    
    # {...., "godina": 2, "prosjek": 9} <-> {...., "godine":2, "prosjek": 8}] ; (9 + 8) / 2 = 8.5

    def prosjek_godine(self, year):
        zbir = 0
        broj_studenata_zadate_godine = 0
        current = self.head
        while current:
            if current.value["godina"] == year:
                zbir += current.value["prosjek"]
                broj_studenata_zadate_godine += 1
            current = current.next
        return zbir / broj_studenata_zadate_godine
    
    # 2 <-> 4 <-> 6 <-> 8 <-> 10 ; 3              output: 4 <-> 2
    def stampa_prije_indeksa(self, index):
        current = current.head
        count = 1
        while count < index:
            current = current.next
            count += 1
        previus = current
        while previus:
            print(previus.value)
            previus = previus.prev
  """

class Narudzba:
 def __init__(self, ime_klijenta:str, naziv_jela:str,
vrijeme_narudzbe:int, prioritet:int):
  self.narudzba = {
 'ime_klijenta' : ime_klijenta,
 'naziv_jela' : naziv_jela,
 'vrijeme_narudzbe' : vrijeme_narudzbe,
 'prioritet' : prioritet
 }
  self.next = None
  self.prev = None
class DoubleListNarudzbe:
 def __init__(self,head=None,tail=None):
  self.head = head
  self.tail = tail
 #1 dodavanje na poceta
  def dodaj_na_pocetak(self, narudzba:Narudzba):
   if self.head is None:
    self.head = narudzba
    self.tail = narudzba
   else:
    current = self.head
    current.prev = narudzba
    narudzba.next = current
    self.head = narudzba
 #2 dodaj na kraj
 def dodaj_na_kraj(self, narudzba:Narudzba):
  if self.head is None:
   self.head = narudzba
   self.tail = narudzba
  else:
   current = self.tail
   current.next = narudzba
   narudzba.prev = current
   self.tail = narudzba
 def print_list(self):
  if self.head is None:
   return "Ne postoje cvorovi u listi"
  else:
   current = self.head
   while current:
    print(current.narudzba)
    current=current.next
 #3 brisanje po imenu
 def del_po_imenu(self, ime:str):
  if self.head is None:
   return "Lista nema cvorova"
  else:
   if self.head.narudzba['ime_klijenta'].lower() == ime.lower():
    current = self.head
    self.head = self.head.next
    self.head.prev = None
    current.next = None
   else:
    current = self.head
    prev = None
    while current:
     if current.narudzba['ime_klijenta'].lower() == ime.lower():
        prev.next = current.next
        if current.next:
          current.next.prev = prev
        current.next = None
        current.prev = None
     prev = current
     current = current.next
 #4 print po prioritetu
 def print_po_prioritetu(self):
  prioritet_1 = []
  prioritet_2 = []
  current = self.head
  while current:
    if current.narudzba['prioritet'] == 1:
      prioritet_1.append(current)
    else:
      prioritet_2.append(current)
    current = current.next
  print("Narudzbe sa vecim prioritetom su: \n" + "\
n".join([str(cvor.narudzba) for cvor in prioritet_1]))
  print("Narudzbe sa manjim prioritetom su: \n" + "\
n".join([str(cvor.narudzba) for cvor in prioritet_2]))
 #5 broj narudzbi nakon zadatog vremena
 def br_narudzbi_vrijeme(self, zadato_vrijeme:int):
   if self.head is None:
     return "Nemamo cvorova u listi"
   count = 0
   current = self.head
   while current:
      if current.narudzba['vrijeme_narudzbe']>zadato_vrijeme:
       count+=1
      current = current.next
      return f"Broj narudzbi koje su narucene nakon zadatog vremena je
{count}"
 #6 brisanje poslednje narudzbe
 def brisanje_poslednje_narudzbe(self):
   if self.head is None:
     return "Nista"
   else:
    current = self.tail
    current.prev.next = None
    self.tail = current.prev
    current.prev = None

narudzba1 = Narudzba("Marko Markovic", 'Pizza', 540, 1)
narudzba2 = Narudzba("Jelena Jovanovic", 'Pasta', 600, 2)
narudzba3 = Narudzba("Petar Petrovic", 'Salata', 480, 1)
narudzba4 = Narudzba("Ana Anic", 'Burger', 720, 2)
narudzba5 = Narudzba("Ivan Ivanovic", 'Biftek', 800, 1)
double_list_narudzbe = DoubleListNarudzbe()
double_list_narudzbe.dodaj_na_pocetak(narudzba1)
double_list_narudzbe.dodaj_na_pocetak(narudzba2)
double_list_narudzbe.dodaj_na_pocetak(narudzba3)
double_list_narudzbe.dodaj_na_pocetak(narudzba4)
double_list_narudzbe.dodaj_na_pocetak(narudzba5)