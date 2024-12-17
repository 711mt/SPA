'''
2. Potrebno je napraviti jednostavan program koji omogućava upravljanje podacima
studenata realizovan kroz binarno pretraživačko stablo. Svaki student je predstavljen kao
čvor u stablu sa sljedećim informacijama:
• Value (rječnik sa podacima o studentu: ime, prezime, ocjene, indeks)
• Svaki čvor može imati lijevo podstablo (studenti sa manjim brojem indeksa) i
desno podstablo (studenti sa većim brojem indeksa).
 Vaš zadatak je da napravite sledeće metode:
• Insert(student_dict) – dodaje novog studenta u binarno stablo prema broju
indeksa
• find_student(indeks) – pretražuje studenta po broju indeksa, vraće podatke o
studentu
• calculate_avg_grade(indeks) – računa prosjek odgovarajućeg studenta
• traverse_right i traverse_left – pronalaze studenta sa najmanjim i najvećim
indeksom
• traverse_nodes_left_subtree – ispisuje podatke o svim studentima u lijevom
podstablu

'''

class Student:
  def __init__(self, ime, prezime, ocjene, indeks):
    self.value = {"ime":ime, "prezime": prezime, "ocjene": ocjene, "indeks":indeks}
    self.right = None
    self.left = None

class StudentStablo:
  def __init__(self, student_node):
    self.root = student_node
  
  def dodaj(self, ime, prezime, ocjene, indeks):
    if self.root is None:
      self.root = Student(ime, prezime,ocjene, indeks)
    else:
      self._dodaj(self.root, ime, prezime, ocjene, indeks)
  
  def _dodaj(self, node, ime, prezime, ocjene, indeks):
    if indeks < node.value.indeks:
      if node. left is None:
        node.left = Student(ime, prezime, ocjene, indeks)
      else:
        self._dodaj(node.left, ime, prezime, ocjene, indeks)
    else:
      if node.right is None:
        node.right = Student(ime, prezime, ocjene, indeks)
      else:
        self._dodaj(node.right, ime, prezime, ocjene, indeks)

  def search(self, indeks):
    rezultati = []
    self._search(self.root, indeks, rezultati)
    return rezultati[0]

  def _search(self, node, indeks, rezultati):
    if node is None:
      return None
    else:
      if node.value['indeks'] == indeks:
        rezultati.append(node.ime)
      self._search(node.left, indeks, rezultati)
      self._search(node.right, indeks, rezultati)
  
  def calculate_avg(self, indeks):
    student = self.search(indeks)
    ocjene_student = student.value['ocjene']
    duzina_niza = len(ocjene_student)

    return sum(ocjene_student) / duzina_niza




