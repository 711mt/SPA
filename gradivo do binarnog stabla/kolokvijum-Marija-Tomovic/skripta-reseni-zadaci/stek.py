# a. Provjeriti da li je zadati string palindrom koristeći stek. String je
# palindrom ako se jednako čita sa lijeve i desne strane.
# Input: 11211 Output:Da
# Input: ad2a Output: Ne
  # Output: Ne
def is_palindrome(s):
    # Koristimo listu kao stek
    stack = []
    
    # Ubacujemo sve znakove stringa u stek
    for char in s:
        stack.append(char)
    
    # Provjeravamo da li su znakovi isti s obje strane
    for char in s:
        if char != stack.pop():
            return "Ne"
    
    return "Da"

# Testiranje
print(is_palindrome("11211"))  # Output: Da
print(is_palindrome("ad2a"))   # Output: Ne
print(is_palindrome("hello"))  # Output: Ne

# b. Dat je stek S u kojem se čuvaju podaci tipa string. Nažalost, neki od
# elemenata steka su bombe (označene sa +). Napišite funkciju
# prebroj_bombe (S) koja će prebrojati koliko bombi ima u steku, a
# ostale elemente poređati u ”naopakom” poretku. Na primjer, ako su
# elementi u S redom od vrha prema dnu steka (‘+’, ‘D’, ‘+’, ‘C’, ‘B’,
# ‘A’), onda funkcija treba da vrati stek (‘A’, ‘B’, ‘C’, ‘D’) i broj bombi 2. Za
# ovaj primjer output bi trebao da izgleda kao ugradjena Python lista
# [(‘A’, ‘B’, ‘C’, ‘D’) , 2]
def prebroj_bombe(S):
    broj_bombi = 0
    novi_stek = []
    
    # Dok ima elemenata u steku
    while S:
        element = S.pop()
        if element == '+':
            broj_bombi += 1  # Povećavamo broj bombi ako naiđemo na '+'
        else:
            novi_stek.append(element)  # Dodajemo elemente koji nisu bombe
    
    # Vraćamo elemente u "naopakom" poretku
    novi_stek.reverse()
    
    return (novi_stek, broj_bombi)

# Testiranje
S = ['+', 'D', '+', 'C', 'B', 'A']
print(prebroj_bombe(S))  # Output: (['A', 'B', 'C', 'D'], 2)

# Napišite funkciju parnepar(S1, S2) koja prima dva steka cijelih brojeva;
# po ulasku u funkciju pretpostavite da je S2 prazan. Funkcija treba da
# prerasporedi elemente steka S1 tako da se po izlasku iz nje u S1
# nalaze svi parni, a u S2 svi neparni elementi, u proizvoljnom poretku.
# Na primjer, ako su elementi u S1 bili (3, 1, 4, 1, 2, 6) onda nakon
# poziva funkcije treba biti S1=(4, 2, 6) i S2=(3, 1, 1)
def parnepar(S1, S2):
    pomocni_stek = []
    
    # Preraspodjela elemenata
    while S1:
        element = S1.pop()
        if element % 2 == 0:
            pomocni_stek.append(element)  # Parni brojevi idu u pomoćni stek
        else:
            S2.append(element)  # Neparni brojevi idu u S2
    
    # Vraćamo parne brojeve u S1 iz pomoćnog steka
    while pomocni_stek:
        S1.append(pomocni_stek.pop())
    
    return S1, S2

# Testiranje
S1 = [3, 1, 4, 1, 2, 6]
S2 = []
print(parnepar(S1, S2))  # Output: ([4, 2, 6], [3, 1, 1])


# d. Napisati funkciju koja će na osnovu ulaznih stekova stek1 i stek2
# stvoriti novi stek koristeći pritom sledeće pravilo da se za novi element
# u novom steku uvek odabere manji od elemenata na vrhu stekova
# stek1 i stek2. Ukoliko se jedan od stekova isprazni, onda uzeti
# preostale elemente iz drugog. Ulazni stekovi moraju nakon završetka
# funkcije ostati nepromijenjeni. Funkcija definisati kao spoji(stek1,
# stek2).
def spoji(stek1, stek2):
    # Kopiramo ulazne stekove da ostanu nepromenjeni
    kopija_stek1 = stek1[:]
    kopija_stek2 = stek2[:]
    novi_stek = []

    # Kombinujemo stekove dok oba imaju elemente
    while kopija_stek1 and kopija_stek2:
        if kopija_stek1[-1] < kopija_stek2[-1]:
            novi_stek.append(kopija_stek1.pop())
        else:
            novi_stek.append(kopija_stek2.pop())

    # Ako je ostalo elemenata u jednom od stekova, dodajemo ih sve u novi stek
    while kopija_stek1:
        novi_stek.append(kopija_stek1.pop())
    while kopija_stek2:
        novi_stek.append(kopija_stek2.pop())

    # Na kraju novi_stek obrnemo kako bi ispunjavao stek pravilo (LIFO)
    novi_stek.reverse()
    return novi_stek

# Testiranje
stek1 = [5, 3, 1]
stek2 = [6, 4, 2]
print(spoji(stek1, stek2))  # Output: [1, 2, 3, 4, 5, 6]
