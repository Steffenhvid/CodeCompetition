import sys
from pathlib import Path

import numpy as np
sys.path.append(r".\\")

from Services.Graphs import Graph
DATA = r".\Data\0107_network.txt"

matrix = []
with open(Path(DATA), "r") as f:
    for line in f.readlines():
        line = line.replace('-', '0')
        row = [int(i) for i in line.split(',')]
        matrix.append(row)


testdata =  [[ 0, 16, 12, 21,  0,  0,  0],
            [16,  0,  0, 17, 20,  0,  0],
            [12,  0,  0, 28,  0, 31,  0],
            [21, 17, 28,  0, 18, 19, 23],
            [ 0, 20,  0, 18,  0,  0, 11],
            [ 0,  0, 31, 19,  0,  0, 27],
            [ 0,  0,  0, 23, 11, 27,  0]]


import networkx as nx
import matplotlib.pyplot as plt


adjacency_matrix = np.triu(matrix)
# Create a graph from the adjacency matrix
G = nx.Graph()
num_nodes = len(adjacency_matrix)

# Add nodes to the graph
G.add_nodes_from(range(num_nodes))

# Add weighted edges to the graph based on the adjacency matrix
for i in range(num_nodes):
    for j in range(i + 1, num_nodes):
        if adjacency_matrix[i][j] != 0:
            G.add_edge(i, j, weight=adjacency_matrix[i][j])

# Define the layout for node positions
pos = nx.spring_layout(G)

# Draw the graph with edge labels showing weights
edge_labels = {(i, j): adjacency_matrix[i][j] for i, j in G.edges()}
nx.draw(G, pos, with_labels=True, node_size=500, node_color='skyblue', font_size=10, font_color='black', font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red', font_size=8, rotate=False)
plt.title("Weighted Graph from Adjacency Matrix")
plt.show()