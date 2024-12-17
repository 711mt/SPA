# (Dvostruko olančane liste) Potrebno je implementirati dvostruko olančanu lista
# i sledeće metode:
# a. Štampa dvostruko olančanu listu od kraja
# Output (za naš primjer): 1 -> 3 -> 45 -> 2
# b. Dodavanje novog čvora na početak dvostruko olančane liste.
# c. Dodavanje novog čvora na kraj dvostruko olančane liste.
# d. Brisanje prvog čvora iz dv. olančane liste.
# e. Brisanje poslednjeg čvora iz dv. olančane liste.
# f. Brisanje poslednja dva elementa iz dv. olančane liste.
# g. Dodavanje elementa na određenoj poziciji.
# h. Brisanje elementa sa zadate pozicije.
# i. Brisanje elementa čija se vrijednost zadata kao argument funkcije
# j. Potrebno je implementirati metod get_middle_node(self) koji vraća
# element sa srednje pozicije iz dvostuko olančane liste
# Primjer:
# Input: 1 -> 2 -> 3 -> 4 -> 5 -> None, output: 3
# Input: 1 -> 3 -> 45 -> 2 -> None, output: 3 (ako imate paran broj
# elemenata srednji element je mid - 1 ili mid + 1, vi uzmite da je to mid -
# 1, koristiti // za dobijanje srednjeg elementa)
# k. Potrebno je implementirati metod remove_duplicates(self) koji uklanja
# duple elemente iz dvostruko olančan liste, a čuva prvo pojavljivanje tog elementa
# Primjer:
# Input: 1 -> 2 -> 2 -> 3 -> 1 -> 10, Output: 1 -> 2 -> 3 -> 10
# l. Napisati funkciju koja mijenja mjesta najmanjem i najvećem elementu
# liste.
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def print_reverse(self):
        """Štampa dvostruko olančanu listu od kraja."""
        if self.head is None:
            return "Lista je prazna."
        current = self.head
        while current.next:
            current = current.next
        reverse_output = []
        while current:
            reverse_output.append(str(current.data))
            current = current.prev
        return " -> ".join(reverse_output)

    def add_at_beginning(self, data):
        """Dodavanje novog čvora na početak dvostruko olančane liste."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_at_end(self, data):
        """Dodavanje novog čvora na kraj dvostruko olančane liste."""
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        new_node.prev = current

    def remove_first(self):
        """Brisanje prvog čvora iz dvostruko olančane liste."""
        if self.head is None:
            return "Lista je prazna."
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def remove_last(self):
        """Brisanje poslednjeg čvora iz dvostruko olančane liste."""
        if self.head is None:
            return "Lista je prazna."
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            current.prev.next = None
        else:
            self.head = None

    def remove_last_two(self):
        """Brisanje poslednja dva elementa iz dvostruko olančane liste."""
        if self.head is None:
            return "Lista je prazna."
        current = self.head
        while current.next:
            current = current.next
        if current.prev:
            if current.prev.prev:
                current.prev.prev.next = None
                current.prev = current.prev.prev
            else:
                self.head = None
        else:
            self.head = None

    def add_at_position(self, data, position):
        """Dodavanje elementa na određenoj poziciji."""
        if position == 0:
            self.add_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                return "Pozicija van opsega."
            current = current.next
        if current is None:
            return "Pozicija van opsega."
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node

    def remove_at_position(self, position):
        """Brisanje elementa sa zadate pozicije."""
        if self.head is None:
            return "Lista je prazna."
        if position == 0:
            self.remove_first()
            return
        current = self.head
        for _ in range(position):
            if current is None:
                return "Pozicija van opsega."
            current = current.next
        if current is None:
            return "Pozicija van opsega."
        if current.next:
            current.next.prev = current.prev
        if current.prev:
            current.prev.next = current.next

    def remove_value(self, value):
        """Brisanje elementa čija se vrijednost zadata kao argument funkcije."""
        if self.head is None:
            return "Lista je prazna."
        current = self.head
        while current:
            if current.data == value:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:  # Ako je prvi element
                    self.head = current.next
                return
            current = current.next

    def get_middle_node(self):
        """Metod koji vraća element sa srednje pozicije iz dvostruko olančane liste."""
        if self.head is None:
            return "Lista je prazna."
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow.data

    def remove_duplicates(self):
        """Uklanja duple elemente iz dvostruko olančane liste."""
        if self.head is None:
            return "Lista je prazna."
        seen = set()
        current = self.head
        while current:
            if current.data in seen:
                self.remove_value(current.data)
            else:
                seen.add(current.data)
            current = current.next

    def swap_min_max(self):
        """Menja mesta najmanjem i najvećem elementu liste."""
        if self.head is None:
            return "Lista je prazna."
        
        min_node = max_node = self.head
        current = self.head
        
        while current:
            if current.data < min_node.data:
                min_node = current
            if current.data > max_node.data:
                max_node = current
            current = current.next
        
        # Zamena podataka između najmanjeg i najvećeg čvora
        min_node.data, max_node.data = max_node.data, min_node.data

# Primer korišćenja
dll = DoublyLinkedList()
dll.add_at_end(1)
dll.add_at_end(2)
dll.add_at_end(2)
dll.add_at_end(3)
dll.add_at_end(1)
dll.add_at_end(10)

print("Lista od kraja:", dll.print_reverse())
print("Srednji element:", dll.get_middle_node())
dll.remove_duplicates()
print("Lista bez duplikata:", dll.print_reverse())
dll.swap_min_max()
print("Lista nakon zamene min i max:", dll.print_reverse())