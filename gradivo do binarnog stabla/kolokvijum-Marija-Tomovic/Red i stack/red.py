'''
Kreirati planer zadataka koristeći red (queue) strukturu podataka. Planer zadataka
mora imati sledeće operacije/metode: Enqueue - dodaje novi zadatak za izvršavanje u planer.
Svaki task/zadatak ima ime i prioritetni nivo. Taskovi sa većim prioritetom moraju biti izvršeni
prije onih sa manjim prioritetom. Ako dva taska imaju isti prioritet, izvršavaju se po redu kom
su dodati u red. Dequeue - vratiti i obrisati task sa najvecim prioritetom. Ako dva taska imaju
isti nivo prioriteta, obrisati onaj koji je prvi dodat u red. Peek - Vraće task najvišeg prioriteta bez
uklanjanja iz reda. isEmpty - Provjerava da li je planer zadataka prazan (bez zadataka u redu).
'''

class Queue:
  def __init__(self):
    self.items=[]

  def get_queue(self):
    return self.items

  def enqueue(self,value):
    return self.items.append(value)
  
  def dequeue(self):
    print(self.get_queue()[0])
    return self.get_queue()[1::]
  
  def peek(self):
    return self.get_queue()[0]
  
  def is_empty(self):
    if len(self.get_queue()) == 0:
      return True
    else:
      return False

task1 = ("Brisanje", 15)
task2 =("Mnozenje brojeva", 25)
task3 = ("Oduzimanje brojeva", 17)

red = Queue()
red.enqueue(task2)
red.enqueue(task3)
red.enqueue(task1)