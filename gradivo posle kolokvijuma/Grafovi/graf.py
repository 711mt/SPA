class Graph:
  def __init__(self, num_nodes):
    self.matrix = []
    for i in range(num_nodes):
      self.matrix.append([0 for i in range(num_nodes)])
    self.node_names = {}
    self.next_index = 0
    self.num_nodes = num_nodes

  def add_node(self, name):
    if name in self.node_names:
      print(f"Cvor {name} vec postoji u grafu.")
    else:
      if self.next_index < self.num_nodes: #ako je indeks manji od broja cvorova
        self.node_names[name] = self.next_index
        self.next_index += 1
      else:
        print("Maksimalan broj cvorova u grafu je postignut.")
  
  def add_edge_by_name(self, start_name, end_name, weight = 1):
    if start_name in self.node_names and end_name in self.node_names:
      start = self.node_names[start_name]
      end = self.node_names[end_name]
      self.matrix[start][end] = weight

  def add_edge(self, start,end):
    self.matrix[start][end]=1

  def remove_edge(self,start,end):
    self.matrix[start][end] == 0

  def is_edge(self,start,end):
    if self.matrix[start][end] != 0:
      return True
    else:
      return False

  def print_graph(self):
    matrix = self.matrix
    node_names = self.node_names
    print(*[name for name in node_names.keys()])
    for r in matrix:
      for c in r:
        print(c,end=" ")
      print("\n")

graph = Graph(5)
graph.add_edge(0,1)
graph.add_edge(2,3)
graph.add_edge(2,1)
graph.add_node("A")
graph.add_node("B")
graph.add_node("C")
graph.add_node("D")
graph.add_node("E")

graph.add_edge_by_name("C","E", 7.5)

graph.print_graph()