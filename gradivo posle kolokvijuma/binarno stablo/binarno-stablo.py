# 1. Binarno stablo sadrzi podatke o turistima(ime i potrosnja) za koje se pamti koliko trose.
# Cvor je turista. U ovom stablu cvorovi se slazu na osnovu vrijednosti atributa potrosnja(lijevo manje vrijednosti, desno vece vrijednosti).
# Radi jednostavnosti, smatrati da su vrijednosti u svakom cvoru binarnog stabla jedinstveni po cijeni(nema ponavljanje).
# a) napisati funkciju dodaj(Node) koja dodaje novog turistu u binarno stablo na osnovu definisane strukture slaganje cvorova(po cijeni)
# b) napisati funkciju trazi(root: Node, min_potrosnja: String) koja treba da vrati imena turista koji su potrosili vise od vrijednosti min_potrosnja
# c) napisati funciju max_potrosnja(root: Node) koja treba da vrati ime turiste cija je potrosnja najveca.
# d) napisati funkciju inorder(root: Node) koja treba da stampa sve cvorove stabla po inorder nacinu obilaska.
# e) sve funkcije je potrebno pozvati i testirati za bar 5 turista.

class Node:
  def __init__(self,ime, potrosnja):
    self.ime = ime
    self.potrosnja = potrosnja
    self.right = None
    self.left = None

class BinarnoStablo:
  def __init__(self):
    self.root = None

  def dodaj(self,ime, potrosnja):
    if self.root is None:
      self.root=Node(ime, potrosnja)
    else:
      self._dodaj(self.root, ime, potrosnja)

  def _dodaj(self, node, ime, potrosnja):
    if potrosnja < node.potrosnja:
      if node.left is None:
        node.left = Node(ime, potrosnja)
      else: 
        self._dodaj(node.left, ime, potrosnja)
    else:
      if node.right is None:
        node.right = Node(ime, potrosnja)
      else:
        self._dodaj(node.left, ime, potrosnja)

  def trazi(self, min_potrosnja):
    rezultati= []
    self._trazi(self.root, min_potrosnja, rezultati)
    return rezultati
#rekurzivna funkcija
  def _trazi(self, node, min_potrosnja,rezultati):
    if node is None:
      return
    if node.potrosnja > min_potrosnja:
      rezultati.append(node.ime)
    self._trazi(node.left,min_potrosnja, rezultati) #lijevi cvor
    self._trazi(node.right, min_potrosnja, rezultati) #desni cvor
  
  def max_potrosnja(self):
    return self._max_potrosnja(self.root)
  
  def _max_potrosnja(self, node):
    if node is None:
      return None
    while node.right is not None:
      node = node.right #node.left ako je u pitanju min_potrosnja
    return node.ime
  
  def inorder(self):
    self._inorder(self.root)

  def _inorder(self, node):
    if node is None:
      return
    self._inorder(node.left)
    print(f"{node.ime} ({node.potrosnja})")
    self._inorder(node.right)

#Testiranje Binarnog stabla

# a) dodavanje turista

binarno_stablo=BinarnoStablo()
binarno_stablo.dodaj("Turista1", 50)
binarno_stablo.dodaj("Turista2", 20)
binarno_stablo.dodaj("Turista3", 30)
binarno_stablo.dodaj("Turista4", 70)
binarno_stablo.dodaj("Turista5", 10)

# b) trazenje turista sa potrosnjom vecom od zadate vrijednosti

min_potrosnja=25
turisti_sa_vecom_potrosnjom = binarno_stablo.trazi(min_potrosnja)
print(f"Turisti sa potrosnjom vecom od {min_potrosnja}: {turisti_sa_vecom_potrosnjom}")

# c) pronalazenje turiste sa najvecom potrosnjom
max_potrosnja_turista = binarno_stablo.max_potrosnja()
print(f"Turista sa najvecom potrosnjom: {max_potrosnja_turista}")
 
# d) Inorder obilazak stabla
print("Inorder obilazak stabla: ")
binarno_stablo.inorder()

 
#2. Za izradu ovog zadatka iskoristiti vec ranije implementirane funkcije: a) kreirati binarno stablo sa bar 5 elemenata gde je vrijednost
# svakog cvora broj. Stampati stablo kao inorder.
# b) napisati metod max_node(self) koji vraca cvor sa najvecom vrijednoscu u kreiranom binarnom stablu.
# c) napisati metode number_of_not_leaves(self) koji vraca broj cvorova binarnog stabla koji nisu list(leaf) (pomoc: broj_cvorova_drveta - broj_leaf_cvorova)

class Node:
  def __init__(self, vrijednost):
    self.vrijednost = vrijednost
    self.left= None
    self.right = None

class BinarnoStablo:
  def __init__(self):
    self.root = None
  
  def dodaj(self, vrijednost):
    if self.root is None:
      self.root=Node(vrijednost)
    else:
      self._dodaj(self.root, vrijednost)

  def _dodaj(self, node,vrijednost):
    if vrijednost < node.vrijednost:
      if node.left is None:
        node.left = Node(vrijednost)
      else:
        self._dodaj(node.left, vrijednost)
    else:
      self._dodaj(node.right, vrijednost)
  
  def inorder(self):
    self._inorder(self.root)
  
  def _inorder(self,node):
    if node is None:
      return
    self._inorder(node.left)
    print(node.vrijednost, end=" ")
    self._inorder(node.right)

  def max_node(self):
    return self._max_node(self.root)
  
  def _max_node(self,node):
    current = node
    while current.right is not None:
      current = current.right
    return current

  def number_of_not_leaves(self):
    total_nodes = self._count_nodes(self.root)
    leaf_nodes = self._count_leaves(self.root)
    return total_nodes - leaf_nodes
  
  def _count_nodes(self,node):
    if node is None:
      return 0
    return 1 + self._count_nodes(node.left) + self._count_nodes(node.right)

  def _count_leaves(self,node):
    if node is None:
      return 0
    if node.left is None and node.right is None:
      return 1
    return self._count_leaves(node.left) + self._count_leaves(node.right)
  
  #Testiranje
