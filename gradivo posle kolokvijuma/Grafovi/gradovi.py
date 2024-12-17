# Dati podaci predstavljaju povezane gradove u Crnoj Gori, gdje su tezine grana(atribut weight) udaljenosti izmedju njih u kilometrima
# Konkretno, udaljenosti izmedju gradova su: Podgorica -> Niksic: 54km; Cetinje: 29km; Bar: 53km; Budva: 65km; Herceg Novi: 118km;
                                            # Niksic -> Pljevlja: 104km; Zabljak: 72km; Herceg Novi: 96km
                                            # Cetinje -> Budva: 31km; Herceg Novi: 91km;
                                            # Bar -> Ulcinj: 25km; Budva: 41km
                                            # Budva -> Herceg Novi: 58km
                                            # Herceg Novi -> Kotor: 43km
# 1. Pronaci najkraci put izmedju gradova Podgorica i Ulcinj i ispisati rezultat
# 2. Pronaci grad sa najvecim brojem povezanih susjeda
# 3. Pronaci sve gradove koji su povezani sa Podgoricom
# 4. Vizuelizovati graf
# koristi se network x biblioteka

import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

edges = [
    ("Podgorica", "Niksic", 54),
    ("Podgorica", "Cetinje", 29),
    ("Podgorica", "Bar", 53),
    ("Podgorica", "Budva", 65),
    ("Podgorica", "Herceg Novi", 118),
    ("Niksic", "Pljevlja", 104),
    ("Niksic", "Zabljak", 72),
    ("Niksic", "Herceg Novi", 96),
    ("Cetinje", "Budva", 31),
    ("Cetinje", "Herceg Novi", 91),
    ("Bar", "Ulcinj", 25),
    ("Bar", "Budva", 41),
    ("Budva", "Herceg Novi", 58),
    ("Herceg Novi", "Kotor", 43)
]


G.add_weighted_edges_from(edges)

# 1. 
shortest_path = nx.shortest_path(G, "Podgorica", "Ulcinj", weight="weight")
shortest_distance = nx.shortest_path_length(G, "Podgorica", "Ulcinj", weight="weight")
print(f"Najkraci put od Podgorice do Ulcinja: {' -> '.join(shortest_path)}")
print(f"Ukupna udaljenost: {shortest_distance} km")

# 2. 
degrees = dict(G.degree())
max_connections = max(degrees.items(), key=lambda x: x[1])
print(f"\nGrad sa najvecim brojem povezanih susjeda: {max_connections[0]} ({max_connections[1]} susjeda)")

# 3. 
podgorica_neighbors = list(G.neighbors("Podgorica"))
print(f"\nGradovi povezani sa Podgoricom: {', '.join(podgorica_neighbors)}")

# 4. 
plt.figure(figsize=(12, 8))
pos = nx.spring_layout(G, k=1, iterations=50)

# 
nx.draw_networkx_nodes(G, pos, node_color='lightblue', node_size=500)
nx.draw_networkx_labels(G, pos)

# 
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels)
nx.draw_networkx_edges(G, pos)

plt.title("Gradovi u Crnoj Gori")
plt.axis('off')
plt.show()
