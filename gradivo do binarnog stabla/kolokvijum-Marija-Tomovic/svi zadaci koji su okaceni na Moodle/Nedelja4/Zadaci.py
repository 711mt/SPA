
#1
"""class Node:
    def __init__(self, value):
        self.value = value  # Svaki čvor (Node) ima vrednost
        self.next = None  # Svaki čvor pokazuje na sledeći čvor u listi (u početku nema sledećeg čvora)

class LinkedList:
    def __init__(self, head=None):
        self.head = head  # Glava liste (početni čvor), inicijalno može biti prazna

    def prepend(self, new_element):
        # Dodaje novi element na početak liste
        new_element.next = self.head  # Nova glava pokazuje na trenutnu glavu
        self.head = new_element  # Nova glava postaje novi čvor

    def append(self, new_element):
        # Dodaje novi element na kraj liste
        current = self.head
        if self.head:
            # Ako postoji čvor, prolazimo kroz listu dok ne dođemo do kraja
            while current.next:
                current = current.next
            current.next = new_element  # Postavljamo novi element kao sledeći u poslednjem čvoru
        else:
            # Ako nema čvorova (lista je prazna), novi element postaje glava
            self.head = new_element

    def brisi_prvi(self):
        # Briše prvi (glavni) čvor u listi
        if not self.head:
            return None  # Ako nema elemenata u listi, ne radi ništa
        self.head = self.head.next  # Glava postaje sledeći čvor u listi

    def brisi_vrijednost(self, value):
        # Briše prvi čvor u listi koji ima zadatu vrednost
        current = self.head
        prev = None
        # Prolazimo kroz listu dok ne nađemo element sa zadatom vrednošću
        while current.value != value and current.next:
            prev = current
            current = current.next
        
        if current.value == value:
            # Ako je pronađen element sa zadatom vrednošću
            if prev:
                prev.next = current.next  # Preskačemo trenutni čvor (brišemo ga)
            else:
                self.head = current.next  # Ako je to glava, pomeramo glavu na sledeći čvor

    def duzina(self):
        # Računa dužinu liste (broj čvorova)
        count = 0
        current = self.head
        while current:
            current = current.next  # Pomeramo se na sledeći čvor
            count = count + 1  # Uvećavamo brojač za svaki čvor
        return count

    def print_list(self):
        # Ispisuje vrednosti svih čvorova u listi
        current = self.head
        while current:
            print(current.value)  # Štampa vrednost trenutnog čvora
            current = current.next  # Pomeramo se na sledeći čvor

    def kvadriraj(self):
        # Štampa kvadrate vrednosti svih čvorova u listi
        current = self.head
        while current:
            print(current.value * current.value)  # Štampa kvadrat vrednosti trenutnog čvora
            current = current.next  # Pomeramo se na sledeći čvor

    def maksimum(self):
        # Vraća maksimalnu vrednost u listi
        current = self.head
        max_elem = current.value  # Postavljamo prvu vrednost kao maksimalnu
        while current:
            if current.value > max_elem:
                max_elem = current.value  # Ako nađemo veću vrednost, ažuriramo maksimalnu vrednost
            current = current.next  # Pomeramo se na sledeći čvor
        return max_elem

    def brisi_drugi(self):
        # Briše svaki drugi čvor u listi
        current = self.head
        current2 = current.next
        while current.next:
            current_2 = current.next  # Čuvamo drugi čvor u nizu
            current.next = current_2.next  # Preskačemo drugi čvor
            current = current.next  # Pomeramo se na sledeći čvor

# Kreiramo čvorove (Node)
n1 = Node(5)
n2 = Node(7)
n3 = Node(3)
n4 = Node(2)
n5 = Node(1)
n6 = Node(11)
n7 = Node(17)
n8 = Node(13)
n9 = Node(22)
n10= Node(14)

# A) Kreiramo listu i dodajemo elemente na kraj
l1 = LinkedList()
l1.append(n4)
l1.append(n3)
l1.append(n2)
l1.append(n1)
l1.append(n5)
l1.print_list()  # Ispisuje listu
print("**********************")

# B) Kreiramo novu listu i dodajemo elemente na početak
l2= LinkedList()
l2.prepend(n6)
l2.prepend(n7)
l2.prepend(n8)
l2.prepend(n9)
l2.prepend(n10)
l2.print_list()  # Ispisuje listu
print("**********************")

# D) Ispisuje maksimalnu vrednost u obe liste
print(l1.maksimum())  # Maksimum u prvoj listi
print(l2.maksimum())  # Maksimum u drugoj listi
print("**********************")

# E) Briše maksimalnu vrednost iz druge liste i ispisuje preostale vrednosti
l2.brisi_vrijednost(l2.maksimum())
l2.print_list()
print("**********************")

# F) Kvadrira sve vrednosti u obe liste
l1.kvadriraj()
l2.kvadriraj()
print("**********************")

# G) Ispisuje dužinu (broj čvorova) u obe liste
print(l1.duzina())  # Dužina prve liste
print(l2.duzina())  # Dužina druge liste
print("**********************")

# H) Briše dva najveća elementa iz prve liste i ispisuje preostale vrednosti
l1.brisi_vrijednost(l1.maksimum())
l1.brisi_vrijednost(l1.maksimum())
l1.print_list()
print(l1.duzina())  # Ispisuje dužinu liste posle brisanja
print("**********************")

# I) Briše prvi element iz prve liste i ispisuje preostale vrednosti
l1.brisi_prvi()
l1.print_list()
"""

