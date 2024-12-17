'''
1. zadatak - implementirati binarno stablo koje čuva raspored vožnje autobusa podanima.
Svaki dan u stablu se predstavlja kao čvor u stablu sa atributima:
• value - lista autobuskih stanica i vremena polaska, dan u nedjelji (double list objekat)
• left - pokazivač na lijevo podstablo
• right - pokazivač na desno podstablo
Zadatak je da se realizuje implementacija klase BinaryTree kako bi omogućila sledeće operacije:
• Dodavanje novog rasporeda vožnje za određeni dan pomoću metode insert(data). Ukoliko već postoji raspored vožnje za određeni dan, prikazati
odgovarajuću poruku.
• Pretraga rasporeda za određeni dan pomoću metode find_bus_stops(dan).
Ako raspored postoji, metoda vraće listu stanica i vremena. U suprotnom, metoda treba da vrati odgovarajuće poruke (kada stablo nema korijen, kada ne
postoji određeni dan u stablu rasporeda)
'''
class Node:
    def __init__(self, stanica, cijena):
        self.stanica = stanica
        self.cijena = cijena
        self.next = None
        self.prev = None

class Double_List:
    def __init__(self, dan:int, head = None, tail = None):
        self.head = head
        self. dan = dan
        self.tail = tail
    def print_list(self):
        current = self.head
        while current:
            print(current.stanica, current.cijena)
            current = current.next

    def append_tail(self, element: Node):
        if self.head is None:
            self.head = element
            self.tail = element
        else:
            current = self.tail
            current.next = element
            element.prev = current
            self.tail = element
class Dan:
    def __init__(self, value: Double_List):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root):
        self.root = Dan(root)
    
    def insert(self, data):
        if self.root is None:
            self.root = Dan(data)
        else:
            self._insert(data, self.root)

    def _insert(self, data, current_node):
        if data.dan < current_node.value.dan:
            if current_node.left is None:
                current_node.left = Dan(data)
            else:
                self._insert(data, current_node.left)
        elif data.dan > current_node.value.dan:
            if current_node.right is None:
                current_node.right = Dan(data)
            else:
                self._insert(data, current_node.right)
        else:
            return "Vrijednost je vec u stablu"
#pretraga u binarnom stablu
    def find_bus_stops(self, dan:int):
        if self.root is None:
            return "Ne postoje rasporedi voznje"
        elif self.root.value.dan == dan:
            return self.root.value.print_list()
        else:
            if self.root.value.dan > dan:
                self._find_bus_stops(dan, self.root.left)
            else:
                self._find_bus_stops(dan, self.root.right)
    def _find_bus_stops(self,dan, current_node):
        indeks_dan = current_node.value.dan
        if indeks_dan == dan:
            return current_node.value.print_list()
        elif indeks_dan > dan:
            if current_node.left is not None:
                self._find_bus_stops(dan, current_node.left)
            else:
                return "U stablu ne postoji ovaj cvor"
        else:
            if current_node.right is not None:
                self._find_bus_stops(dan, current_node.right)
            else:
                return "U stablu ne postoji ovaj cvor"

node1 = Node("Stanica 1", "0.5")
node2 = Node("Stanica 2", "2.5")
node3 = Node("Stanica 3", "2.75")
node4 = Node("Stanica 4", "1.5")
node5 = Node("Stanica 5", "3.5")
node6 = Node("Stanica 6", "2.7")

double_list_srijeda = Double_List(3)
double_list_srijeda.append_tail(node1)
double_list_srijeda.append_tail(node2)
double_list_srijeda.append_tail(node3)
double_list_srijeda.append_tail(node4)
double_list_srijeda.append_tail(node5)
double_list_srijeda.append_tail(node6)

binarno = BinaryTree(double_list_srijeda)
binarno.insert(double_list_srijeda)
    
        
        


    

