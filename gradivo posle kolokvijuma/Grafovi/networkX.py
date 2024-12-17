import networkx as nx

graph = nx.Graph()

usmjereni_graph = nx.DiGraph()

graph.add_node(1)

print(graph)


graph.add_nodes_from([1,23,4,5,6,7])
print(*graph.nodes())
graph.add_edge(4,5)
print(graph)
graph.add_edges_from([(2,3),(23,4)])
print(graph.edges())

graph[4][5]['weight'] = 7.5

graph.add_edge(1,5,weight = 5.0)

import matplotlib.pyplot as plt
nx.draw(graph, with_labels = True, node_color = "#b3ffff", edge_color = "green")
plt.savefig('graph.png')
