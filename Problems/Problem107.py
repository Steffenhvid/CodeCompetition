import sys
sys.path.append(r".\\")

from pathlib import Path
from Services.Graphs.Graph import Graph
from Services.Graphs.Kruskal import Kruskal
import networkx as nx
import matplotlib.pyplot as plt

DATA = r".\Data\0107_network.txt"

matrix = []
with open(Path(DATA), "r") as f:
    for line in f.readlines():
        line = line.replace('-', '0')
        row = [int(i) for i in line.split(',')]
        matrix.append(row)

Gr = Graph(len(matrix))
Gr.add_edges_from_adj_matrix(matrix)

krustal = Kruskal(Gr)

result = krustal.execute_alorithm()

oldweight = Gr.get_weight_of_graph() / 2
newweight = result.get_weight_of_graph()

print(f"The original of the graph: {oldweight}")
print(f"Weight of the new graph: {newweight}")
print(f"Saving: {oldweight - newweight}")

G = nx.Graph()
G.add_nodes_from(result.V)
G.add_weighted_edges_from(result.E)

pos = nx.planar_layout(G)  # You can choose different layout algorithms
labels = nx.get_edge_attributes(G, 'weight')
nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

# Display the graph
plt.show()