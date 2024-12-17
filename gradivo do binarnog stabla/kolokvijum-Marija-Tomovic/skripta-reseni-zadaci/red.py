# f. Dat je red R u kome se čuvaju podaci tipa broj. Napisati funkciju
# brisi_svaki_drugi (R) koja iz reda uklanja svaki drugi element. Npr.
# ako je dat red 1, 5, 7, 8, 9, output treba da bude 1, 7, 9. Za dodavanje
# elemenata u red koristiti funkciju enqueue, a za brisanje dequeue koje
# su implementirane na vjezbama.

class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

def brisi_svaki_drugi(R):
    # Nova instanca reda za čuvanje rezultata
    rezultat = Queue()
    
    # Prolazimo kroz red R i dodajemo svaki prvi element u rezultat
    for i in range(R.size()):
        element = R.dequeue()
        if i % 2 == 0:  # Svaki drugi element, počinjući od 0
            rezultat.enqueue(element)
    
    # Vraćamo rezultat
    return rezultat

# Testiranje funkcionalnosti
if __name__ == "__main__":
    R = Queue()
    # Dodavanje elemenata u red
    for broj in [1, 5, 7, 8, 9]:
        R.enqueue(broj)

    # Brisanje svakog drugog elementa
    novi_red = brisi_svaki_drugi(R)

    # Ispis rezultata
    while not novi_red.is_empty():
        print(novi_red.dequeue(), end=', ')