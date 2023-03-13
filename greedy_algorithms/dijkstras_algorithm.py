import sys

# Define vertices and edges as lists of lists containing integers
vertices: list[list[int]] = [[0, 0, 1, 1, 0, 0, 0],
                             [0, 0, 1, 0, 0, 1, 0],
                             [1, 1, 0, 1, 1, 0, 0],
                             [1, 0, 1, 0, 0, 0, 1],
                             [0, 0, 1, 0, 0, 1, 0],
                             [0, 1, 0, 0, 1, 0, 1],
                             [0, 0, 0, 1, 0, 1, 0]]
edges: list[list[int]] = [[0, 0, 1, 2, 0, 0, 0],
                          [0, 0, 2, 0, 0, 3, 0],
                          [1, 2, 0, 1, 3, 0, 0],
                          [2, 0, 1, 0, 0, 0, 1],
                          [0, 0, 3, 0, 0, 2, 0],
                          [0, 3, 0, 0, 2, 0, 1],
                          [0, 0, 0, 1, 0, 1, 0]]

num_of_vertices: int = len(vertices[0])

def to_be_visited() -> int:
    """Returns the index of the vertex with the smallest tentative distance."""
    global visited_and_distance  # declare global variable
    v: int = -10  # initialize v to a negative value
    for index in range(num_of_vertices):  # iterate over all vertices
        if visited_and_distance[index][0] == 0 and (v < 0 or visited_and_distance[index][1] <= visited_and_distance[v][1]):
            # if the vertex has not been visited and it has the smallest tentative distance so far
            v = index  # update the index of the vertex with the smallest tentative distance
    return v  # return the index of the vertex with the smallest tentative distance


# Initialize visited_and_distance as a list of lists containing 2 integers each
visited_and_distance: list[list[int]] = [[0, 0]]
for i in range(num_of_vertices - 1):
    visited_and_distance.append([0, sys.maxsize])

# Apply Dijkstra's algorithm
for vertex in range(num_of_vertices):
    to_visit: int = to_be_visited()  # Get the vertex with the smallest tentative distance
    for neighbour_index in range(num_of_vertices):
        # If the vertex is adjacent and not visited
        if vertices[to_visit][neighbour_index] == 1 and visited_and_distance[neighbour_index][0] == 0:
            # Calculate the new tentative distance
            new_distance: int = visited_and_distance[to_visit][1] + edges[to_visit][neighbour_index]
            # If the new tentative distance is smaller, update the distance
            if visited_and_distance[neighbour_index][1] > new_distance:
                visited_and_distance[neighbour_index][1] = new_distance
        # Mark the current vertex as visited
        visited_and_distance[to_visit][0] = 1

# Print the distances
i: int = 0
for distance in visited_and_distance:
    print(f"Distance of {chr(ord('a') + i)} from source vertex: {distance[1]}")
    i = i + 1
