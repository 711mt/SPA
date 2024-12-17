#Imamo podatke o knjigama u biblioteci: naslov, broj stranica, autor i žanr. Svaka knjiga predstavlja čvor u binarnom stablu, koje se slaže prema
#broju stranica(lijevo manje stranica, desno više stranica). Cilj je implementirati funkcije za upravljanje ovim podacima:
# dodavanje knjige u stablo
# pretraga knjiga po žanru
# knjiga sa najviše stranica
# izračunavanje prosječnog broja stranica
# broj knjiga autora
# inorder obilazak stabla

class KnjigaNode:
  def __init__(self,naslov, broj_stranica, autor, zanr):
    self.naslov = naslov
    self.broj_stranica = broj_stranica
    self.autor = autor
    self.zanr = zanr
    self.right = None
    self.left = None

class BinarnoStabloBiblioteka:
  def __init__(self):
    self.root = None

#dodavanje knjige u stablu

  def dodaj_knjigu(self,naslov, broj_stranica, autor, zanr):
    if self.root is None:
      self.root=KnjigaNode(naslov,broj_stranica, autor, zanr)
    else:
      self._dodaj_knjigu(self.root, naslov, broj_stranica, autor, zanr)

  def _dodaj_knjigu(self, node, naslov,broj_stranica, autor, zanr):
    if broj_stranica < node.broj_stranica:
      if node.left is None:
        node.left = KnjigaNode(naslov, broj_stranica, autor, zanr)
      else: 
        self._dodaj_knjigu(node.left, naslov, broj_stranica, autor, zanr)
    else:
      if node.right is None:
        node.right = KnjigaNode(naslov, broj_stranica, autor, zanr)
      else:
        self._dodaj_knjigu(node.left, naslov, broj_stranica, autor, zanr)

# pretraga knjiga po zanru       
  def trazi_po_zanru(self, zanr):
    knjige= []
    self._trazi_po_zanru(self.root, zanr, knjige)
    return knjige
  
#rekurzivna funkcija za trazi_po_zanru
  def _trazi_po_zanru(self, node, zanr, knjige):
    if node:
       if node.zanr == zanr:
          knjige.append(node.naslov)
       self._trazi_po_zanru(node.left, zanr, knjige)
       self._trazi_po_zanru(node.right, zanr, knjige)

# knjiga sa najviše stranica
  def najvise_stranica(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current
  
#drugi nacin za knjigu sa najvise stranica
def max_node(self):
  return self._max_node(self.root)

def _max_node(self, node):
  current = node
  while current.right is not None:
     current = current.right
  return current
  
#izracunavanje prosjecnog broja stranica
  def prosjecan_broj_stranica(self):
        ukupno_strana = [0]
        ukupno_knjiga = [0]
        self._izracunaj_stranicu(self.root, ukupno_strana, ukupno_knjiga)
        return ukupno_strana[0] / ukupno_knjiga[0] if ukupno_knjiga[0] > 0 else 0
     
  def _izracunaj_stranicu(self, node, ukupno_strana, ukupno_knjiga):
        if node:
            ukupno_strana[0] += node.broj_stranica
            ukupno_knjiga[0] += 1
            self._izracunaj_stranicu(node.left, ukupno_strana, ukupno_knjiga)
            self._izracunaj_stranicu(node.right, ukupno_strana, ukupno_knjiga)  
#drugi nacin za izracunavanje prosecnog broja stranica
  def average_pages(self):
     info = [0,0]
     self._average_pages(self.root,info)
     return info[0]/ info[1]
  def _average_pages(self,node, info):
     if node is None:
        return
     info[0] = info[0] + node.broj_stranica
     info[1] = info[1] + 1
     self._average_pages(node.left, info)
     self._average_pages(node.right, info)

#broj knjiga autora
  def broj_autor_knjige(self, autor):
        return self._broj_autor_knjige(self.root, autor)
        
  def _broj_autor_knjige(self, node, autor):
        if not node:
            return 0
        count = 1 if node.autor == autor else 0
        return count + self._count_author_books_recursive(node.left, autor) + \
               self._broj_autor_knjige(node.right, autor)
# drugi nacin za broj knjiga autora
  def br_knjiga_autor(self, autor):
     rezultati = [0]
     self._br_knjiga_autor(self.root,rezultati)
     return rezultati[0]
  def _br_knjiga_autor(self, node,autor, rezultati):
     if node is None:
        return
     else: 
        if node.autor == autor:
           rezultati[0] = rezultati[0] + 1
     self._br_knjiga_autor(node.left, autor, rezultati)
     self._br_knjiga_autor(node.right, autor, rezultati)

#inorder obilazak knjiga
  def inorder(self):
      knjige = []
      self._inorder(self.root, knjige)
      return knjige
        
  def _inorder(self, node, knjige):
      if node:
          self._inorder(node.left, knjige)
          knjige.append((node.naslov, node.broj_stranica, node.autor, node.zanr))
          self._inorder(node.right, knjige)

#Testiranje 

biblioteka = BinarnoStabloBiblioteka()

#dodavanje knjiga
biblioteka.dodaj_knjigu("Hobit", 310, "J.R.R. Tolkien", "Fantazija")
biblioteka.dodaj_knjigu("Ana Karenjina", 864, "Leo Nikolajević Tolstoj", "Novel")
biblioteka.dodaj_knjigu("1984", 328, "George Orwell", "Distopija")



        
    
