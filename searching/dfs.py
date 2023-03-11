def dfs(graph: dict[str, set[str]], start: str, visited: set[str] = None) -> set[str]:
    """
    Depth First Search (DFS) function to traverse a graph

    Args:
        graph (dict): The graph to be traversed
        start (str): The starting node for the traversal
        visited (set): A set to keep track of visited nodes (default is None)

    Returns:
        visited (set): A set of visited nodes
    """
    # Create a set to keep track of visited nodes
    if visited is None:
        visited = set()
    # Add the current node to the visited set
    visited.add(start)

    # Print the current node
    print(start)

    # Recursively call the DFS function on unvisited neighbors of the current node
    for next_node in graph[start] - visited :
        dfs(graph, next_node, visited)
    return visited

# Define a graph as a dictionary
graph = {'0': set(['1', '2']),
         '1': set(['0', '3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}

# Call the DFS function with starting node '0'
dfs(graph, '0')
