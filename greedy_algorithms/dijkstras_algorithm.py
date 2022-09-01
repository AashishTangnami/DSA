
# Dijkstra's Algorithm allows us to find,
# the shortest path between any two vertices of a graph.

# Shortest path might not include all the vertices of a graph.

# Pseudocode.
    # function dijkstra(g, s)
        #for each vertex V in graph
            # distance[V] <- infinite
            # previous[V] <- Null
            # if V != S, add V to priority Queue Q
        # distance[S] < 0
    # While Q is not empty
        # U <- Extract MIN from Q
        # for each unvisited neighbor V of U 
            # temp_distance <- distance[U] + edge_weight(U, V)
            # if temp_distance < distance[V]
                # distance[V] <- temp_distance
                # previous[V] <- U
    # return distance[], previous[]

import sys

vertices = [[0, 0, 1, 1, 0, 0, 0],
            [0, 0, 1, 0, 0, 1, 0],
            [1, 1, 0, 1, 1, 0, 0],
            [1, 0, 1, 0, 0, 0, 1],
            [0, 0, 1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1, 0, 1],
            [0, 0, 0, 1, 0, 1, 0]]
            
edges = [[0, 0, 1, 2, 0, 0, 0],
         [0, 0, 2, 0, 0, 3, 0],
         [1, 2, 0, 1, 3, 0, 0],
         [2, 0, 1, 0, 0, 0, 1],
         [0, 0, 3, 0, 0, 2, 0],
         [0, 3, 0, 0, 2, 0, 1],
         [0, 0, 0, 1, 0, 1, 0]]
num_of_vertices = len(vertices[0])
def to_be_visited():
    global visited_and_distance
    v = - 10
    for index in range(num_of_vertices):
        if visited_and_distance[index][0] == 0 \
            and (v < 0 or visited_and_distance[index][1] <= \
                visited_and_distance[v][1]):
            v = index
    return v

visited_and_distance = [[0,0]]

for i in range(num_of_vertices-1):
    visited_and_distance.append([0, sys.maxsize])

for vertex in range(num_of_vertices):
    to_visit = to_be_visited()
    
    for neighbour_index in range(num_of_vertices):
        if vertices[to_visit][neighbour_index] == 1 and \
            visited_and_distance[neighbour_index][0] == 0:
            new_distance = visited_and_distance[to_visit][1] + edges[to_visit][neighbour_index]
            if visited_and_distance[neighbour_index][1] > new_distance:
                visited_and_distance[neighbour_index][1] = new_distance

        visited_and_distance[to_visit][0] = 1
i = 0

for distance in visited_and_distance:
    print("Distance of ", chr(ord('a') + i),
          " from source vertex: ", distance[1])
    i = i + 1