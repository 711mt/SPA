# (Jednostruko olančane liste) U nastavku su dati zadaci za razne vrste
# olančanih listi:
# a. Brojeve sa ulaza stavljati u jednostruko olančanu listu sve dok se ne
# unese nula, a zatim dobijenu listu ispisati na izlaz.
# i. Zadatak realizovati dodavanjem elemenata liste na početak
# liste.
# ii. Zadatak realizovati tako da listu koja se formira bude sortirana.
# iii. Zadatak realizovati dodavanjem elemenata liste na kraj liste a
# listu ispisati unazad.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def add_sorted(self, data):
        new_node = Node(data)
        if self.head is None or self.head.data >= data:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next is not None and current.next.data < data:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def add_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" ")
            current = current.next
        print()

    def print_list_reverse(self, node):
        if node is None:
            return
        self.print_list_reverse(node.next)
        print(node.data, end=" ")
# a.i) Dodavanje elemenata na početak liste
def task_ai():
    linked_list = LinkedList()
    while True:
        num = int(input("Unesite broj (0 za kraj): "))
        if num == 0:
            break
        linked_list.add_to_start(num)
    print("Lista:")
    linked_list.print_list()
# a.ii) Formiranje sortirane liste
def task_aii():
    linked_list = LinkedList()
    while True:
        num = int(input("Unesite broj (0 za kraj): "))
        if num == 0:
            break
        linked_list.add_sorted(num)
    print("Sortirana lista:")
    linked_list.print_list()
# a.iii) Dodavanje na kraj liste i ispis unazad
def task_aiii():
    linked_list = LinkedList()
    while True:
        num = int(input("Unesite broj (0 za kraj): "))
        if num == 0:
            break
        linked_list.add_to_end(num)
    print("Lista unazad:")
    linked_list.print_list_reverse(linked_list.head)
    print()
# c. Napisati funkciju koja na osnovu ulazne liste l1, kreira i štampa novu
# listu l2, a koja se sastoji od neparnih elemenata iz liste l1 koje je
# potrebno kvadrirati
# Input: 5 -> 4 -> 3 -> 8 ->2 Output: 25 -> 9

# b. Kreirati jednostruko olančanu listu sa bar 5 elemenata. Svaki element
# je prirodan broj. Moguće je ponavljanje elemenata.
def create_odd_squared_list(self):
        l2 = LinkedList()
        current = self.head
        while current:
            if current.data % 2 != 0:  # Provera da li je broj neparan
                l2.add_to_end(current.data ** 2)  # Kvadriranje neparnih brojeva
            current = current.next
        return l2

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [5, 4, 3, 8, 2]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Kreiranje i ispis nove liste l2
l2 = l1.create_odd_squared_list()
print("Lista l2 (kvadrirani neparni elementi):")
l2.print_list()
# Kreiramo listu sa bar 5 elemenata
linked_list = LinkedList()
elements = [3, 5, 8, 5, 12]  # primer liste sa ponavljanjem elemenata

# Dodavanje elemenata u listu
for element in elements:
    linked_list.add_to_end(element)

# Ispis liste
print("Jednostruko ulančana lista:")
linked_list.print_list()

# d. Napisati funkciju koja iz liste l1 uklanja svaki treći element, počevši od
# prvog elementa
# Input: 5 -> 4 -> 3 -> 8 -> 2 Output: 5 -> 8
def remove_every_third(self):
        current = self.head
        prev = None
        index = 1  # Brojimo pozicije čvorova počevši od 1
        while current:
            if index % 3 == 0:  # Uklanjamo svaki treći element
                prev.next = current.next
            else:
                prev = current
            current = current.next
            index += 1

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [5, 4, 3, 8, 2]
for element in elements:
    l1.add_to_end(element)
print("Ulazna lista l1:")
l1.print_list()

# Uklanjanje svakog trećeg elementa i ispis nove liste
l1.remove_every_third()
print("Lista nakon uklanjanja svakog trećeg elementa:")
l1.print_list()

