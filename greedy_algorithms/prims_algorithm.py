# Prim's Algorithm
# It finds the local optimum in the hopes of finding a global optimum.
# Start from one vertex and keep adding edges with the lowest weight until we reach our goal.

# Pseudocode
# Initialize the minimum spanning tree with a vertex chosen at random
# find all the edges that connect the tree to new vertices find the minumum and add it to the tree.
# keep repeating step 2 until we get a minimum spanning tree.

no_edge = 0 # initial val
V =  5 # number of vertices 
inf = 99999999 

selected = [0, 0, 0, 0, 0]
# the number of egde in minimum spanning tree will be
# always less than(V - 1), where V is number of vertices in
# graph
# choose 0th vertex and make it true
selected[0] = True
# print for edge and weight
print("Edge : Weight\n")

# 2d array - matrix of 5X5
# for adjacent matrix to represent graph

G = [[0, 9, 75, 0, 0],
     [9, 0, 95, 19, 42],
     [75, 95, 0, 51, 66],
     [0, 19, 51, 0, 31],
     [0, 42, 66, 31, 0]]

while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices
    #, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise
    # choose another vertex nearest to selected vertex  at step 1.
    minimum = inf
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]):
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(f'{str(x)} - {str(y)} : {str(G[x][y])}')
    selected[y] = True
    no_edge += 1


