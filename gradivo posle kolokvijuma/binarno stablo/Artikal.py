'''
Binarno stablo sadrzi podatke o artiklima(naziv i cenu), cvor je artikal. 
a. Napisati funkciju trazi(root: Node, naziv: String) koja ce da vrati cijenu artikla sa navedenim nazivom ili None, ukoliko navedeni artikal
ne postoji u stablu.
d. Napisati funkciju dubina(root:Node) koja ce izracunati dubinu stabla.
e. Racuna i stampa proizvod dva najmanja cvora u binarnom stablu(za dva cvora se smatra da su najmanja, ako su im vrijednosti najmanje)
f. Racuna i stampa sumu svih elemenata binarnog stabla, cija je vrijednost cvora veca od 10
g. Napisati funkciju ogledalo_stablo(root:Node) koja ce svakom cvoru medjusobno zamijeniti lijevo i desno podstablo
h. Napraviti metode za pravljenje ovakvog stabla, kao i test program koji ce omoguciti ucitavanje elemenata, pravljenje stabla i trazenje
zadatog elementa.

'''
class ArtikalNode:
    def __init__(self, naziv, cijena):
        self.naziv = naziv
        self.cena = cijena
        self.left = None
        self.right = None

class ArtikalBinaryTree:
    def __init__(self):
        self.root = None
    
    def dodaj(self, naziv, cijena):
        if not self.root:
            self.root = ArtikalNode(naziv, cijena)
        else:
            self._dodaj(self.root, naziv, cijena)
    
    def _dodaj(self, node, naziv, cijena):
        if naziv < node.naziv:
            if node.left is None:
                node.left = ArtikalNode(naziv, cijena)
            else:
                self._dodaj(node.left, naziv, cijena)
        else:
            if node.right is None:
                node.right = ArtikalNode(naziv, cijena)
            else:
                self._dodaj(node.right, naziv, cijena)

    def trazi1(self, root, naziv):
        if not root:
            return None
        if root.naziv == naziv:
            return root.cijena
        if naziv < root.naziv:
            return self.trazi1(root.left, naziv)
        return self.trazi1(root.right, naziv)
#drugi nacin za trazenje
    def trazi(self,cijena):
        rezultati=[]
        self._trazi(self.root,cijena,rezultati)
        return rezultati
    def _trazi(self,node,cijena,rezultati):
        if node is None:
            return 
        if node.cijena == cijena:
            rezultati.append(node.naziv)
        self._trazi(node.left,cijena, rezultati)
        self._trazi(node.right, cijena, rezultati)

    def dubina(self, root):
        if not root:
            return 0
        left_depth = self.dubina(root.left)
        right_depth = self.dubina(root.right)
        return max(left_depth, right_depth) + 1
#drugi nacin za dubinu
    def depth(self):
        depth =[0]
        self._depth(self.root, depth)
        return depth[0]
    def _depth(self,node,depth, progress = 0):
        if node is None:
            return
        if depth[0] < progress:
            depth[0] = progress
        self._depth(node.left, depth, progress + 1)
        self._depth(node.right, depth, progress + 1)

    def nadji_dva_najmanja(self, root):
        vrijednosti = []
        def inorder(node):
            if node:
                inorder(node.left)
                vrijednosti.append(node.cijena)
                inorder(node.right)
        inorder(root)
        if len(vrijednosti) >= 2:
            vrijednosti.sort()
            return vrijednosti[0] * vrijednosti[1]
        return None
# drugi nacin za nadji_dva_najmanja cvora
    def proizvod_najmanjih(self):
        if self.root is None or self.root.left is None:
            return None
        return self._proizvod_najmanjih(self.root)
    def _proizvod_najmanjih(self,current):
        if current.left.left is None:
            return current.cijena * current.left.cijena
        return self._proizvod_najmanjih(current.left)
    
    def suma_vecih_od_10(self, root):
        if not root:
            return 0
        suma = 0
        if root.cijena > 10:
            suma += root.cijena
        return suma + self.suma_vecih_od_10(root.left) + self.suma_vecih_od_10(root.right)
  # drugi nacin za sumu vecih od 10
    def calculate_10(self):
        results = [0]
        self._calculate_10(self.root, results)
        return results[0]
    def _calculate_10(self,node, results):
        if node is None:
            return
        if node.cijena >= 10:
            results[0] = results[0] + node.cijena
        self._calculate_10(node.left, results)
        self._calculate_10(node.right, results)
            

    def ogledalo_stablo(self, root):
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.ogledalo_stablo(root.left)
        self.ogledalo_stablo(root.right)
        return root

#metode za pravljenje stabla, test program za ucitavanje elemenata
    def inorder(self):
      self._inorder(self.root)

    def _inorder(self,node):
        if node is None:
            return None
        self._inorder(node.left)
        print(f"{node.naziv}, {node.cijena}")
        self._inorder(node.right)
        