#2

"""class UceniciNode():
    def __init__(self, ime, prosj):
        # Svaki čvor sadrži rečnik koji čuva ime učenika i njegov prosek
        self.ucenici = {'ime': ime, 'prosj': prosj}

class LinkedListUcenici:
    def __init__(self, head=None):
        # Glava liste može biti postavljena na prazan čvor pri inicijalizaciji
        self.head = head

    def print(self):
        # Ispisuje podatke svih učenika u listi
        current = self.head
        while current:
            print(current.ucenici)  # Ispisuje rečnik koji sadrži ime i prosek učenika
            current = current.next  # Prelazi na sledeći čvor

    def append(self, new_element):
        # Dodaje novi čvor (učenik) na kraj liste
        current = self.head
        if not current:
            # Ako je lista prazna, novi element postaje glava liste
            self.head = new_element
            new_element.next = None
        else:
            # Ako lista nije prazna, prolazi se kroz listu do kraja
            while current.next:
                current = current.next
            current.next = new_element  # Dodaje novi čvor na kraj
            new_element.next = None  # Poslednji čvor uvek pokazuje na None (nema sledećeg)

    def prosjek(self):
        # Računa i vraća prosek ocena svih učenika u listi
        current = self.head
        count = 0  # Broj učenika
        sum_rate = 0  # Zbir proseka
        while current:
            count = count + 1  # Povećava brojač učenika
            sum_rate = sum_rate + current.ucenici['prosj']  # Dodaje prosek trenutnog učenika u zbir
            current = current.next  # Prelazi na sledeći čvor
        if count != 0:
            return sum_rate / count  # Ako ima učenika, vraća prosek
        else:
            return None  # Ako nema učenika, vraća None

    def prosjek_veci(self, prosjek):
        # Ispisuje učenike čiji je prosek veći od zadate vrednosti
        current = self.head
        while current:
            if current.ucenici['prosj'] > prosjek:
                print(current.ucenici)  # Ispisuje podatke o učeniku čiji je prosek veći od zadatog
            current = current.next  # Prelazi na sledeći čvor

# Kreiranje čvorova za svakog učenika
n1 = UceniciNode('Tamara Pavlovic', 4.2)
n2 = UceniciNode('Dejan Babic', 4.9)
n3 = UceniciNode('Ivan Jovovic', 4.7)
n4 = UceniciNode('Sanel Nisic', 3.2)
n5 = UceniciNode('Benjamin Dobardzic', 4.1)

# Kreiranje povezane liste i dodavanje učenika
ucenici_list = LinkedListUcenici()
ucenici_list.append(n1)
ucenici_list.append(n2)
ucenici_list.append(n3)
ucenici_list.append(n4)
ucenici_list.append(n5)

# Ispisuje sve učenike
ucenici_list.print()
print("*****************")

# Ispisuje prosečnu ocenu svih učenika
print(ucenici_list.prosjek())
print("*****************")

# Ispisuje učenike čiji je prosek veći od proseka svih učenika
ucenici_list.prosjek_veci(ucenici_list.prosjek())

"""