# e. Napisati funkciju koja na osnovu ulazne liste l1, kreira i štampa novu
# listu l2, a koja se sastoji od negativnih elemenata iz liste l1 koje je
# potrebno kvadrirati
# Input: -5 -> 4 -> -3 -> 8 -> -2 Output: 25 -> 9 -> 4
def create_negative_squared_list(self):
        l2 = LinkedList()
        current = self.head
        while current:
            if current.data < 0:  # Provera da li je broj negativan
                l2.add_to_end(current.data ** 2)  # Kvadriranje negativnih brojeva
            current = current.next
        return l2

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [-5, 4, -3, 8, -2]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Kreiranje i ispis nove liste l2
l2 = l1.create_negative_squared_list()
print("Lista l2 (kvadrirani negativni elementi):")
l2.print_list()

# f. Napisati funkciju koja iz liste l1 izvlači brojeve čijim korijenovanjem
# dobijamo prirodan broj, počevši od prvog elementa
# Input: -9 -> 4 -> -3 -> 8 -> -2 -> 16 Output: 4 -> 16
import math

def create_square_root_list(self):
        l2 = LinkedList()
        current = self.head
        while current:
            if current.data > 0:  # Uzimamo samo pozitivne brojeve
                root = math.isqrt(current.data)  # Celi deo korena
                if root * root == current.data:  # Proveravamo da li je savršen kvadrat
                    l2.add_to_end(current.data)
            current = current.next
        return l2

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [-9, 4, -3, 8, -2, 16]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Kreiranje i ispis nove liste l2
l2 = l1.create_square_root_list()
print("Lista l2 (brojevi čijim korenovanjem dobijamo prirodan broj):")
l2.print_list()

# g. Napisati funkciju koja na osnovu ulazne liste l1, kreira i štampa novu
# listu l2, a koja se sastoji od parnih elemenata iz liste l1 koje je potrebno
# kvadrirati
# Input: 5 -> 4 -> 3 -> 8 ->2 Output: 16 -> 64 -> 4
def create_even_squared_list(self):
        l2 = LinkedList()
        current = self.head
        while current:
            if current.data % 2 == 0:  # Provera da li je broj paran
                l2.add_to_end(current.data ** 2)  # Kvadriranje parnih brojeva
            current = current.next
        return l2

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [5, 4, 3, 8, 2]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Kreiranje i ispis nove liste l2
l2 = l1.create_even_squared_list()
print("Lista l2 (kvadrirani parni elementi):")
l2.print_list()

# h. Napisati funkciju koja iz liste l1 uklanja svaki drugi element, počevši od
# prvog elementa
# Input: 5 -> 4 -> 3 -> 8 -> 2 Output: 5 -> 3 -> 2
def remove_every_second(self):
        current = self.head
        prev = None
        index = 1  # Brojimo pozicije čvorova počevši od 1
        while current:
            if index % 2 == 0:  # Uklanjamo svaki drugi element
                prev.next = current.next
            else:
                prev = current
            current = current.next
            index += 1

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [5, 4, 3, 8, 2]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Uklanjanje svakog drugog elementa i ispis nove liste
l1.remove_every_second()
print("Lista nakon uklanjanja svakog drugog elementa:")
l1.print_list()

# i. Napisati funkciju koja uklanja najmanji element iz liste
# Input: 5 -> 4 -> 3 -> 7 -> 5 -> 1 Output: 5 -> 4 -> 3 ->7 -> 5
def remove_minimum(self):
        if self.head is None:
            return  # Ako je lista prazna, nema šta da se uklanja

        # Pronađi najmanji element
        min_value = self.head.data
        current = self.head
        while current:
            if current.data < min_value:
                min_value = current.data
            current = current.next

        # Ukloni prvi čvor koji ima vrednost jednaku min_value
        current = self.head
        prev = None
        while current:
            if current.data == min_value:
                if prev is None:  # Ako je to prvi element u listi
                    self.head = current.next
                else:
                    prev.next = current.next
                break
            prev = current
            current = current.next

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [5, 4, 3, 7, 5, 1]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Uklanjanje najmanjeg elementa i ispis nove liste
l1.remove_minimum()
print("Lista nakon uklanjanja najmanjeg elementa:")
l1.print_list()

