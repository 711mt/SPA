# zadatak 1
class Pacijent:
 def __init__(self, ime_prezime:str, godina_rodjenja:int,
   dijagnoza:str, br_dana_bolnica:int):
   self.patient_data = {
 'ime_prezime': ime_prezime,
 'godina_rodjenja': godina_rodjenja,
 'dijagnoza': dijagnoza,
 'br_dana_bolnica':br_dana_bolnica
 }
   self.next = None
class LinkedListPatients:
  def __init__(self, head=None):
   self.head = head
 #1 dodavanje na pocetak liste (prepend)
  def add_to_list(self, pacijent:Pacijent):
   if self.head is None:
    self.head = pacijent
   else:
    current = self.head
    pacijent.next = current
    self.head = pacijent
 #2 brisanje pacijenta po imenu
  def delete_by_name(self, name:str):
    if self.head is None:
      return "U listi nema pacijenata"
    else:
     current = self.head
     prev = self.head
    while current:
      if current.patient_data['ime_prezime'].lower() ==name.lower():
        prev.next = current.next
        current.next = None
      prev = current
      current = current.next
 #3 prosjecan broj dana po dijagnozi
  def avg_day_by_diagnosis(self, diagnosis:str):
     average = 0
     count = 0
     if self.head is None:
      return "Prosjecan broj je 0, lista je prazna" #ili samo integer 0
     else:
      current = self.head
      while current:
         if current.patient_data['dijagnoza'].lower() ==diagnosis.lower():
           count += 1
           average += current.patient_data['br_dana_bolnica']
         current = current.next
      average = average / count
      return "Prosjecan br dana u bolnici je " + str(average)

#4 pronalazak pacijenta sa najduzim boravkom
  def find_longest_stay(self):
    if self.head:
      longest_stay = self.head
      current = self.head.next
      while current:
        if longest_stay.patient_data['br_dana_bolnica'] <current.patient_data['br_dana_bolnica']:
           longest_stay = current
        current = current.next
      return "Pacijent sa najduzim boravkom u bolnici je: " +str(longest_stay.patient_data)
 #5 brojanje pacijenata starijih od zadate godine
  def count_by_age(self, age:int):
    if self.head is None:
      return None
    else:
      count = 0
      current = self.head
      while current:
        if 2024 - current.patient_data['godina_rodjenja'] > age:
          count += 1
        current = current.next
      return "Br pacijenata starijih od zadate godine je: " +str(count)
 #6 implementirati samostalno :)
def pretraga_po_dijagnozi(self, dijagnoza):
    current = self.head
    found = False
    while current is not None:
         if current.dijagnoza == dijagnoza:
            print(f"Pacijent: {current.ime}, Godina rođenja: {current.godina_rodjenja}, "
                    f"Broj dana u bolnici: {current.broj_dana_u_bolnici}")
            found = True
         current = current.next
    if not found:
        print(f"Nema pacijenata sa dijagnozom: {dijagnoza}")
#7 implementirati samostalno :)
def broj_pacijenata_mladjih_od_30(self, trenutna_godina):
    current = self.head
    broj_pacijenata = 0
    while current is not None:
        starost = trenutna_godina - current.godina_rodjenja
        if starost < 30:
            broj_pacijenata += 1
        current = current.next
    return broj_pacijenata
 
 #8 stampanje svih pacijenata
def print_patient_list(self):
     current = self.head
     while current:
        print(current.patient_data)
        current = current.next

pacijent_1 = Pacijent("Marko Markovic", 1990, 'Gripa', 5)
pacijent_2 = Pacijent("Jelena Jovanovic", 1990, 'Upala pluca', 3)
pacijent_3 = Pacijent("Ivo Ivic", 1999, 'Anksioznost', 10)
pacijent_4 = Pacijent("Ana Anic", 1975, 'Upala pluca', 15)
pacijent_5 = Pacijent("Ivan Ivanovic", 1995, 'Migrena', 2)
lista_pacijenata = LinkedListPatients()
lista_pacijenata.add_to_list(pacijent_1)
lista_pacijenata.add_to_list(pacijent_2)
lista_pacijenata.add_to_list(pacijent_3)
lista_pacijenata.add_to_list(pacijent_4)
lista_pacijenata.add_to_list(pacijent_5)
# Pretraga pacijenata po dijagnozi
print("Pacijenti sa dijagnozom 'Grip':")
lista_pacijenata.pretraga_po_dijagnozi("Grip")

# Izračunavanje broja pacijenata mlađih od 30 godina
trenutna_godina = 2024
print("\nBroj pacijenata mlađih od 30 godina:", lista_pacijenata.broj_pacijenata_mladjih_od_30(trenutna_godina))


