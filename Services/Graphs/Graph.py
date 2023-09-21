
class Graph:
    def __init__(self, number_of_nodes:int):
        self.NodeCount = number_of_nodes
        self.V = range(number_of_nodes)
        self.E = []
        self.Adj_Matrix = [[]]
        self.Adj_List = {k : [] for k in range(self.NodeCount + 1)}

    def add_edge(self, e:tuple()):
        self.E.append(e)
        self.Adj_List[e[0]].append(e[1])

    def remove_edge(self, e:tuple()):
        self.E.remove(e)
        self.Adj_Matrix[e[0]][e[1]] = 0
        self.Adj_List[e[0]].remove(e[1])

    def add_edges_from_adj_matrix(self, adj_matrix:[[]]):
        self.Adj_Matrix = adj_matrix
        self.E = []
        self.Adj_List = {k : [] for k in range(self.NodeCount + 1)}
        for v in range(self.NodeCount):
            for u in range(self.NodeCount):
                if adj_matrix[v][u] > 0:
                    self.add_edge((v, u, adj_matrix[v][u]))

    def get_weight_of_graph(self):
        return sum([e[2] for e in self.E])