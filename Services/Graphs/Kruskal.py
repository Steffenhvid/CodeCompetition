from importlib.metadata import SelectableGroups
from Services.Graphs.Graph import Graph

class Kruskal:
    '''
    Algorithm for finding a minimum spanning tree.
    '''
    def __init__(self, graph:Graph):
        self.graph = graph
        self.result = Graph(graph.NodeCount)
        self.parent = {}  
        self.rank = {} 
        for v in self.result.V:  
            self.make_set(v)  

    def sort_edges_by_weight(self):
        self.graph.E.sort(key=lambda e: e[2])

    def make_set(self, v):  
        self.parent[v] = v  
        self.rank[v] = 0  
  
    def find(self, v):  
        if self.parent[v] != v:  
            self.parent[v] = self.find(self.parent[v])  
        return self.parent[v]  
  
    def union(self, u, v):  
        root1 = self.find(u)  
        root2 = self.find(v)  
  
        if root1 != root2:  
            if self.rank[root1] > self.rank[root2]:  
                self.parent[root2] = root1  
            else:  
                self.parent[root1] = root2  
                if self.rank[root1] == self.rank[root2]:  
                    self.rank[root2] += 1  
        
    
    def execute_alorithm(self) -> Graph:
        self.sort_edges_by_weight()
  
        # Sort edges by weight using priorit
        for e in self.graph.E:
            if self.find(e[0]) != self.find(e[1]):  
                self.union(e[0], e[1])  
                self.result.add_edge(e) 
            if len(self.result.E) == self.result.NodeCount - 1:
                break
        
        return self.result
            
        