#1 Kreirati jednostruko olancanu listu
'''
a) Podatke unositi na kraju liste
b) Podatke unositi na pocetku liste
c) Napisati funkciju za printanje liste
d) Napisati funkciju za pronalazak maksimalnog elementa u listi
e) Brisanje maksimalnog elementa iz liste
f) Kvadrirati svaki element u listi
g) Naci broj elemenata u listi
i) Obrisati prvi element u listi
'''
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self,head=None):
        self.head=head
        #funkcija za dodavanje elementa na kraju liste
    def append(self,new_element):
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=new_element
        else:
            self.head=new_element
        #funkcija za dodavanje elementa na pocetku liste
    def prepend(self,new_element):
        new_element.next=self.head
        self.head=new_element
    #printanje liste
    def print_list(self):
        current=self.head
        while current:
            print(current.value)
            current=current.next
    #funkcija za pronalazak maksimalnog elementa u listi
    def pronadji_max(self):
        if self.head is None:
            print("Lista je prazna.")
        else:
            current=self.head
            max_element = self.head
            while current:
                if current.value > max_element.value:
                    max_element = current
                current=current.next
            return max_element
    
    #funkcija za brisanje maksimalnog elementa iz liste
    def brisanje_max(self):
        current=self.head 
        max = self.pronadji_max()
        while current:
            if current.next.value == max.value:
                current.next = current.next.next
            current=current.next


    #funkcija za kvadriranje svakog elementa u listi
    def kvadriranje(self):
        current=self.head
        while current:
            print(current.value*current.value)
            current=current.next
            
    
    #funkcija za broj elemenata u listi
    def broj_elemenata(self):
       brojac=0
       current =self.head
       while current:
           current=current.next
           brojac+=1
       return brojac

    #funkcija za brisanje prvog elementa u listi
    def brisanje_prvog(self):
        if not self.head:
            return None
        else:
            self.head=self.head.next

n1=Node(1)
n2=Node(2)
n3=Node(3)
n4=Node(4)
n5=Node(5)
l1=LinkedList()
l1.prepend(n5)
l1.prepend(n4)
l1.prepend(n3)
l1.prepend(n2)
l1.prepend(n1)
#l1.broj_elemenata()
#l1.brisanje_prvog()
#l1.kvadriranje()
l1.print_list()

#2 Druga olancana lista
 
#varijabla = ["dejan",1,{},(0,)]
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,head=None):
        self.head = head
#dodavanje elemenata na pocetak liste
    def prepend(self,new_element):
       if self.head == None:
         self.head = new_element
       new_element.next = self.head
       self.head = new_element
#dodavanje elemenata na kraj liste
    def append(self,new_element):
      current=self.head
      if self.head:
        while current.next: #dok current.next postoji
             current = current.next
        current.next = new_element
      else:
        self.head = new_element

    def print_list(self):
       current = self.head
       if self.head:
         while current.next:
            print(current.value)
            current=current.next
         print(current.value)
       else:
          print(current.value)
#metoda koja uklanja prvi element liste
    def uklanjanje_prvog_elementa(self):
       current=self.head
       self.head=self.head.next
       current.next=None
#metoda koja uklanja zadnji element liste
    def uklanjanje_zadnjeg_elementa(self):
       current=self.head
       while current.next.next:
          current=current.next
       current.next=None
    def drugi_nacin_uklanjanje_zadnjeg_elementa(self):
       current=self.head
       while current:
          if current.next and not current.next.next:
             current.next=None
          else:
             current=current.next
    def treci_nacin_uklanjanje_zadnjeg_elementa(self):
       current=self.head
       previous=self.head
       while current.next:
          previous=current
          current=current.next
       previous.next=None
#metoda koja ce vracati cvor na n-toj poziciji
    def get_value_from_position(self,position):
       current=self.head
       count=1
       if position <= 1:
          return current
       else:
          while current.next:
             if count == position:
                print(current.value)
                break
             else:
                current=current.next
                count+=1
#metoda za duzinu liste
    def duzina_lista(self):
       current=self.head
       if self.head:
          len=1
          while current.next:
             current=current.next
             len+=1
          print("Duzina liste je " + str(len))
       else:
          print("Duzina liste je 0")
#rekurzija za duzinu liste
    def length_recursively(self,node):
       if not node:
          return 0
       else:
          return 1 + self.length_recursively(node.next)
      
       
node1=Node(4)
node2=Node(5)
node3=Node(12)
node4=Node(7)

linked_list=LinkedList(node1)
linked_list.prepend(node2)
linked_list.prepend(node3)
linked_list.prepend(node4)#prvi element
#linked_list.get_value_from_position(3)
#linked_list.uklanjanje_prvog_elementa()
#linked_list.uklanjanje_zadnjeg_elementa()
linked_list.print_list()
linked_list.duzina_lista() #Duzina liste je 4
print(linked_list.length_recursively(linked_list.head)) #Output je 4


'''
Kreirati jednostruko olancanu listu gde svaki cvor predstavlja studenta
Data dio svakog cvora sadrzi 2 podatka: ime i prosjek studenta. 
Napisati funkciju koja racuna prosecni prosek svih studenata u listi,kao i posebnu funkciju koja vraca listu studenata
koji imaju veci prosek od prosecnog
'''  
class UceniciNode:
    def __init__(self,ime,prosjek):
        self.ucenici = {'ime': ime, 'prosjek' : prosjek}

class LinkedListUcenici:
    def __init__(self,head=None):
        self.head = head
    def append(self,new_element):
        current=self.head
        if not current:
            self.head=new_element
            new_element.next=None
        else:
            while current.next:
                current=current.next
            current.next=new_element
            new_element.next=None
    #funkcija za dodavanje elementa na pocetku liste
    def prepend(self,new_element):
        new_element.next=self.head
        self.head=new_element
    #printanje liste
    def print_list1(self):
        current=self.head
        while current:
            print(current.ucenici)
            current=current.next
    #prosecni prosek svih studenata
    def pronadji_prosjek(self):
        current=self.head
        suma=0
        brojanje=0
        while current:
            suma+=current.ucenici['prosjek']
            brojanje+=1
            current=current.next
        if brojanje==0:
            return None
        else:
            return suma/brojanje
    
    def above_average(self):
        average = self.pronadji_prosjek()
        if average==None:
            print("Nema ucenika")
        else:
            current=self.head
            while current:
                if current.ucenici['prosjek'] > average:
                    print(current.ucenici)
                current=current.next


l2=LinkedListUcenici()

     
