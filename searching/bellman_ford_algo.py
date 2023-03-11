# Bellman Ford Algorithm in Python


class Graph:
    """
    A class to represent a weighted graph with V vertices.
    """

    def __init__(self, vertices: int) -> None:
        """
        Initializes the Graph class.

        Args:
        - vertices (int): Total number of vertices in the graph.
        """
        self.V = vertices
        self.graph: list[list[int]] = []

    def add_edge(self, s: int, d: int, w: int) -> None:
        """
        Adds an edge to the graph.

        Args:
        - s (int): Source vertex.
        - d (int): Destination vertex.
        - w (int): Weight of the edge.
        """
        self.graph.append([s, d, w])

    def print_solution(self, dist: list[int]) -> None:
        """
        Prints the distance of each vertex from the source vertex.

        Args:
        - dist (List[int]): List of distances from the source vertex to each vertex.
        """
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))

    def bellman_ford(self, src: int) -> None:
        """
        Finds the shortest distance from the source vertex to all other vertices using the Bellman-Ford algorithm.

        Args:
        - src (int): Source vertex.

        Returns:
        - None
        """
        # Step 1: Fill the distance array and predecessor array
        dist: list[int] = [float("Inf")] * self.V
        # Mark the source vertex
        dist[src] = 0

        # Step 2: Relax edges V-1 times
        for i in range(self.V - 1):
            # Keep track of whether any distance was updated or not
            changed: bool = False
            for s, d, w in self.graph:
                # If we have found a shorter path to destination vertex
                # via current source vertex, update the distance
                if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                    dist[d] = dist[s] + w
                    changed = True
            # If no distance was updated in the previous iteration,
            # we can stop early as we have already found the shortest path
            if not changed:
                break

        # Step 3: Detect negative cycle
        for s, d, w in self.graph:
            if dist[s] != float("Inf") and dist[s] + w < dist[d]:
                print("Graph contains negative weight cycle")
                return

        # No negative weight cycle found!
        # Print the distance and predecessor array
        self.print_solution(dist)


g = Graph(5)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)

g.bellman_ford(0)