import collections

def bfs_with_collection(graph: dict[int, list[int]], root: int) -> None:
    """
    Performs Breadth First Search (BFS) on a given graph starting from the root node and prints the order of visited nodes.
    Uses collections.deque to implement the queue.

    Args:
    - graph: A dictionary representing the graph in adjacency list format.
    - root: The starting node for BFS.
    """

    visited, queue = set(), collections.deque([root]) # initialize the visited set and the queue with the root node
    visited.add(root) # add the root node to the visited set

    while queue: # while the queue is not empty
        vertex = queue.popleft() # remove the first node from the queue and mark it as visited
        print(f'{str(vertex)}')

        for neighbour in graph[vertex]: # for each neighbor of the current node
            if neighbour not in visited: # if the neighbor is not already visited
                visited.add(neighbour) # mark it as visited
                queue.append(neighbour) # add it to the queue for processing later to ensure its visited only once

     
def bfs(graph: dict[int, list[int]], root: int) -> None:
    """
    Performs breadth-first search on the given graph starting from the root node and prints the traversal order.
    """
    visited = set() # create an empty set to keep track of visited nodes
    queue = [root] # create a queue and add the root node to it
    visited.add(root) # mark the root node as visited

    while queue: # loop until the queue is empty
        vertex = queue.pop(0) # remove the first node from the queue and process it
        print(f'{str(vertex)}') # print the node

        for neighbour in graph[vertex]: # loop through the neighbours of the current node
            if neighbour not in visited: # if the neighbour has not been visited yet
                visited.add(neighbour) # mark the neighbour as visited
                queue.append(neighbour) # # add it to the queue for processing later to ensure its visited only once
                
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: [3], 3: [1, 2]}
    print("Following is Breadth First Traversal using collection module: ")
    bfs_with_collection(graph, 0)
    print("Following is Breadth First Traversal")
    bfs(graph, 0)
