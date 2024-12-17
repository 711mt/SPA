'''
Imamo podatke o predavacima: ime, broj odrzanih casova, plata, predmet i ocjena predavaca. Svaki predavac predstavlja cvor u binarnom stablu,
koji se slaze prema broju odrzanih casova (lijevo manje casova, desno vise casova). Cilj je implementirati funkcije za upravljanje ovim podacima.
1. Dodavanje predavaca u stablo
2. Pretraga predavaca po predmetu
3. Predavac sa najvecim brojem odrzanih casova
4. Predavac sa najmanjim brojem odrzanih casova
5. Izracunavanje prosjecne plate predavaca
6. Broj predavaca sa ocjenom iznad zadate vrijednosti
7. Pronalazenje predavaca sa najvisom ocjenom
8. Pronalazenje predavaca sa najnizom ocjenom
9. Ukupan broj predavaca u stablu
10. Broj predavaca cija plata prelazi u zadatu vrijednost
11. Ukupan broj odrzanih casova svih predavaca zajedno
12. Inorder obilazak stabla
'''

class PredavacNode:
    def __init__(self, ime, broj_casova, plata, predmet, ocjena_predavaca):
        self.ime = ime
        self.broj_casova = broj_casova
        self.plata = plata
        self.predmet = predmet
        self.ocjena_predavaca = ocjena_predavaca
        self.left = None
        self.right = None

class PredavacBinarnoStablo:
    def __init__(self):
        self.root = None
#dodavanje
    def dodaj(self, ime, broj_casova, plata, predmet, ocjena_predavaca):
        if not self.root:
            self.root = PredavacNode(ime, broj_casova, plata, predmet, ocjena_predavaca)
        else:
            self._dodaj(self.root, ime, broj_casova , plata, predmet, ocjena_predavaca)

    def _dodaj(self, node, ime, broj_casova, plata, predmet, ocjena_predavaca):
        if broj_casova < node.broj_casova:
            if node.left is None:
                node.left = PredavacNode(ime, broj_casova, plata, predmet, ocjena_predavaca)
            else:
                self._dodaj(node.left,ime, broj_casova, plata, predmet, ocjena_predavaca)
        else:
            if node.right is None:
                node.right = PredavacNode(ime, broj_casova, plata, predmet, ocjena_predavaca)
            else:
                self._dodaj(node.right, ime, broj_casova, plata, predmet, ocjena_predavaca)

    def search_by_subject(self, predmet):
        rezultati = []
        self._search_by_subject(self.root, predmet, rezultati)
        return rezultati

    def _search_by_subject(self, node, predmet, rezultati):
        if node:
            if node.predmet == predmet:
                rezultati.append(node)
            self._search_by_subject_(node.left, predmet, rezultati)
            self._search_by_subject_(node.right, predmet, rezultati)

    def find_max_classes(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current

    def find_min_classes(self):
        if not self.root:
            return None
        current = self.root
        while current.left:
            current = current.left
        return current

    def calculate_average_salary(self):
        ukupna_plata = [0]
        count = [0]
        
        def traverse(node):
            if node:
                ukupna_plata[0] += node.plata
                count[0] += 1
                traverse(node.left)
                traverse(node.right)
        
        traverse(self.root)
        return ukupna_plata[0] / count[0] if count[0] > 0 else 0
#drugi način
   def prosjecna_plata(self):
    ukupna_plata = 0
    broj_predavaca = 0

   def _calculate(root):
    nonlocal ukupna_plata, broj_predavaca
    if root:
      ukupna_plata += root.plata
      broj_predavaca += 1
   _calculate (self.root)
   return ukupna_plata / broj_predavaca

   def broj_predavaca_ocjenom_iznad(self):
    vrijednost = 5
    brojac = 0
   def _count(root):
    nonlocal brojac
    if root:
      if root.ocjena_predavaca > vrijenost:
        brojac+=1
      _count(root.left)
      _count(root.right)
   _count(self.root)
   return brojac

    def count_above_rating(self, min_ocjena_predavaca):
        def count_(node):
            if not node:
                return 0
            count = 1 if node.ocjena_predavaca > min_ocjena_predavaca else 0
            return count + count_(node.left) + count_(node.right)
        return count_(self.root)

    def find_highest_rating(self):
        highest = [None]
        
        def traverse(node):
            if node:
                if not highest[0] or node.ocjena_predavaca > highest[0].ocjena_predavaca:
                    highest[0] = node
                traverse(node.left)
                traverse(node.right)
        
        traverse(self.root)
        return highest[0]

    def find_lowest_rating(self):
        lowest = [None]
        
        def traverse(node):
            if node:
                if not lowest[0] or node.ocjena_predavaca < lowest[0].ocjena_predavaca:
                    lowest[0] = node
                traverse(node.left)
                traverse(node.right)
        
        traverse(self.root)
        return lowest[0]

    def get_total_nodes(self):
        def count_(node):
            if not node:
                return 0
            return 1 + count_(node.left) + count_(node.right)
        return count_(self.root)

    def count_above_salary(self, min_plata):
        def count_(node):
            if not node:
                return 0
            count = 1 if node.plata > min_plata else 0
            return count + count_(node.left) + count_(node.right)
        return count_(self.root)

    def get_total_classes(self):
        def sum_(node):
            if not node:
                return 0
            return node.broj_casova + sum_(node.left) + sum_(node.right)
        return sum_(self.root)

    def inorder(self):
        rezultati = []
        def obilazak(node):
            if node:
                obilazak(node.left)
                rezultati.append(node)
                obilazak(node.right)
        obilazak(self.root)
        return rezultati

