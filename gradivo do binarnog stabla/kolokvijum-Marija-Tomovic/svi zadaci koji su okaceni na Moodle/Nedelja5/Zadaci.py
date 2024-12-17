"""class UceniciNode:
    def __init__(self, ime, prosjek, id_ucenika, razred, izostanci):
        # Svaki čvor sadrži podatke o učeniku: ime, prosjek, ID, razred i broj izostanaka
        self.ucenici = {
            'ime': ime,  # Ime učenika
            'prosj': prosjek,  # Prosjek učenika
            'id': id_ucenika,  # Jedinstveni ID broj učenika
            'razred': razred,  # Razred koji učenik pohađa
            'izostanci': izostanci  # Broj izostanaka učenika
        }
        self.prev = None  # Pokazivač na prethodni čvor u listi, inicijalno postavljen na None
        self.next = None  # Pokazivač na sljedeći čvor u listi, inicijalno postavljen na None

class DoublyLinkedListUcenici:
    def __init__(self, head=None):
        # Inicijalizuje dvostruko olancanu listu sa glavom postavljenom na None, ako nije prosleđena
        self.head = head  # Glava liste (prvi element)
        self.tail = head  # Rep liste (poslednji element), inicijalno isti kao glava

    def print(self):
        # Ispisuje sve podatke o učenicima u listi
        current = self.head  # Počinje od glave liste
        while current:
            print(current.ucenici)  # Ispisuje rečnik sa podacima o trenutnom učeniku
            current = current.next  # Prelazi na sljedeći čvor

    def append(self, new_element):
        # Dodaje novi čvor (učenika) na kraj liste
        if not self.head:
            self.head = new_element  # Ako je lista prazna, novi čvor postaje glava
            self.tail = new_element  # Takođe, rep postaje taj isti čvor jer je to jedini element
        else:
            self.tail.next = new_element  # Povezuje trenutni rep sa novim čvorom kao sljedećim
            new_element.prev = self.tail  # Povezuje novi čvor sa prethodnim (trenutnim repom)
            self.tail = new_element  # Ažurira tail tako da pokazuje na novi zadnji element

    def prosjek(self):
        # Računa prosjek ocjena svih učenika u listi
        current = self.head  # Počinje od glave liste
        count = 0  # Brojač učenika
        sum_rate = 0  # Suma prosjeka svih učenika
        while current:
            count += 1  # Uvećava broj učenika za svakog pronađenog
            sum_rate += current.ucenici['prosj']  # Dodaje prosjek trenutnog učenika zbiru
            current = current.next  # Prelazi na sljedeći čvor
        if count != 0:
            return sum_rate / count  # Vraća prosječan prosjek ako ima učenika
        else:
            return None  # Ako nema učenika, vraća None

    def prosjek_veci(self, prosjek):
        # Ispisuje učenike čiji je prosjek veći od datog prosjeka
        current = self.head  # Počinje od glave liste
        while current:
            if current.ucenici['prosj'] > prosjek:  # Provjerava da li je prosjek učenika veći od zadatog
                print(current.ucenici)  # Ispisuje podatke učenika koji zadovoljava uslov
            current = current.next  # Prelazi na sljedeći čvor

    def find_by_id(self, id_ucenika):
        # Pronalaženje učenika prema ID-u
        current = self.head  # Počinje od glave liste
        while current:
            if current.ucenici['id'] == id_ucenika:  # Provjerava da li ID trenutnog učenika odgovara zadatom
                return current.ucenici  # Ako odgovara, vraća podatke tog učenika
            current = current.next  # Prelazi na sljedeći čvor
        return None  # Ako učenik nije pronađen, vraća None

    def delete_by_id(self, id_ucenika):
        # Brisanje učenika iz liste na osnovu ID-a
        current = self.head  # Počinje od glave liste
        while current:
            if current.ucenici['id'] == id_ucenika:  # Provjerava da li ID trenutnog učenika odgovara zadatom
                if current == self.head:
                    self.head = current.next  # Ako je prvi čvor, ažurira glavu na sljedeći čvor
                    if self.head:
                        self.head.prev = None  # Ako postoji novi prvi čvor, uklanja vezu ka starom
                    if current == self.tail:  # Ako je jedini element u listi, ažurira i tail
                        self.tail = None
                elif current == self.tail:
                    self.tail = current.prev  # Ako je poslednji čvor, ažurira tail na prethodni
                    self.tail.next = None  # Novi tail nema sljedeći čvor
                else:
                    current.prev.next = current.next  # Povezuje prethodni čvor sa sljedećim
                    current.next.prev = current.prev  # Povezuje sljedeći čvor sa prethodnim
                return True  # Vraća True nakon uspješnog brisanja
            current = current.next  # Prelazi na sljedeći čvor
        return False  # Vraća False ako učenik nije pronađen

    def update_prosjek(self, id_ucenika, novi_prosjek):
        # Ažuriranje prosjeka učenika na osnovu ID-a
        current = self.head  # Počinje od glave liste
        while current:
            if current.ucenici['id'] == id_ucenika:  # Provjerava da li ID trenutnog učenika odgovara zadatom
                current.ucenici['prosj'] = novi_prosjek  # Ažurira prosjek učenika
                return True  # Vraća True nakon uspješnog ažuriranja
            current = current.next  # Prelazi na sljedeći čvor
        return False  # Vraća False ako učenik nije pronađen

    def find_most_absent(self):
        # Pronalaženje učenika sa najviše izostanaka
        current = self.head  # Počinje od glave liste
        most_absent = None  # Čuva podatke o učeniku sa najviše izostanaka
        max_izostanci = 0  # Maksimalan broj izostanaka
        while current:
            if current.ucenici['izostanci'] > max_izostanci:  # Provjerava da li trenutni učenik ima više izostanaka
                max_izostanci = current.ucenici['izostanci']  # Ažurira maksimalni broj izostanaka
                most_absent = current.ucenici  # Čuva podatke o učeniku sa najviše izostanaka
            current = current.next  # Prelazi na sljedeći čvor
        return most_absent  # Vraća podatke o učeniku sa najviše izostanaka

    def print_reverse(self):
        # Ispisuje učenike u obrnutom redosledu, koristeći rep (tail)
        current = self.tail  # Počinje od repa liste (poslednji čvor)
        while current:
            print(current.ucenici)  # Ispisuje podatke o trenutnom učeniku
            current = current.prev  # Prelazi na prethodni čvor

# Kreiranje čvorova za svakog učenika
n1 = UceniciNode('Tamara Pavlovic', 4.2, 1, 'IV-1', 5)  # Kreira čvor za Tamara Pavlovic
n2 = UceniciNode('Dejan Babic', 4.9, 2, 'IV-2', 2)  # Kreira čvor za Dejan Babic
n3 = UceniciNode('Ivan Jovovic', 4.7, 3, 'IV-1', 3)  # Kreira čvor za Ivan Jovovic
n4 = UceniciNode('Sanel Nisic', 3.2, 4, 'III-3', 10)  # Kreira čvor za Sanel Nisic
n5 = UceniciNode('Benjamin Dobardzic', 4.1, 5, 'IV-2', 4)  # Kreira čvor za Benjamin Dobardzic

# Kreiranje povezane liste i dodavanje učenika
ucenici_list = DoublyLinkedListUcenici()  # Kreira praznu dvostruko olancanu listu
ucenici_list.append(n1)  # Dodaje čvor n1 na kraj liste
ucenici_list.append(n2)  # Dodaje čvor n2 na kraj liste
ucenici_list.append(n3)  # Dodaje čvor n3 na kraj liste
ucenici_list.append(n4)  # Dodaje čvor n4 na kraj liste
ucenici_list.append(n5)  # Dodaje čvor n5 na kraj liste

# Ispisuje sve učenike
ucenici_list.print()  # Ispisuje podatke svih učenika u listi
print("*****************")

# Pronalaženje učenika prema ID-u
print("Pronalaženje učenika s ID-om 3:")
print(ucenici_list.find_by_id(3))  # Pronalazi učenika sa ID-om 3 i ispisuje podatke
print("*****************")

# Brisanje učenika sa ID-om 2
print("Brisanje učenika sa ID-om 2:")
ucenici_list.delete_by_id(2)  # Briše učenika sa ID-om 2
ucenici_list.print()  # Ponovo ispisuje listu nakon brisanja
print("*****************")

# Ažuriranje prosjeka za učenika sa ID-om 1
print("Ažuriranje prosjeka za učenika sa ID-om 1 na 4.5:")
ucenici_list.update_prosjek(1, 4.5)  # Ažurira prosjek učenika sa ID-om 1 na 4.5
ucenici_list.print()  # Ponovo ispisuje listu nakon ažuriranja prosjeka
print("*****************")

# Prikaz učenika s najviše izostanaka
print("Učenik sa najviše izostanaka:")
print(ucenici_list.find_most_absent())  # Pronalazi i ispisuje učenika sa najviše izostanaka
print("*****************")

# Ispis učenika u obrnutom redosledu
print("Ispis učenika unazad:")
ucenici_list.print_reverse()  # Ispisuje sve učenike u obrnutom redosledu


"""
#2