binarno_stablo=BinarnoStablo()
binarno_stablo.dodaj(50)
binarno_stablo.dodaj(70)
binarno_stablo.dodaj(20)
binarno_stablo.dodaj(40)
binarno_stablo.dodaj(60)
binarno_stablo.dodaj(80)

#a) Inorder ispis stabla
print("Inorder ispis stabla: ")
binarno_stablo.inorder()
print()

#b) Pronalazenje cvora sa najvecom vrijednoscu
max_node = binarno_stablo.max_node()
print(f"Cvor sa najvecom vrijednoscu: {max_node.vrijednost}")

#c) Brojanje cvorova koji nisu listovi
num_not_leaves = binarno_stablo.number_of_not_leaves()
print(f"Broj cvorova koji nisu listovi: {num_not_leaves}")

#3. Binarno stablo sadrzi podatke o pjevacima(ime i prosjecna godisnja zarada) za koje se pamti koliko prosjecno zaradjuju. Cvor je pjevac
# u ovom stablu cvorovi se slazu na osnovu vrijednosti atributa zarade(lijevo manje vrijednosti, desno vece vrijednosti). Radi jednostavnosti,
# smatrati da su vrijednosti u svakom cvoru binarnog stabla jedinstvene po zaradi(nema ponavljanja).
# a) napisati funkciju dodaj(Node) koja dodaje novog pjevaca u binarno stablo na osnovu definisane strukture slaganja cvorova(po zaradi)
# b) napisati funkciju trazi(root: Node, max_zarada: Float) koja treba da vrati imena pjevaca koji su zaradili manje od vrijednosti max_zarada
# c) napisati funkciju min_zarada(root: Node) koja treba da vrati ime pjevaca cija je prosjecna zarada najveca
# d) napisati funkciju preorder(root: Node) koja treba da stammpa sve cvorove stable po preorder nacinu obilaska
# e) sve funkcije je potrebno pozvati i testirati za bar 5 pjevaca

class Node:
  def __init__(self, ime, zarada):
    self.ime=ime
    self.zarada = zarada
    self.left = None
    self.right = None
class BinarnoStablo:
  def __init__(self):
    self.root = None
  
  def dodaj(self,ime,zarada):
    if self.root is None:
      self.root=Node(ime,zarada)
    else: 
      self._dodaj(self.root, ime, zarada)
  def _dodaj(self, node, ime, zarada):
    if zarada < node.zarada:
      if node.left is None:
        node.left = Node(ime,zarada)
      else:
        self._dodaj(node.left, ime, zarada)
    else:
      if node.right is None:
        node.right = Node(ime, zarada)
      else:
        self._dodaj(node.right, ime, zarada)
  
  def trazi(self, max_zarada):
    rezultati = []
    self._trazi(self.root, max_zarada, rezultati)
    return rezultati
  
  def _trazi(self,node, max_zarada, rezultati):
    if node is None:
      return
    if node.zarada < max_zarada:
      rezultati.append(node.ime)
    self._trazi(node.left, max_zarada, rezultati)
    self._trazi(node.right, max_zarada, rezultati)

  def max_zarada(self):
    return self._max_zarada(self.root)
  def _max_zarada(self,node):
    if node is None:
      return None
    while node.right is not None:
      node=node.right
    return node.ime
  
  def preorder(self):
    self._preorder(self.root)

  def _preorder(self,node):
    if node is Node:
      return
    self._preorder(node.left)
    print(f"{node.ime} ({node.zarada})")
    self._preorder(node.left)
    self._preorder(node.right)

  def postorder(self):
    self._postorder(self.root)

  def _postorder(self,node):
    if node is None:
      return
    self._postorder(node.left)
    self._postorder(node.right)
    print(f"{node.ime} ({node.zarada})")
#Testiranje
binarno_stablo = BinarnoStablo()
binarno_stablo.dodaj("Pjevac1",50000)
binarno_stablo.dodaj("Pjevac2",30000)
binarno_stablo.dodaj("Pjevac3",70000)
binarno_stablo.dodaj("Pjevac4",20000)
binarno_stablo.dodaj("Pjevac5",60000)
# a) dodavanje pjevaca je vec implementirano i testirano kroz kreiranje stabla
# b) trazenje pjevaca sa zaradom manjom od zadate vrijednosti
max_zarada = 60000
pjevaci_sa_manjom_zaradom = binarno_stablo.trazi(max_zarada)
print(f"Pjevaci sa zaradom manjom od {max_zarada}: {pjevaci_sa_manjom_zaradom}")

#c) pronalazenje pjevaca sa najvecom zaradom
max_zarada_pjevac = binarno_stablo.max_zarada()
print(f"Pjevac sa najvecom zaradom: {max_zarada_pjevac}")

# d) Preorder obilazak stabla
print("Preorder obilazak stabla: ")
binarno_stablo.preorder()




  



    







            

