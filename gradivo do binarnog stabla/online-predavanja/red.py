class Queue:
    def __init__(self):
        self.items = []
        self.size = 0
    
    def enqueue(self, item):
        self.size = self.size + 1
        return self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            self.size = self.size - 1
            return self.items.pop(0)
    
    def is_empty(self):
        return self.size == 0

    def first(self):
        if not self.is_empty():
            return self.items[0]
    
    def get_queue(self):
        return self.items

    def __len__(self):
        return self.size

q = Queue()
print(q.is_empty())

q.enqueue("Wake up")
q.enqueue("Have a caffe")
q.enqueue("Have a shower")
q.enqueue("Get dress")
q.enqueue("Go to breakfast")
q.enqueue("Go to faculty")

print(q.get_queue())

print(q.dequeue())

#Kreirati planer zadataka koristeći red (queue) strukturu podataka. Planer zadataka
#mora imati sledeće operacije/metode: Enqueue - dodaje novi zadatak za izvršavanje u planer.
#Svaki task/zadatak ima ime i prioritetni nivo. Taskovi sa većim prioritetom moraju biti izvršeni
#prije onih sa manjim prioritetom. Ako dva taska imaju isti prioritet, izvršavaju se po redu kom
#su dodati u red. Dequeue - vratiti i obrisati task sa najvecim prioritetom. Ako dva taska imaju
#isti nivo prioriteta, obrisati onaj koji je prvi dodat u red. Peek - Vraće task najvišeg prioriteta bez
#uklanjanja iz reda. isEmpty - Provjerava da li je planer zadataka prazan (bez zadataka u redu).
class Queue:
 def __init__(self):
  self.items = []
 def isEmpty(self):
  return len(self.items) == 0
 def get_queue(self):
  return self.items
 def enqueue(self, item):
  self.items.append(item)
  self.items.sort(key=lambda x: x[1], reverse=True)
 def print_queue(self):
  print("Items in queue", "->", *self.items)
  return
 def peek(self):
  return self.items[0]
#pretpostavka da se taskovi dodaju po nivou prioriteta
 def enqueue_pretp(self, item):
  self.items.append(item)
 def dequeue(self):
  return self.items[1:len(self.get_queue())]
 
task1 = ("Brisanje", 15)
task2 = ("Sabiranje", 17)
task3 = ("Pinguj", 7)
queue = Queue()
queue.enqueue(task1)
queue.enqueue(task2)
queue.enqueue(task3)
queue.dequeue()
[('Brisanje', 15), ('Pinguj', 7)]