#3

class MoivieNode():
    def __init__(self, name, genre, year, rating):
        # Svaki čvor predstavlja film sa nazivom, žanrom, godinom i ocenom
        self.movie = {'name': name, 'genre': genre, 'year': year, 'rating': rating}

class LinkedListFilms:
    def __init__(self, head=None):
        # Kreira povezanu listu sa opcionalnom početnom glavom
        self.head = head

    def print_values(self):
        # Ispisuje sve filmove u listi
        current = self.head
        while current:
            print(current.movie)  # Ispisuje podatke o trenutnom filmu
            current = current.next  # Prelazi na sledeći čvor (film)

    def append(self, new_element):
        # Dodaje novi film na kraj liste
        current = self.head
        if not current:
            # Ako lista nema elemenata, novi film postaje glava liste
            self.head = new_element
            new_element.next = None
        else:
            # Ako lista već ima elemente, prolazi se kroz listu do poslednjeg elementa
            while current.next:
                current = current.next
            current.next = new_element  # Dodaje novi film na kraj
            new_element.next = None  # Poslednji element nema sledeći čvor (None)

    def avg_rate_per_year(self, year):
        # Računa i vraća prosečnu ocenu filmova za zadatu godinu
        current = self.head
        count = 0  # Broji filmove iz zadate godine
        sum_rate = 0  # Zbir ocena filmova iz zadate godine
        while current:
            if current.movie['year'] == year:
                # Ako je godina filma jednaka zadatoj, dodaje ocenu
                count = count + 1
                sum_rate = sum_rate + current.movie['rating']
            current = current.next
        if count != 0:
            return sum_rate / count  # Ako postoje filmovi iz te godine, vraća prosek
        else:
            return None  # Ako nema filmova iz te godine, vraća None

    def print_movies_greater_than(self, min_year):
        # Ispisuje sve filmove čija je godina izlaska veća ili jednaka zadatoj godini
        current = self.head
        while current:
            if current.movie['year'] >= min_year:
                print(current.movie)  # Ispisuje filmove koji zadovoljavaju uslov
            current = current.next

    def genre_count(self, genre):
        # Broji i vraća broj filmova određenog žanra
        current = self.head
        count = 0  # Brojač filmova sa zadatim žanrom
        while current:
            if current.movie['genre'] == genre:
                count = count + 1  # Uvećava brojač ako žanr odgovara
            current = current.next
        return count  # Vraća ukupan broj filmova sa zadatim žanrom

# Kreiranje čvorova za svaki film sa podacima o filmu (naziv, žanr, godina, ocena)
n1 = MoivieNode('The Batman', 'drama', 2022, 8.1)
n2 = MoivieNode('Joker', 'drama', 2019, 8.4)
n3 = MoivieNode('Dune', 'action', 2021, 8.1)
n4 = MoivieNode('The Shawshank Redemption', 'drama', 1994, 9.3)
n5 = MoivieNode("Don't Look Up", 'comedy', 2021, 7.2)
n6 = MoivieNode('Once Upon a Time... In Hollywood', 'comedy', 2019, 7.6)

# Kreiranje povezane liste i dodavanje filmova
movies_list = LinkedListFilms()
movies_list.append(n1)
movies_list.append(n2)
movies_list.append(n3)
movies_list.append(n4)
movies_list.append(n5)
movies_list.append(n6)

# Ispisuje sve filmove iz liste
movies_list.print_values()
print("**********")

# A) Računa prosečnu ocenu filmova iz 2021. godine
print(movies_list.avg_rate_per_year(2021))
print("**********")

# B) Ispisuje sve filmove koji su izašli 2020. godine ili kasnije
movies_list.print_movies_greater_than(2020)
print("**********")

# C) Ispisuje broj filmova koji su drama
print(movies_list.genre_count('drama'))
