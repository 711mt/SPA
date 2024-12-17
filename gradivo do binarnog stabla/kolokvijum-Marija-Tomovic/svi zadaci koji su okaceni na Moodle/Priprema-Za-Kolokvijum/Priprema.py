class BookNode:
    def __init__(self, title, author, year, pages):
        self.book = {'title': title, 'author': author, 'year': year, 'pages': pages}
        self.next = None

class LinkedListBooks:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if not current:
            self.head = new_element
        else:
            while current.next:
                current = current.next
            current.next = new_element

    def print_books(self):
        current = self.head
        while current:
            print(current.book)
            current = current.next

    def remove_by_title(self, title):
        current = self.head
        prev = None
        while current:
            if current.book['title'] == title:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return
            prev = current
            current = current.next

    def average_pages_after_year(self, year):
        current = self.head
        total_pages = 0
        count = 0
        while current:
            if current.book['year'] > year:
                total_pages += current.book['pages']
                count += 1
            current = current.next
        return total_pages / count if count else None

    def longest_title(self):
        current = self.head
        longest = ""
        while current:
            if len(current.book['title']) > len(longest):
                longest = current.book['title']
            current = current.next
        return longest

    def books_by_author(self, author):
        current = self.head
        while current:
            if current.book['author'] == author:
                print(current.book)
            current = current.next

    def count_books_between_pages(self, min_pages, max_pages):
        current = self.head
        count = 0
        while current:
            if min_pages <= current.book['pages'] <= max_pages:
                count += 1
            current = current.next
        return count

    def books_published_in_year(self, year):
        current = self.head
        while current:
            if current.book['year'] == year:
                print(current.book)
            current = current.next

# Testiranje sa primerima knjiga
n1 = BookNode('1984', 'George Orwell', 1949, 328)
n2 = BookNode('To Kill a Mockingbird', 'Harper Lee', 1960, 281)
n3 = BookNode('The Great Gatsby', 'F. Scott Fitzgerald', 1925, 180)
n4 = BookNode('Brave New World', 'Aldous Huxley', 1932, 311)
n5 = BookNode('Moby Dick', 'Herman Melville', 1851, 635)

books_list = LinkedListBooks()
books_list.append(n1)
books_list.append(n2)
books_list.append(n3)
books_list.append(n4)
books_list.append(n5)

# Ispis svih knjiga
books_list.print_books()
print("**********")

# Računanje prosečnog broja stranica za knjige izdate posle 1930. godine
print(books_list.average_pages_after_year(1930))
print("**********")

# Pronalazak knjige sa najdužim naslovom
print(books_list.longest_title())
print("**********")

# Ispis knjiga autora 'George Orwell'
books_list.books_by_author('George Orwell')
print("**********")

# Brojanje knjiga između 200 i 500 stranica
print(books_list.count_books_between_pages(200, 500))
print("**********")

# Ispis knjiga izdatih 1925. godine
books_list.books_published_in_year(1925)



#2

class Stack:
    def __init__(self):
        # Inicijalizuje prazan stek
        self.items = []

    def push(self, item):
        # Dodaje riječ na vrh steka
        return self.items.append(item)

    def pop(self):
        # Skida i vraća riječ sa vrha steka
        return self.items.pop() if not self.is_empty() else None

    def is_empty(self):
        # Provjerava da li je stek prazan
        return len(self.items) == 0

    def reverse_sentence(self, sentence):
        # Razdvaja rečenicu na riječi i dodaje ih u stek
        words = sentence.split()
        for word in words:
            self.push(word)
        
        # Skida riječi sa steka i prikazuje ih obrnutim redosledom
        reversed_sentence = []
        while not self.is_empty():
            reversed_sentence.append(self.pop())
        
        return ' '.join(reversed_sentence)

# Testiranje
stack = Stack()
sentence = "Ovo je primjer rečenice za testiranje"
print("Originalna rečenica:", sentence)
print("Rečenica unazad:", stack.reverse_sentence(sentence))

#3

class CafeOrderQueue:
    def __init__(self):
        # Inicijalizuje prazan red za narudžbe
        self.orders = []

    def enqueue(self, order_number, drink_name):
        # Dodaje novu narudžbu na kraj reda
        self.orders.append((order_number, drink_name))
        print(f"Narudžba {order_number} za '{drink_name}' dodata u red.")

    def dequeue(self):
        # Obrađuje i uklanja prvu narudžbu iz reda
        if not self.is_empty():
            order = self.orders.pop(0)
            print(f"Obrađena narudžba: {order[0]} za '{order[1]}'")
            return order
        else:
            print("Red je prazan, nema narudžbi za obrađivanje.")
            return None

    def show_orders(self):
        # Prikazuje sve narudžbe u redu
        if not self.is_empty():
            print("Trenutne narudžbe u redu:")
            for order in self.orders:
                print(f"- Narudžba {order[0]} za '{order[1]}'")
        else:
            print("Red je prazan.")

    def is_empty(self):
        # Provjerava da li je red prazan
        return len(self.orders) == 0

# Testiranje
cafe_queue = CafeOrderQueue()

# Dodavanje narudžbi
cafe_queue.enqueue(101, "Espresso")
cafe_queue.enqueue(102, "Cappuccino")
cafe_queue.enqueue(103, "Latte")
cafe_queue.enqueue(104, "Mocha")

# Prikaz trenutnih narudžbi
cafe_queue.show_orders()

# Obrada narudžbi
cafe_queue.dequeue()

# Prikaz narudžbi nakon obrade
cafe_queue.show_orders()

# Još jedna obrada
cafe_queue.dequeue()

# Finalno stanje reda
cafe_queue.show_orders()
