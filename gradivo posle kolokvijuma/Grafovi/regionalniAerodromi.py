# Zadatak da se realizuje program koji će da omogući unos N regionalnih aerodroma, kao i da da mogućnost korisniku da unese veze 
# između unesenih aerodroma. Prilikom dodavanja veze, potrebno je dodati i težinu veze (udaljenost leta u kilometrima između dva aerodroma)
# Zadatak realizovati kroz strukturu grafa, i na kraju omogućiti pretragu najkraćeg puta od startne do krajnje destinacije

import network x as nx

br_aerodroma = int(input("Koliko aerodroma zelite da "))

aerodrom = nx.DiGraph

gradovi = []

for i in range(br_aerodroma):
  aerodrom_ = input("Unesite aerodrom: ")
  gradovi.append(aerodrom_)
  aerodrom.add_node(aerodrom_)

for grad in gradovi:
  br_veza = int(input(f"Koliko veza ima {grad}? "))
  for j in range(br_veza):
    aerodrom.add_edge(grad,input(f"Unesite grad sa kojim {grad} ima vezu: "), weight = int(input("Unesite udaljenost izmedju destinacija: ")))

#add_edge(cvor, cvor, tezina)

print(aerodrom.nodes)
print(aerodrom.edges)

start_aerodrom = "PG"
end_aerodrom = "SAR"
shortest_path= nx.shortest_path(aerodrom, source = start_aerodrom, target = end_aerodrom, weight = 'weight')

print(f"Najkraci put je {shortest_path}")

#realizovati program koji trazi cvor sa najvecim stepenom

graph = nx.Graph()

graph.add_nodes_from(["A","B","C","D","E"])

graph.add_edges_from([
  ("A","B"), ("A","C"),
  ("B","C"), ("B","D"),
  ("C","D"),
  ("D","E"), ("A","E"),
  ("B","E"), ("C","E")
])

def highest_degree(graf):
  highest_degree_ = 0
  highest_node_ = None

  for node, degree in graf.degree():
    if degree >= highest_degree_:
      highest_degree_ = degree
      highest_node_ = node
  return highest_degree_, highest_node_

  degree, node = highest_degree(graph)
  print(f"Cvor sa najvecim stepenom je: {node}, a stepen je {degree}.")


graph.degree() #metoda koja pokazuje stepen svakog cvora