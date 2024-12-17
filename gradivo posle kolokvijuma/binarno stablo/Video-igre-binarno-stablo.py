#Imamo podatke o video igrama: naziv, broj igraca, zanr i platforma. Svaka video igra je cvor u binarnom stablu,koje se slaze
# prema broju igraca(lijevo manje igraca, desno vise igraca). Cilj je implementirati funkcije za upravljanje ovim podacima.
# dodavanje igara u stablo prema broju igraca
# pretraga po zanru
# najpopularnija igra
# prosjecan broj igraca
# brojanje igara po platformi
# inorder obilazak

class VideoGame:
    def __init__(self, naziv, igraci, zanr, platforma):
        self.naziv = naziv
        self.igraci = igraci
        self.zanr = zanr
        self.platforma = platforma
        self.left = None
        self.right = None

class IgricaBinarnoStablo:
    def __init__(self):
        self.root = None
        
    def dodaj_igru(self, naziv, igraci, zanr, platforma):
        if not self.root:
            self.root = VideoGame(naziv, igraci, zanr, platforma)
        else:
            self._dodaj_igru(self.root,naziv, igraci, zanr, platforma)
            
    def _dodaj_igru(self, node, naziv, igraci, zanr, platforma):
        if igraci < node.igraci:
            if node.left is None:
                node.left = VideoGame(naziv, igraci, zanr, platforma)
            else:
                self._dodaj_igru(node.left, naziv, igraci, zanr, platforma)
        else:
            if node.right is None:
                node.right = VideoGame(naziv, igraci, zanr, platforma)
            else:
                self._dodaj_igru(node.right, naziv, igraci, zanr, platforma)
                
    def trazi_po_zanru(self, zanr):
        igre = []
        self._trazi_po_zanru(self.root, zanr, igre)
        return igre
        
    def _trazi_po_zanru(self, node, zanr,igre):
        if node:
            if node.zanr == zanr:
                igre.append(node.naziv)
            self._trazi_po_zanru(node.left, zanr, igre)
            self._trazi_po_zanru(node.right, zanr, igre)
            
    def najpopularnija_igra(self):
        if not self.root:
            return None
        current = self.root
        while current.right:
            current = current.right
        return current
        
    def prosjecni_broj_igraca(self):
        ukupno_igraca = [0]
        ukupno_igrica = [0]
        self._izracunaj_prosjecni_broj_igraca(self.root, ukupno_igraca, ukupno_igrica)
        return ukupno_igraca[0] / ukupno_igrica[0] if ukupno_igrica[0] > 0 else 0
        
    def _izracunaj_prosjecni_broj_igraca(self, node, ukupno_igraca, ukupno_igrica):
        if node:
            ukupno_igraca[0] += node.igraci
            ukupno_igrica[0] += 1
            self._izracunaj_prosjecni_broj_igraca(node.left, ukupno_igraca, ukupno_igrica)
            self._izracunaj_prosjecni_broj_igraca(node.right, ukupno_igraca, ukupno_igrica)
            
    def brojanje_po_platformi(self, platforma):
        return self._brojanje_po_platformi(self.root, platforma)
        
    def _brojanje_po_platformi(self, node, platforma):
        if not node:
            return 0
        count = 1 if node.platforma == platforma else 0
        return count + self._brojanje_po_platformi(node.left, platforma) + \
               self._brojanje_po_platformi(node.right, platforma)
    #inorder obilazak knjiga
    def inorder(self):
      igrice = []
      self._inorder(self.root, igrice)
      return igrice
        
    def _inorder(self, node, igrice):
      if node:
          self._inorder(node.left, igrice)
          igrice.append((node.naziv, node.igraci, node.zanr, node.platforma))
          self._inorder(node.right, igrice)

# kreiranje igrica u binarnom stablu
igrice = IgricaBinarnoStablo()

# Dodavanje igrica
igrice.dodaj_igru("Minecraft", 1000000, "Sandbox", "PC")
igrice.dodaj_igru("FIFA 23", 500000, "Sports", "PS5")
igrice.dodaj_igru("The Last of Us", 200000, "Action", "PS5")
igrice.dodaj_igru("Mario Kart", 800000, "Racing", "Switch")
igrice.dodaj_igru("Counter-Strike", 900000, "FPS", "PC")

# Pretrazivanje igrica po zanru
fps_igrice = igrice.trazi_po_zanru("FPS")
print("FPS igrice:", fps_igrice)

# Najpopularnija igrica
most_popular = igrice.najpopularnija_igra()
print("Najpopularnija igrica:", most_popular.naziv, most_popular.igraci)

# Izracunavanje prosjecnog broja igraca
avg_players = igrice.prosjecni_broj_igraca()
print("Prosjecni broj igraca:", avg_players)

# Brojanje ifara po platformi
pc_games = igrice.brojanje_po_platformi("PC")
print("PC igrice:", pc_games)

# Get sorted list of games by player count
sortirane_igrice = igrice.inorder()
print("Igrice koje su sortirane po broju igraca:")
for igrice in sortirane_igrice:
    print(f"Naziv: {igrice[0]}, Igraci: {igrice[1]}, Zanr: {igrice[2]}, Platforma: {igrice[3]}")