# j. Napisati funkciju koja nalazi drugi najmanji element liste i vraća taj
# element
# Input: 5 -> 4 -> 3 -> 7 -> 5 -> 1 Output: 3
def find_second_minimum(self):
        if self.head is None or self.head.next is None:
            return None  # Ako lista ima manje od 2 elementa, nema drugog najmanjeg

        # Inicijalizujemo prvi i drugi najmanji na maksimum
        min_value = float('inf')
        second_min = float('inf')
        current = self.head

        while current:
            if current.data < min_value:
                # Ako nađemo novi minimum, ažuriramo drugi najmanji
                second_min = min_value
                min_value = current.data
            elif min_value < current.data < second_min:
                # Ako je trenutni element između min_value i second_min
                second_min = current.data
            current = current.next

        return second_min if second_min != float('inf') else None

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [5, 4, 3, 7, 5, 1]
for element in elements:
    l1.add_to_end(element)

# Pronalaženje drugog najmanjeg elementa
second_min = l1.find_second_minimum()
print("Drugi najmanji element u listi:", second_min)

# k. Napisati funkciju koja prebrojava koliko elemenata je veće od drugog
# najmanjeg elementa liste (preporuka da iskoristite prethodne funkcije)
# Input: 5 -> 4 -> 3 -> 7 -> 5 -> 1 Output: 4 (veci su 5, 4, 7 i 5)
def find_second_minimum(self):
        if self.head is None or self.head.next is None:
            return None  # Ako lista ima manje od 2 elementa, nema drugog najmanjeg

        min_value = float('inf')
        second_min = float('inf')
        current = self.head

        while current:
            if current.data < min_value:
                second_min = min_value
                min_value = current.data
            elif min_value < current.data < second_min:
                second_min = current.data
            current = current.next

        return second_min if second_min != float('inf') else None

def count_greater_than_second_min(self):
        second_min = self.find_second_minimum()
        if second_min is None:
            return 0  # Ako nema drugog najmanjeg, vraćamo 0

        count = 0
        current = self.head
        while current:
            if current.data > second_min:
                count += 1
            current = current.next

        return count

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [5, 4, 3, 7, 5, 1]
for element in elements:
    l1.add_to_end(element)

# Prebrojavanje elemenata većih od drugog najmanjeg
count = l1.count_greater_than_second_min()
print("Broj elemenata većih od drugog najmanjeg elementa:", count)
# #l. Napisati funkciju koja uklanja najveći element iz liste (podsjetnik da
# imate implementiranu funkciju koja briše element na osnovu zadate
# vrijednosti – nedelja 2)
# Input: 5 -> 4 -> 3 -> 7 -> 5 -> 1 Output: 5 -> 4 -> 3 -> 5 -> 1
def remove_by_value(self, value):
        current = self.head
        prev = None
        
        while current:
            if current.data == value:
                if prev is None:  # Ako je to prvi element u listi
                    self.head = current.next
                else:
                    prev.next = current.next
                return  # Prekinimo nakon uklanjanja prvog nalaska
            prev = current
            current = current.next

def remove_maximum(self):
        if self.head is None:
            return  # Ako je lista prazna, nema šta da se uklanja

        # Pronađi najveći element
        max_value = self.head.data
        current = self.head
        while current:
            if current.data > max_value:
                max_value = current.data
            current = current.next

        # Ukloni prvi čvor koji ima vrednost jednaku max_value
        self.remove_by_value(max_value)

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [5, 4, 3, 7, 5, 1]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Uklanjanje najvećeg elementa i ispis nove liste
l1.remove_maximum()
print("Lista nakon uklanjanja najvećeg elementa:")
l1.print_list()

