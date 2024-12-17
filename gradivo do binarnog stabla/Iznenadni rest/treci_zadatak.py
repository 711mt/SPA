#druga dvostruko olancana lista za Zaposlene

class Node:
    def __init__(self, ime, prezime, pozicija, godina_zaposlenja, plata, tim, broj_projekata):
        self.zaposleni = {'ime': ime, 'prezime': prezime, 'pozicija': pozicija, 'godina': godina_zaposlenja, 'plata': plata, 'tim': tim, 'broj_projekata': broj_projekata}
        self.next = None
        self.prev = None

class DoubleLinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
            new_element.prev = current
        else:
            self.head = new_element

    def print_list(self):
        current = self.head
        while current:
            print(current.zaposleni)
            current = current.next

    def prepend(self, node):
        if self.head is None:
            self.head = node
            return
        node.next = self.head
        self.head.prev = node
        self.head = node

    # Funkcija koja pronalazi zaposlenike sa platom većom od prosečne (računati prosečnu platu svih zaposlenih)
    def zaposleni_iznad_proseka(self):
        current = self.head
        total_plata = 0
        count = 0
        while current:
            total_plata += current.zaposleni['plata']
            count += 1
            current = current.next
        if count == 0:
            return []
        average_plata = total_plata / count
        current = self.head
        result = []
        while current:
            if current.zaposleni['plata'] > average_plata:
                result.append(current.zaposleni)
            current = current.next
        return result

    # Funkcija koja ispisuje sve zaposlene koji su angažovani na više od zadatog broja projekata
    def zaposleni_iznad_broja_projekata(self, broj_projekata):
        current = self.head
        while current:
            if current.zaposleni['broj_projekata'] > broj_projekata:
                print(current.zaposleni)
            current = current.next

    # Funkcija koja povećava platu zaposlenima koji su zaposleni duže od zadatog broja godina (u procentima)
    def povecaj_platu(self, godine, procenat):
        current = self.head
        while current:
            if 2024 - current.zaposleni['godina'] > godine:
                current.zaposleni['plata'] += current.zaposleni['plata'] * (procenat / 100)
            current = current.next

    # Funkcija koja vraća listu zaposlenih koji pripadaju određenom timu i imaju platu iznad zadate vrednosti
    def zaposleni_po_timu_i_plati(self, tim, minimalna_plata):
        current = self.head
        result = []
        while current:
            if current.zaposleni['tim'] == tim and current.zaposleni['plata'] > minimalna_plata:
                result.append(current.zaposleni)
            current = current.next
        return result

    # Funkcija za brisanje zaposlenog iz liste na osnovu imena
    def delete_by_ime(self, ime):
        current = self.head
        while current:
            if current.zaposleni['ime'] == ime:
                if current == self.head:
                    self.head = current.next
                    if self.head:
                        self.head.prev = None
                elif current.next:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                else:
                    current.prev.next = None
                return True
            current = current.next
        return False

    # Funkcija koja ažurira broj projekata za određenog zaposlenog na osnovu imena zaposlenog
    def azuriraj_broj_projekata(self, ime, novi_broj_projekata):
        current = self.head
        while current:
            if current.zaposleni['ime'] == ime:
                current.zaposleni['broj_projekata'] = novi_broj_projekata
                return True
            current = current.next
        return False

    # Funkcija koja ispisuje listu zaposlenih prema godini zaposlenja (najpre zaposleni na vrhu liste)
    def ispis_po_godini_zaposlenja(self):
        zaposlenici = []
        current = self.head
        while current:
            zaposlenici.append(current.zaposleni)
            current = current.next
        zaposlenici.sort(key=lambda x: x['godina'])
        for zaposlenik in zaposlenici:
            print(zaposlenik)

# Primer upotrebe
zaposleni1 = Node('Srdjan', 'Radanovic', 'preduzetnik', 2017, 1200, 'Cortex', 21)
zaposleni2 = Node('Natasa', 'Lalevic', 'Backend programerka', 2022, 1000, 'VegaIT', 5)
zaposleni3 = Node('Nikola', 'Jankovic', 'Menadzer', 2015, 1500, 'Backend programeri', 5)
zaposleni4 = Node('Marko', 'Markovic', 'Frontend developer', 2022, 850, 'VegaIT', 10)

l = DoubleLinkedList()
l.append(zaposleni1)
l.append(zaposleni2)
l.append(zaposleni3)
l.append(zaposleni4)