class MovieNode:
    def __init__(self, name, genre, year, rating, director, duration):
        # Svaki čvor predstavlja film sa dodatnim informacijama o reditelju i trajanju
        self.movie = {
            'name': name,  # Naziv filma
            'genre': genre,  # Žanr filma
            'year': year,  # Godina izlaska filma
            'rating': rating,  # Ocjena filma
            'director': director,  # Reditelj filma
            'duration': duration  # Trajanje filma u minutama
        }
        self.prev = None  # Pokazivač na prethodni čvor (film) u listi
        self.next = None  # Pokazivač na sljedeći čvor (film) u listi

class DoublyLinkedListFilms:
    def __init__(self):
        # Inicijalizuje praznu dvostruko olancanu listu
        self.head = None  # Glava liste (prvi element)
        self.tail = None  # Rep liste (poslednji element)

    def append(self, new_element):
        # Dodaje novi film na kraj liste
        if not self.head:
            # Ako je lista prazna, novi film postaje glava i rep
            self.head = new_element
            self.tail = new_element
        else:
            # Ako lista nije prazna, dodaje novi element na kraj liste
            self.tail.next = new_element  # Povezuje trenutni rep sa novim čvorom
            new_element.prev = self.tail  # Povezuje novi čvor sa prethodnim (trenutnim repom)
            self.tail = new_element  # Ažurira tail tako da pokazuje na novi zadnji element

    def print_values(self):
        # Ispisuje sve filmove u listi
        current = self.head  # Počinje od glave liste
        while current:
            print(current.movie)  # Ispisuje podatke o trenutnom filmu
            current = current.next  # Prelazi na sljedeći čvor (film)

    def avg_rate_per_year(self, year):
        # Računa i vraća prosečnu ocjenu filmova za zadatu godinu
        current = self.head  # Počinje od glave liste
        count = 0  # Broji filmove iz zadate godine
        sum_rate = 0  # Zbir ocjena filmova iz zadate godine
        while current:
            if current.movie['year'] == year:  # Provjerava da li film pripada zadatoj godini
                count += 1  # Povećava brojač filmova
                sum_rate += current.movie['rating']  # Dodaje ocjenu trenutnog filma zbiru
            current = current.next  # Prelazi na sljedeći čvor
        if count > 0:
            return sum_rate / count  # Vraća prosjek ocjena za filmove iz te godine
        return None  # Ako nema filmova iz te godine, vraća None

    def print_movies_greater_than(self, min_year):
        # Ispisuje sve filmove čija je godina izlaska veća ili jednaka zadatoj godini
        current = self.head  # Počinje od glave liste
        while current:
            if current.movie['year'] >= min_year:  # Provjerava da li film zadovoljava uslov
                print(current.movie)  # Ispisuje podatke o filmu
            current = current.next  # Prelazi na sljedeći čvor

    def genre_count(self, genre):
        # Broji i vraća broj filmova određenog žanra
        current = self.head  # Počinje od glave liste
        count = 0  # Brojač filmova sa zadatim žanrom
        while current:
            if current.movie['genre'].lower() == genre.lower():  # Provjerava da li žanr odgovara
                count += 1  # Povećava brojač filmova sa tim žanrom
            current = current.next  # Prelazi na sljedeći čvor
        return count  # Vraća broj filmova sa zadatim žanrom


    def delete_movie(self, name):
        current = self.head  # Postavlja pokazivač 'current' na glavu liste (prvi element).
        
        # Petlja koja prolazi kroz sve čvorove liste dok ne pronađe film ili ne stigne do kraja liste.
        while current:
            if current.movie['name'] == name:  # Provjerava da li naziv filma u trenutnom čvoru odgovara zadatom nazivu.
                
                if current == self.head:  # Ako je trenutni film u glavi (prvi film u listi):
                    self.head = current.next  # Ažurira glavu liste tako da bude sljedeći film.
                    
                    if self.head:  # Ako nakon brisanja postoji nova glava liste (lista nije prazna):
                        self.head.prev = None  # Nova glava više nema prethodni čvor (postaje prva).
                    
                    if current == self.tail:  # Ako je film koji se briše jedini u listi (i glava i rep):
                        self.tail = None  # Postavlja tail (rep) na None jer lista postaje prazna.
                
                elif current == self.tail:  # Ako je trenutni film u repu (poslednji film u listi):
                    self.tail = current.prev  # Ažurira rep liste tako da bude prethodni čvor.
                    self.tail.next = None  # Novi rep više nema sljedeći čvor (postaje poslednji).
                
                else:  # Ako film koji se briše nije ni na početku ni na kraju liste, već između:
                    current.prev.next = current.next  # Povezuje prethodni čvor sa sljedećim (preskače trenutni).
                    current.next.prev = current.prev  # Povezuje sljedeći čvor sa prethodnim (preskače trenutni).
                
                return True  # Vraća True nakon što je film uspješno obrisan iz liste.
            
            current = current.next  # Ako trenutni film nije traženi, prelazi na sljedeći čvor u listi.

        return False  # Ako prođe kroz cijelu listu, a ne pronađe film, vraća False.
    
    

    def update_rating(self, name, new_rating):
        # Ažurira ocjenu filma na osnovu naziva
        current = self.head  # Počinje od glave liste
        while current:
            if current.movie['name'] == name:  # Provjerava da li naziv filma odgovara zadatom
                current.movie['rating'] = new_rating  # Ažurira ocjenu filma
                return True  # Vraća True nakon uspješnog ažuriranja
            current = current.next  # Prelazi na sljedeći čvor
        return False  # Vraća False ako film nije pronađen

    def find_by_director(self, director):
        # Ispisuje sve filmove određenog reditelja
        current = self.head  # Počinje od glave liste
        while current:
            if current.movie['director'].lower() == director.lower():  # Provjerava da li ime reditelja odgovara
                print(current.movie)  # Ispisuje filmove koji zadovoljavaju uslov
            current = current.next  # Prelazi na sljedeći čvor

    def movies_longer_than(self, min_duration):
        # Ispisuje sve filmove duže od zadatog trajanja
        current = self.head  # Počinje od glave liste
        while current:
            if current.movie['duration'] > min_duration:  # Provjerava da li trajanje filma zadovoljava uslov
                print(current.movie)  # Ispisuje filmove sa dužim trajanjem
            current = current.next  # Prelazi na sljedeći čvor

