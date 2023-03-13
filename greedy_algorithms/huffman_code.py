# Define the NodeTree class to represent nodes in the Huffman tree
class NodeTree:
    def __init__(self, left: 'NodeTree', right: 'NodeTree') -> None:
        self.left = left
        self.right = right
    
    def children(self) -> tuple['NodeTree', 'NodeTree']:
        return (self.left, self.right)
    
    def nodes(self) -> tuple['NodeTree', 'NodeTree']:
        return (self.left, self.right)
    
    def __str__(self) -> str:
        return f"{self.left}_{self.right}"

# Define the huffman_code_tree function to generate the Huffman codes for each character in the input tree
def huffman_code_tree(nodes : NodeTree , left: bool = True, emt_string: str = '') -> dict[str, str]:
    if isinstance(nodes, str):
        return {nodes: emt_string}
    left_child, right_child = nodes.children()
    # Recursively generate the Huffman code for each child node, appending '0' for the left child and '1' for the right child
    left_code = huffman_code_tree(left_child, True, emt_string + '0')
    right_code = huffman_code_tree(right_child, False, emt_string + '1')
    # Merge the dictionaries for the left and right child nodes and return the result
    return {**left_code, **right_code}

# Define the input string and create a frequency dictionary for each character in the string
input_string = 'BDABCADIACADKA'
freq: dict[str, int] = {}
for c in input_string:
    freq[c] = freq.get(c, 0) + 1
    
# Sort the frequency dictionary in decreasing order of frequency
freq_sorted: list[tuple[str, int]] = sorted(freq.items(), key=lambda x: x[1], reverse=True)

# Create a list of nodes for each character in the frequency dictionary
nodes: list[tuple['NodeTree', int]] = [(key, count) for key, count in freq_sorted]

# Merge the nodes until a single tree is formed
while len(nodes) > 1:
    # Get the two nodes with the lowest frequency and remove them from the list
    key1, count1 = nodes.pop()
    key2, count2 = nodes.pop()
    # Create a new node with the two nodes as children and add it to the list of nodes
    new_node = NodeTree(key1, key2)
    nodes.append((new_node, count1 + count2))
    # Sort the list of nodes in decreasing order of frequency
    nodes.sort(key=lambda x: x[1], reverse=True)

# Generate the Huffman code for each character in the original frequency dictionary using the Huffman tree
huffman_codes = huffman_code_tree(nodes[0][0])

# Print the Huffman code for each character in the original frequency dictionary
print(' Char | Huffman code ')
print('----------------------')
for char, frequency in freq_sorted:
    code = huffman_codes[char]
    print(f" {char:<4} | {code:>12}")


