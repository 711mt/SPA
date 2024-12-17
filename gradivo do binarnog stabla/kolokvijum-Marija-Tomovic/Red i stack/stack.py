'''
#Stek
Dat je stek S u kojem se čuvaju podaci tipa string. Neki od elemenata steka su bombe (označene
sa “”). Napišite funkciju makni_bombe (S) koja će iz steka S ukloniti sve bombe, a ostale elemente
poređati u ”naopakom” poretku. Na primjer, ako su elementi u S redom od vrha prema dnu steka
(””, D, ”*”, C, B, A), onda nakon poziva funkcije stek treba izgledati ovako: (A, B, C, D)**
'''
class Stack:
  def __init__(self):
    self.items = []
  
  def push(self, value):
    return self.items.append(value)
  
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
  def remove_bombs(self):
     new_stack = Stack()
     while not self.is_empty():
        if self.peek() == "*":
           self.pop()
           continue
        new_stack.push(self.peek())
        self.pop()
     return new_stack.get_stack()
        


s = Stack()
s.push("A")
s.push("B")
s.push("C")
s.push("*")
s.push("D")
s.push("*")

s.remove_bombs()

#primer na casu
s= Stack()
s.push(15)
s.push(72)
s.pop()
s.push(1)
print(s.pop()) #--> stampa 1
print(s.peek()) # --> stampa 15
    