# Kreiranje čvorova za svaki film sa proširenim podacima o reditelju i trajanju
n1 = MovieNode('The Batman', 'drama', 2022, 8.1, 'Matt Reeves', 176)  # Kreira čvor za film 'The Batman'
n2 = MovieNode('Joker', 'drama', 2019, 8.4, 'Todd Phillips', 122)  # Kreira čvor za film 'Joker'
n3 = MovieNode('Dune', 'action', 2021, 8.1, 'Denis Villeneuve', 155)  # Kreira čvor za film 'Dune'
n4 = MovieNode('The Shawshank Redemption', 'drama', 1994, 9.3, 'Frank Darabont', 142)  # Kreira čvor za film 'The Shawshank Redemption'
n5 = MovieNode("Don't Look Up", 'comedy', 2021, 7.2, 'Adam McKay', 138)  # Kreira čvor za film "Don't Look Up"
n6 = MovieNode('Once Upon a Time... In Hollywood', 'comedy', 2019, 7.6, 'Quentin Tarantino', 161)  # Kreira čvor za film 'Once Upon a Time... In Hollywood'

# Kreiranje dvostruko olancane liste i dodavanje filmova
movies_list = DoublyLinkedListFilms()  # Kreira praznu dvostruko olancanu listu filmova
movies_list.append(n1)  # Dodaje čvor n1 na kraj liste
movies_list.append(n2)  # Dodaje čvor n2 na kraj liste
movies_list.append(n3)  # Dodaje čvor n3 na kraj liste
movies_list.append(n4)  # Dodaje čvor n4 na kraj liste
movies_list.append(n5)  # Dodaje čvor n5 na kraj liste
movies_list.append(n6)  # Dodaje čvor n6 na kraj liste