# m. Napisati funkciju koja nalazi drugi najveći element liste i vraća taj
# element koja uklanja najveći element, što znači da je nakon brisanja
# tog elementa najveći element koji ostane drugi najveći)
# Input: 5 -> 4 -> 3 -> 7 -> 5 -> 1 Output: 5
# def remove_by_value(self, value):
#         current = self.head
#         prev = None
        
#         while current:
#             if current.data == value:
#                 if prev is None:  # Ako je to prvi element u listi
#                     self.head = current.next
#                 else:
#                     prev.next = current.next
#                 return  # Prekinimo nakon uklanjanja prvog nalaska
#             prev = current
#             current = current.next

#     def find_maximum(self):
#         if self.head is None:
#             return None  # Ako je lista prazna

#         max_value = self.head.data
#         current = self.head
#         while current:
#             if current.data > max_value:
#                 max_value = current.data
#             current = current.next

#         return max_value

#     def find_second_maximum_after_removing_max(self):
#         max_value = self.find_maximum()
#         if max_value is None:
#             return None  # Ako lista nema elemenata

#         self.remove_by_value(max_value)  # Ukloni najveći element
        
#         # Sada pronalazimo drugi najveći element
#         second_max = float('-inf')
#         current = self.head

#         while current:
#             if current.data > second_max:
#                 second_max = current.data
#             current = current.next

#         return second_max if second_max != float('-inf') else None

# # Kreiranje ulazne liste l1
# l1 = LinkedList()
# elements = [5, 4, 3, 7, 5, 1]
# for element in elements:
#     l1.add_to_end(element)

# print("Ulazna lista l1:")
# l1.print_list()

# # Pronalaženje drugog najvećeg elementa nakon uklanjanja najvećeg
# second_max = l1.find_second_maximum_after_removing_max()
# print("Drugi najveći element nakon uklanjanja najvećeg:", second_max)
# # n. Napisati funkciju koja prebrojava koliko elemenata je manje od drugog
# # najvećeg elementa liste (preporuka da iskoristite prethodne funkcije)
# # Input: 5 -> 4 -> 3 -> 7 -> 5 -> 1 Output: 3 (manji su 4, 3 i 1)
#  def remove_by_value(self, value):
#         current = self.head
#         prev = None
        
#         while current:
#             if current.data == value:
#                 if prev is None:  # Ako je to prvi element u listi
#                     self.head = current.next
#                 else:
#                     prev.next = current.next
#                 return  # Prekinimo nakon uklanjanja prvog nalaska
#             prev = current
#             current = current.next

#     def find_maximum(self):
#         if self.head is None:
#             return None  # Ako je lista prazna

#         max_value = self.head.data
#         current = self.head
#         while current:
#             if current.data > max_value:
#                 max_value = current.data
#             current = current.next

#         return max_value

#     def find_second_maximum_after_removing_max(self):
#         max_value = self.find_maximum()
#         if max_value is None:
#             return None  # Ako lista nema elemenata

#         self.remove_by_value(max_value)  # Ukloni najveći element
        
#         # Sada pronalazimo drugi najveći element
#         second_max = float('-inf')
#         current = self.head

#         while current:
#             if current.data > second_max:
#                 second_max = current.data
#             current = current.next

#         return second_max if second_max != float('-inf') else None

#     def count_less_than_second_maximum(self):
#         second_max = self.find_second_maximum_after_removing_max()
#         if second_max is None:
#             return 0  # Ako nema drugog najvećeg, vraćamo 0

#         count = 0
#         current = self.head
#         while current:
#             if current.data < second_max:
#                 count += 1
#             current = current.next

#         return count

# # Kreiranje ulazne liste l1
# l1 = LinkedList()
# elements = [5, 4, 3, 7, 5, 1]
# for element in elements:
#     l1.add_to_end(element)

# print("Ulazna lista l1:")
# l1.print_list()

