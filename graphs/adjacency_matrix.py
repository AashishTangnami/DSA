# Adjacency matrix - Representing a graph as a matrix of booleans(0's and 1's)

class Graph(object):

    def __init__(self, size):
        self.adj_matrix = []

        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.size = size

    def add_edge(self, v1, v2):
        if v1 == v2:
            print(f"Same vertex {v1} and {v2} ")
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1
    
    def remove_edge(self, v1, v2):
        if self.adj_matrix[v1][v2] == 0:
            print(f"Same vertex {v1} and {v2} ")
            return
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def __len__(self):
        return self.size
    
    def print_matrix(self):
        for row in self.adj_matrix:
            for val in row:
                print(f'{round(val, 4)}')
            print()

def main():
    g = Graph(5)
    g.add_edge(0,1)
    g.add_edge(0,2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)

    g.print_matrix()

if __name__ == '__main__':
    main()

