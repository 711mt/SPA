class Stack:
    def __init__(self):
        self.items=[]

    def push(self,value):
        self.items.append(value)
    
    def pop(self):
       return self.items.pop()
    
    def peek(self):
        return self.items[-1]
    
    def get_stack(self):
        return self.items
    
    def is_empty(self):
        if len(self.get_stack())==0:
            return True
        else:
            return False
    
    def obrnuto(self):
        recenica=""
        while not self.is_empty():
            recenica=recenica+" "+self.peek()
            self.pop()
        return recenica
        
    
'''stack=Stack()
s=input("Unesite recenicu: ")
s=s.split()
for i in s:
    stack.push(i)
print(stack.obrnuto())'''

class Knjiga:
    def __init__(self,naslov,autor,godina,brstrana):
        self.value={'naslov':naslov,'autor':autor,"godina":godina,"strane":brstrana}
        self.next=None

class linkedList:
    def __init__(self,head=None):
        self.head=head

    def append(self,new_elemenat):
        current=self.head
        if self.head:
            while current.next:
                current=current.next
            current.next=new_elemenat
        else:
            self.head=new_elemenat

    def stampaj(self):
        current=self.head
        if self.head: 
            while current.next: 
                print(current.value)
                current=current.next
            print(current.value)
        else:
            print("Nema elemenata")
    
    
    def del_naslov(self,naslov):
        current=self.head
        if self.head.value['naslov']==naslov:
            self.head=current.next
            current.next=None
        else:
            while current.next.value['naslov']!=naslov:
                current=current.next
            current.next.next=None
            current.next=current.next.next
            
'''
knjiga1=Knjiga("naslov1","autor1",1990,300)
knjiga2=Knjiga("naslov2","autor2",1999,400)
knjiga3=Knjiga("naslov3","autor3",2000,500)
linked_list=linkedList()
linked_list.append(knjiga1)
linked_list.append(knjiga2)
linked_list.append(knjiga3)
linked_list.del_naslov("naslov3")
linked_list.stampaj()
'''   
class Red:
    def __init__(self):
        self.items=[]
    
    def enqueue(self,value):
        self.items.append(value)
        print("Ova narduzbina ",value," je dodata")
        
    def dequeue(self):
        print("Ovaj task je izvrsen: ",self.items[0])
        self.pop()
        return self.items
    
    def pop(self):
       return self.items.pop(0)
    

    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False
'''
r=Red()
task1=(1,"Pivo")
task2=(2,"Rakija")
task3=(3,"Somersbi")
r.enqueue(task1)
r.enqueue(task2)
r.enqueue(task3)
r.dequeue()
print(r.dequeue())
'''
class Restoran:
    def __init__(self,klijent,jelo,vreme,prioritet):
        self.value={'klijent':klijent,'jelo':jelo,"vreme":vreme,'prioritet':prioritet}
        self.next=None
        self.prev=None

class doubleList:
    def __init__(self,head=None,tail=None):
        self.head=head
        self.tail=tail
    
    def append(self,element):
        if self.tail:
           current=self.tail
           current.next=element
           element.prev=current
           self.tail=element
        else:
            self.head=element
            self.tail=element
        
    def prepend(self,element):
        current=self.head
        if self.head:
            element.next=self.head
            self.head=element
        else:
            self.head=element
            self.tale=element

    def stampaj(self):
        current=self.head
        if self.head:
            while current:
                print(current.value)
                current=current.next
        else:
            print("Prazna lista")
    
    def del_klijent(self,klijent):
        if self.head:
            current=self.head
            while current.value['klijent'].lower()!=klijent.lower():
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
    
    def print_sorted(self):   
        if self.head:   
            current = self.head  
            while(current.next != None):  
                index = current.next;  
                while(index != None):  
                    if(current.value['prioritet'] >= index.value['prioritet']):  
                        temp = current.value;  
                        current.value = index.value;  
                        index.value = temp;  
                    index = index.next  
                current = current.next 
            self.stampaj()
        else:
            print("Nema elemenata za sortiranje") 

    
    def br_nakon_vremena(self,vreme):
        if self.head:
            current=self.head
            i=0
            while current:
                if current.value['vreme']>vreme:
                   i=i+1
                current=current.next
            return i
        else:
            print("Lista je prazna")
    
    def brisi_poslednju(self):
        if self.head:
            if self.tail==self.head:
                self.tail=None
                self.head=None
            else:
                current=self.tail
                previous=current.prev
                previous.next=None
                current.prev=None
                self.tail=previous
        else:
            print("Lista je prazna")

naruceno1=Restoran("Balsa","Cevapi",500,1)
naruceno2=Restoran("Branko","Burger",600,2)
naruceno3=Restoran("Jovan","Burek",400,1)
naruceno4=Restoran("Boban","Pizza",450,2)
double_list=doubleList()
double_list.append(naruceno1)
double_list.append(naruceno2)
double_list.append(naruceno3)
double_list.append(naruceno4)
#double_list.print_sorted()
#print(double_list.br_nakon_vremena(450))
#double_list.del_klijent("Boban")
double_list.brisi_poslednju()
double_list.stampaj()
    
    
