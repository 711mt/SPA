'''
Zamisliti da se radi na aplikaciji za biblioteku koja upravlja velikim brojem knjiga. Svaka knjiga ima sljedece informacije:
Naslov(string)
Autor(string)
Godina izdavanja(integer)

Podaci o knjigama se cuvaju u binarnom stablu gdje je naslov knjige kljuc za sortiranje.
Sledeci zadaci su:
a) Kreiranje strukture binarnog stabla
b) Dodavanje knjige u binarno stablo: implementirati metodu dodaj_knjigu(naslov, autor, godina) koja dodaje novi cvor u stablo na odgovarajuce mjesto
prema abecednom redu naslova.
c) Pretraga knjige po naslovu: implementirati metodu pronadji_knjigu(naslov) koja pretrazuje stablo po naslovu i vraca podatke o knjizi(naslov.autor, godina)
d) Izlistavanje svih knjiga: implementirati metodu izlistaj_knjige() koja koristi in-order prolazak kroz stablo i ispisuje sve knjige abecednim redom
e) Brisanje knjige: implementirati metodu obrisi_knjigu(naslov) koja brise knjigu iz stabla, uz korektno azuriranje cvorova
f) Azuriranje podataka o knjizi: dodati metodu azuriraj_knjigu(naslov, novi_autor, nova_godina) koja pronalazi cvor i mijenja informacije o autoru i godini
'''
class Knjiga:
    def __init__(self, naslov, autor, godina):
        self.naslov = naslov
        self.autor = autor
        self.godina = godina
        self.left = None
        self.right = None

class Biblioteka:
    def __init__(self):
        self.root = None

    def dodaj_knjigu(self, naslov, autor, godina):
        if not self.root:
            self.root = Knjiga(naslov, autor, godina)
        else:
            self._dodaj(self.root, naslov, autor, godina)

    def _dodaj(self, node, naslov, autor, godina):
        if naslov < node.naslov:
            if node.left is None:
                node.left = Knjiga(naslov, autor, godina)
            else:
                self._dodaj(node.left, naslov, autor, godina)
        else:
            if node.right is None:
                node.right = Knjiga(naslov, autor, godina)
            else:
                self._dodaj(node.right, naslov, autor, godina)

    def pronadji_knjigu(self, naslov):
        return self._pronadji(self.root, naslov)

    def _pronadji(self, node, naslov):
        if node is None or node.naslov == naslov:
            return node
        if naslov < node.naslov:
            return self._pronadji(node.left, naslov)
        return self._pronadji(node.right, naslov)

    def izlistaj_knjige(self):
        self._inorder_prolazak(self.root)

    def _inorder_prolazak(self, node):
        if node:
            self._inorder_prolazak(node.left)
            print(f"Naslov: {node.naslov}, Autor: {node.autor}, Godina: {node.godina}")
            self._inorder_prolazak(node.right)

    def obrisi_knjigu(self, naslov):
        self.root = self._obrisi(self.root, naslov)
   
    def _obrisi(self, node, naslov):
        if not node:
            return node
        if naslov < node.naslov:
            node.left = self._obrisi(node.left, naslov)
        elif naslov > node.naslov:
            node.right = self._obrisi(node.right, naslov)
        else:
            if not node.left:
                return node.right
            elif not node.right:
                return node.left
            temp = self._nadji_minimum(node.right)
            node.naslov = temp.naslov
            node.autor = temp.autor
            node.godina = temp.godina
            node.right = self._obrisi(node.right, temp.naslov)
        return node

    def _nadji_minimum(self, node):
        current = node
        while current.left:
            current = current.left
        return current

    def azuriraj_knjigu(self, naslov, novi_autor, nova_godina):
        knjiga = self.pronadji_knjigu(naslov)
        if knjiga:
            knjiga.autor = novi_autor
            knjiga.godina = nova_godina
            return True
        return False
    






'''
def main():
    biblioteka = Biblioteka()
    
    while True:
        print("\n1. Dodaj knjigu")
        print("2. Pronadji knjigu")
        print("3. Izlistaj sve knjige")
        print("4. Obrisi knjigu")
        print("5. Azuriraj knjigu")
        print("6. Izlaz")
        
        izbor = input("Izaberite opciju: ")
        
        if izbor == "1":
            naslov = input("Unesite naslov: ")
            autor = input("Unesite autora: ")
            godina = int(input("Unesite godinu: "))
            biblioteka.dodaj_knjigu(naslov, autor, godina)
            print("Knjiga je uspjesno dodata!")
            
        elif izbor == "2":
            naslov = input("Unesite naslov za pretragu: ")
            knjiga = biblioteka.pronadji_knjigu(naslov)
            if knjiga:
                print(f"Pronadjena knjiga: {knjiga.naslov}, {knjiga.autor}, {knjiga.godina}")
            else:
                print("Knjiga nije pronadjena")
                
        elif izbor == "3":
            print("\nSve knjige:")
            biblioteka.izlistaj_knjige()
            
        elif izbor == "4":
            naslov = input("Unesite naslov knjige za brisanje: ")
            biblioteka.obrisi_knjigu(naslov)
            print("Knjiga je obrisana ako je postojala")
            
        elif izbor == "5":
            naslov = input("Unesite naslov knjige za azuriranje: ")
            novi_autor = input("Unesite novog autora: ")
            nova_godina = int(input("Unesite novu godinu: "))
            if biblioteka.azuriraj_knjigu(naslov, novi_autor, nova_godina):
                print("Knjiga je uspjesno azurirana!")
            else:
                print("Knjiga nije pronadjena")
                
        elif izbor == "6":
            break

if __name__ == "__main__":
    main()
'''