# Ispisuje sve filmove
movies_list.print_values()  # Ispisuje sve filmove u listi
print("**********")

# A) Računa prosečnu ocjenu filmova iz 2021. godine
print(movies_list.avg_rate_per_year(2021))  # Računa i ispisuje prosječnu ocjenu filmova iz 2021. godine
print("**********")

# B) Ispisuje sve filmove koji su izašli 2020. godine ili kasnije
movies_list.print_movies_greater_than(2020)  # Ispisuje filmove koji su izašli 2020. godine ili kasnije
print("**********")

# C) Ispisuje broj filmova koji su drama
print(movies_list.genre_count('drama'))  # Broji i ispisuje broj filmova koji pripadaju žanru 'drama'
print("**********")

# D) Briše film 'Joker' iz liste
movies_list.delete_movie('Joker')  # Briše film 'Joker' iz liste
movies_list.print_values()  # Ispisuje sve filmove nakon brisanja
print("**********")

# E) Ažurira ocjenu filma 'Dune'
movies_list.update_rating('Dune', 8.5)  # Ažurira ocjenu filma 'Dune' na 8.5
movies_list.print_values()  # Ispisuje sve filmove nakon ažuriranja
print("**********")

# F) Ispisuje sve filmove reditelja 'Quentin Tarantino'
print("Filmovi Quentina Tarantina:")
movies_list.find_by_director('Quentin Tarantino')  # Pronalazi i ispisuje sve filmove reditelja 'Quentin Tarantino'
print("**********")

# G) Ispisuje filmove duže od 150 minuta
print("Filmovi duži od 150 minuta:")
movies_list.movies_longer_than(150)  # Ispisuje sve filmove čije trajanje prelazi 150 minuta