# # Prebrojavanje elemenata koji su manji od drugog najvećeg elementa
# count = l1.count_less_than_second_maximum()
# print("Broj elemenata manjih od drugog najvećeg elementa:", count)

# o. Napisati funkciju koja na osnovu ulazne liste l1, kreira i štampa novu
# listu l2, a koja se sastoji od negativnih elemenata iz liste l1 koje je
# potrebno kvadrirati
# Input: -5 -> 4 -> -3 -> 8 -> -2 Output: 25 -> 9 -> 4
def create_squared_negative_list(self):
        new_list = LinkedList()
        current = self.head
        
        while current:
            if current.data < 0:  # Proveravamo da li je element negativan
                new_list.add_to_end(current.data ** 2)  # Kvadriramo i dodajemo u novu listu
            current = current.next
        
        return new_list

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [-5, 4, -3, 8, -2]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Kreiranje i ispis nove liste l2
l2 = l1.create_squared_negative_list()
print("Nova lista l2 (kvadrirani negativni elementi):")
l2.print_list()
# p. Napisati funkciju koja iz liste l1 izvlači neparne elemente, počevši od
# prvog elementa
# Input: -5 -> 4 -> -3 -> 8 -> -2 Output: 4 -> 8 -> -2
def extract_even_elements(self):
        new_list = LinkedList()
        current = self.head
        
        while current:
            if current.data % 2 == 0:  # Proveravamo da li je element paran
                new_list.add_to_end(current.data)  # Dodajemo u novu listu
            current = current.next
        
        return new_list

# Kreiranje ulazne liste l1
l1 = LinkedList()
elements = [-5, 4, -3, 8, -2]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Kreiranje i ispis nove liste l2 sa parnim elementima
l2 = l1.extract_even_elements()
print("Nova lista l2 (parni elementi):")
l2.print_list()

# q. Kreirati metod concat_lists(self, list2) koja mijenja postojeću listu tako
# što spaja trenutnu listu (self) sa listom list2
# Input: 1 -> 2 -> 5 i 4 -> 7 Output: 1 -> 2 -> 5 -> 4 -> 7
def concat_lists(self, list2):
        if self.head is None:  # Ako je trenutna lista prazna
            self.head = list2.head
            return
        if list2.head is None:  # Ako je lista2 prazna, nema šta dodati
            return

        current = self.head
        while current.next:  # Prolazimo do kraja trenutne liste
            current = current.next

        current.next = list2.head  # Spojimo dve liste

# Kreiranje prvih i drugih lista
l1 = LinkedList()
elements1 = [1, 2, 5]
for element in elements1:
    l1.add_to_end(element)

l2 = LinkedList()
elements2 = [4, 7]
for element in elements2:
    l2.add_to_end(element)

print("Prva lista l1:")
l1.print_list()

print("Druga lista l2:")
l2.print_list()

# Spajanje listi
l1.concat_lists(l2)
print("Spajena lista:")
l1.print_list()

# r. Data je jednostruko olančana lista. Transformisati postojeću ili kreirati
# novu jednostruko olančanu listu tako da prvi dio liste čine negativni
# brojevi, a ostatak pozitivni brojevi. Elemente čija je vrijednost 0 smjestiti
# na kraj liste. Potrebno je očuvati raspored iz originalne liste.
# Input: 2, 3, -2, 13, -5, 0, 1 Output: -2, -5, 2, 3, 13, 1, 0
def transform_list(self):
        negative_list = LinkedList()
        positive_list = LinkedList()
        zero_count = 0
        
        current = self.head
        
        # Prolazimo kroz originalnu listu
        while current:
            if current.data < 0:
                negative_list.add_to_end(current.data)
            elif current.data > 0:
                positive_list.add_to_end(current.data)
            else:
                zero_count += 1  # Brojimo nule
            current = current.next
        
        # Spajamo negativne, pozitivne i nule
        new_list = LinkedList()
        
        # Dodajemo negativne brojeve
        current = negative_list.head
        while current:
            new_list.add_to_end(current.data)
            current = current.next
        
        # Dodajemo pozitivne brojeve
        current = positive_list.head
        while current:
            new_list.add_to_end(current.data)
            current = current.next
        
        # Dodajemo nule na kraj
        for _ in range(zero_count):
            new_list.add_to_end(0)
        
        return new_list

