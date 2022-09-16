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
selected = []
G = []
while (no_edge < V - 1):
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

