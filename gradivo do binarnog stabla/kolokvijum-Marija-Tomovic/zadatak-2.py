# Zadatak 2 - Dvostruko olancane liste
class Kurs: #cvor Kurs i predstavlja jednu lekciju kursa
    def __init__(self,naslov,predavac,godina,mjesec,trajanje):
        self.value={'naslov':naslov,'predavac':predavac,'godina':godina,"mjesec":mjesec,"trajanje":trajanje}
        self.next=None 
        self.prev=None

class doubleList:
    def __init__(self,head=None,tail=None): #head i tail pokazivaci
        self.head=head
        self.tail=tail
#Pod a) kreiranje funkcija za dodavanje cvorova na pocetak:
    def append(self,element):
        if self.tail:
           current=self.tail
           current.next=element
           element.prev=current
           self.tail=element
        else:
            self.head=element
            self.tail=element
#dodavanje cvorova na kraj liste:
    def prepend(self,element):
        current=self.head
        if self.head:
            element.next=self.head
            self.head=element
        else:
            self.head=element
            self.tale=element

#za stampanje liste cvorova
    def stampanje_lista(self):
        current=self.head
        if self.head:
            while current:
                print(current.value)
                current=current.next
        else:
            print("Lista je prazna")
    
#Pod b) kreiranje funkcije za brisanje cvora na osnovu naziva lekcije
    
    def del_based_naslov(self,name):
        if self.head:
            current=self.head
            while current.value['naslov'].lower()!=name.lower():
                current=current.next
            if current==self.head:
                self.next=None
                self.head=current.next
                self.head.prev=None
            elif current==self.tail:
                self.tail=current.prev
                self.tail.next=None
                current.prev=None
            else:
                sledbenik=current.next
                previous=current.prev
                current.next=None
                current.prev=None
                sledbenik.prev=previous
                previous.next=sledbenik
        else:
            print("Lista je prazna")
    
 #Pod c) izracunavanje koliko lekcija ima trajanje duze od odredjenog broja minuta nakon odredjenog meseca i odredjene godine
    def br_trajanje(self,trajanje,mjesec,godina):
        if self.head:
            current=self.head
            count=0
            while current:
                if current.value['godina']>godina and current.value['mjesec']>mjesec and current.value['trajanje']>trajanje:
                    count=count+1
                current=current.next
            print(count)
        else:
            print("Prazna lista")
    
#Pod d) stampanje naziva kursa sa najduzim trajanjem, i ime predavaca tog kursa
    def max(self):
        current=self.head
        max=current
        while current.next:
            if max.value['trajanje']<current.next.value['trajanje']:
                max=current.next
            current=current.next
        print(max.value['naslov'],max.value['predavac'])
    
#Pod e) stampanje parova(lekcija, predavac) u obrnutom poretku, pocevsi od zadnjeg
    def stampanje_unazad(self):
        current=self.tail
        if self.head:
            while current:
                print(current.value)
                current=current.prev
        else:
            print("Lista je prazna")
    
#Pod f) transformisanje postojece olancane liste
    def print_sorted(self,godina):
        duplikat=self   
        if duplikat.head:   
            current = duplikat.head  
            while(current.next != None):  
                index = current.next;  
                while(index != None):  
                    if(godina <= index.value['godina']):  
                        temp = current.value;  
                        current.value = index.value;  
                        index.value = temp;  
                    index = index.next  
                current = current.next 
            duplikat.stampanje_lista()
        else:
            print("Nema elemenata za sortiranje") 

#Pod g) 5 kurseva
kurs1=Kurs("Linearna algebra","Milica",2012,5,1000)
kurs2=Kurs("Biologija","Neda",2010,6,700)
kurs3=Kurs("Hemija","Pavle",2013,3,800)
kurs4=Kurs("Istorija","Janko",2015,3,900)
kurs5=Kurs("Engleski jezik","Anja",2013,7,600)

double_list=doubleList()
double_list.append(kurs1)
double_list.append(kurs2)
double_list.prepend(kurs3)
double_list.append(kurs4)
double_list.append(kurs5)

#testiranje funkcija
double_list.del_based_naslov("Biologija")
double_list.br_trajanje(500,5,2011)
double_list.max()
double_list.stampanje_unazad()
double_list.print_sorted(2013)
double_list.stampanje_lista()