# Kreiranje ulazne liste
l1 = LinkedList()
elements = [2, 3, -2, 13, -5, 0, 1]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Transformacija liste
transformed_list = l1.transform_list()
print("Transformisana lista:")
transformed_list.print_list()

# s. Napisati funkciju insert_between(node) koja izmedju dva elementa u
# listi umece element koji predstavlja razliku ta dva susjedna elementa.
# Npr. za listu 3, 4, 6, 7, 0 generise se lista 3 -1 4 -2 6 -1 7.
def insert_between(self):
        if self.head is None or self.head.next is None:
            return  # Nema dovoljno elemenata za umetanje razlika

        current = self.head
        while current and current.next:
            difference = current.next.data - current.data  # Izračunavamo razliku
            new_node = Node(difference)  # Kreiramo novi čvor sa razlikom
            new_node.next = current.next  # Povezujemo novi čvor sa sledećim
            current.next = new_node  # Povezujemo trenutni čvor sa novim čvorom
            current = new_node.next  # Pomera se na sledeći čvor (originalni)

# Kreiranje ulazne liste
l1 = LinkedList()
elements = [3, 4, 6, 7, 0]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Umetanje razlika
l1.insert_between()
print("Lista nakon umetanja razlika između elemenata:")
l1.print_list()

# t. Napisati funkciju custom_count(value) koja za zadatu jednostruko
# olančanu listu prebrojava koliko elemenata je veće od zadate
# vrijednosti. Elementi liste su cijeli brojevi. Zadatak testirati na listi koja
# ima bar 5 elemenata.
def custom_count(self, value):
        count = 0
        current = self.head
        
        while current:
            if current.data > value:
                count += 1
            current = current.next
        
        return count

# Kreiranje ulazne liste
l1 = LinkedList()
elements = [3, 4, 6, 7, 0]
for element in elements:
    l1.add_to_end(element)

print("Ulazna lista l1:")
l1.print_list()

# Testiranje funkcije custom_count
value_to_compare = 4
count_greater = l1.custom_count(value_to_compare)
print(f"Broj elemenata većih od {value_to_compare}: {count_greater}")

# v. Napisati funkciju intersection(l1, l2) koja za dvije unijete liste vraca
# trecu listu koja se dobija kao presjek te dvije unesene liste.
def to_set(self):
        """Pretvara listu u skup za lakše pretraživanje."""
        result_set = set()
        current = self.head
        while current:
            result_set.add(current.data)
            current = current.next
        return result_set

def intersection(l1, l2):
    # Kreiramo novu listu za presjek
    intersected_list = LinkedList()

    # Konvertujemo l1 u set za brže pretraživanje
    set_l1 = l1.to_set()
    
    # Prolazimo kroz l2 i dodajemo elemente u intersected_list ako postoje u set_l1
    current = l2.head
    while current:
        if current.data in set_l1:
            intersected_list.add_to_end(current.data)
        current = current.next
    
    return intersected_list

# Kreiranje i testiranje
l1 = LinkedList()
l2 = LinkedList()

# Dodajemo elemente prvoj listi
elements1 = [1, 2, 3, 4, 5]
for element in elements1:
    l1.add_to_end(element)

# Dodajemo elemente drugoj listi
elements2 = [3, 4, 5, 6, 7]
for element in elements2:
    l2.add_to_end(element)

print("Lista 1:")
l1.print_list()
print("Lista 2:")
l2.print_list()

# Ispitivanje presjeka lista
intersected_list = intersection(l1, l2)
print("Presjek lista:")
intersected_list.print_list()