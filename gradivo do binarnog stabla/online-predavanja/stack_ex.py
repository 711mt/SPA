class Stack:
  def __init__(self):
    self.items=[]
  def push(self,item):
    return self.items.append(item)
  def pop(self):
    if not self.is_empty():
      return self.items.pop()
  def is_empty(self):
    return len(self.items)==0
  def peek(self):
    if not self.is_empty():
      return self.items[-1]
  def get_stack(self):
    return self.items
    
  
s=Stack()
print(s.is_empty())
s.push(1)
s.push(2)
print(s.peek()) #--> output 2
print(s.get_stack())
s.pop()
print(s.get_stack())

####################################
from stack_ex import Stack

def to_binary(num):
    s = Stack()
    while num > 0:
        reminder = num % 2
        s.push(reminder)
        num = num // 2
    
    bin_num = ""
    while not s.is_empty():
        bin_num = bin_num + str(s.pop())
    return bin_num
print(to_binary(7))


######################################
def reverse(izvorni):
    count = 0
    pomocni = Stack()
    while count != izvorni.length() - 1: 
      
        topVal = izvorni.pop() 
        while count != izvorni.length(): 
            pomocni.push(izvorni.pop()) 
            
        izvorni.push(topVal) 
        while pomocni.length() != 0: 
            izvorni.push(pomocni.pop()) 
          
        count += 1
    return izvorni