#1. Pronalaženje maksimalne vrednosti u tuplu
def max_in_tuple(tup):
    # Ako je tuple prazan, vraćamo None (nema maksimalne vrednosti)
    if not tup:
        return None
    # Ako tuple ima samo jedan element, taj element je maksimalan
    elif len(tup) == 1:
        return tup[0]
    else:
        # Rekurzivno pozivamo funkciju na tuple bez prvog elementa
        max_of_rest = max_in_tuple(tup[1:])
        # Vraćamo veći broj između prvog elementa i maksimalnog od ostatka
        return tup[0] if tup[0] > max_of_rest else max_of_rest

# Primer upotrebe
print(max_in_tuple((3, 5, 2, 9, 1)))  # Izlaz: 9


#2.  Suma elemenata tuple-a

def sum_of_tuple(tup):
    # Ako je tuple prazan, suma je 0
    if not tup:
        return 0
    else:
        # Prvi element dodajemo sumi ostatka tuple-a rekurzivno
        return tup[0] + sum_of_tuple(tup[1:])

# Primer upotrebe
print(sum_of_tuple((1, 2, 3, 4)))  # Izlaz: 10


#3.Brojanje određenog elementa u tuple-u
def count_element_in_tuple(tup, element):
    # Ako je tuple prazan, brojanje završava i rezultat je 0
    if not tup:
        return 0
    else:
        # Dodajemo 1 ako je prvi element jednak traženom, i nastavljamo rekurziju
        count_in_rest = count_element_in_tuple(tup[1:], element)
        return (1 if tup[0] == element else 0) + count_in_rest

# Primer upotrebe
print(count_element_in_tuple((1, 2, 3, 2, 2, 4), 2))  # Izlaz: 3

#4. 
# Evo koda za svaki od predloženih zadataka sa komentarima koji objašnjavaju svaki deo rekurzivne funkcije.

# 1. Pronalaženje maksimalne vrednosti u tuplu
# python
# Copy code
def max_in_tuple(tup):
    # Ako je tuple prazan, vraćamo None (nema maksimalne vrednosti)
    if not tup:
        return None
    # Ako tuple ima samo jedan element, taj element je maksimalan
    elif len(tup) == 1:
        return tup[0]
    else:
        # Rekurzivno pozivamo funkciju na tuple bez prvog elementa
        max_of_rest = max_in_tuple(tup[1:])
        # Vraćamo veći broj između prvog elementa i maksimalnog od ostatka
        return tup[0] if tup[0] > max_of_rest else max_of_rest

# Primer upotrebe
print(max_in_tuple((3, 5, 2, 9, 1)))  # Izlaz: 9
# 2. Suma elemenata tuple-a
# python
# Copy code
def sum_of_tuple(tup):
    # Ako je tuple prazan, suma je 0
    if not tup:
        return 0
    else:
        # Prvi element dodajemo sumi ostatka tuple-a rekurzivno
        return tup[0] + sum_of_tuple(tup[1:])

# Primer upotrebe
print(sum_of_tuple((1, 2, 3, 4)))  # Izlaz: 10
# 3. Brojanje određenog elementa u tuple-u
# python
# Copy code
def count_element_in_tuple(tup, element):
    # Ako je tuple prazan, brojanje završava i rezultat je 0
    if not tup:
        return 0
    else:
        # Dodajemo 1 ako je prvi element jednak traženom, i nastavljamo rekurziju
        count_in_rest = count_element_in_tuple(tup[1:], element)
        return (1 if tup[0] == element else 0) + count_in_rest

# Primer upotrebe
print(count_element_in_tuple((1, 2, 3, 2, 2, 4), 2))  # Izlaz: 3

# 4. Preokretanje tuple-a
def reverse_tuple(tup):
    # Ako je tuple prazan, vraćamo prazan tuple
    if not tup:
        return ()
    else:
        # Prvi element postavljamo na kraj tuple-a i rekurzivno prolazimo kroz ostatak
        return reverse_tuple(tup[1:]) + (tup[0],)

# Primer upotrebe
print(reverse_tuple((1, 2, 3)))  # Izlaz: (3, 2, 1)

#5  rekurzija da pronadjemo nekku odredjenu vrednost iz tuple?

def find_in_tuple(tup, value):
    # Ako je tuple prazan, vrednost nije pronađena, vraćamo False
    if not tup:
        return False
    # Ako je prvi element jednak traženoj vrednosti, vraćamo True
    elif tup[0] == value:
        return True
    else:
        # Nastavljamo pretragu u ostatku tuple-a
        return find_in_tuple(tup[1:], value)

# Primer upotrebe
print(find_in_tuple((1, 2, 3, 4, 5), 3))  # Izlaz: True
print(find_in_tuple((1, 2, 3, 4, 5), 6))  # Izlaz: False
