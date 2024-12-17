#Pod a)
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
    
    def stack_pop(self):
        return self.items.pop()
    

    def peek(self):
        return self.items[0]
    
    def is_empty(self):
        if len(self.items)==0:
            return True
        else:
            return False
    
    def filtriraj_svaki_drugi_kurs(self,N):
        new_red=Red()
        while not self.is_empty():
            if self.peek()[0]<=N:
                self.pop()
                continue
            else:
                new_red.enqueue(self.peek())
                self.pop()
        return new_red.items
    
    def push(self,value):
        self.items.append(value)
    
    def stack_peek(self):
        return self.items[-1]
    
    def convert_to_stack(self):
        stack=Red()
        while not self.is_empty():
            stack.push(self.stack_peek())
            self.stack_pop()
        return stack.items
        



r=Red()
task1=(700,"Matematika")
task2=(500,"Hemija")
task3=(600,"Fizika")
r.enqueue(task1)
r.enqueue(task2)
r.enqueue(task3)
print(r.filtriraj_svaki_drugi_kurs(500))
print(r.items)
print(r.convert_to_stack())