# Kosarajus Algorithm based on the depth-first search algorithm

# Perform a depth first search on the whole graph.
# start from vertrex-0
    # visit all child vertices.
    # mark the visited vertices.
    # if a vertex leads to an already visited vertex then push it to the stack
    # if all vertices are visited and if a vertice after that has nowhere to got then push it to the stack.
    # then add the previous elements after last to the stack which are all vistied.
# reverse the original graph.
# Perfrom the depth-first serach on the reversed graph.

from collections import defaultdict 

class Graph:
    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)
    
    def add_edge(self, s, d):
        self.graph[s].append(d)
    
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)
    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)
    
    # transpose the matrix.
    def transpose(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g
    
    # print strongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)
        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        gr = self.transpose()
        visited_vertex = [False] * (self.V)
        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print(" ")

g = Graph(8)
g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(2, 4)
g.add_edge(3, 0)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 4)
g.add_edge(6, 7)

print("Strongly Connected Components:")
g.print_scc()