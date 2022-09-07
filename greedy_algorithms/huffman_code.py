# Technique of compressing data to reduce its size without losing any of the detail information is called Huffman coding.
# If there is frequent occurance of characters then Huffman coding is used to compress the data.

# Huffman coding first creates a tree using the frequencies of the character and then generates code for each character.
# Encoding the characters in one tree then decoding is also done using same tree.

# Pseudocode.
    # 1. Calculate the frequency of each character in the string.
    # 2. Sort the characters in increasing order of the frequency.
    # - Characters are stored in a priority queue Q.
    # 3. Make each unique character as a leaf node.
    # 4. Create and empty node (Z).
        # - Assign the minimum frequency to the left child of z and assign the second minimum frequency to the right child of Z.
        # - Set the value of the Z as the sum of the above two minimum frequencies.
    # 5. Remove these two minimum frequencies from Q and add the sum into the list of frequencies
    # 6. Insert node Z to the tree.
    # 7. Repeat steps 3 to 5 for all the characters.
    # 8. For each non-leaf node, assign 0 to the left edge and 1 to the right edge.


string = 'BDABCADIACADKA'
class NodeTree(object):
    def __init__(self, left = None, right = None):
        self.left = left
        self.right = right
    
    def children(self):
        return (self.left, self.right)
    
    def nodes(self):
        return (self.left, self.right)
    
    def __str__(self) -> str:
        return '%s_%s' % (self.left, self.right)

def huffman_code_tree(nodes, left = True, emt_string=''):
    if type(nodes) is str:
        return {nodes: emt_string}
    (l, r) = nodes.children()
    tmp_dict = dict()
    tmp_dict.update(huffman_code_tree(l, True, emt_string + '0'))
    tmp_dict.update(huffman_code_tree(r, False, emt_string + '1'))
    return tmp_dict

freq = {}
for c in string:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1
    
freq = sorted(freq.items(), key = lambda x:x[1], reverse= True)
nodes = freq

while len(nodes) > 1:
    (key1, c1) = nodes[-1]
    (key2, c2) = nodes[-2]
    nodes = nodes[:-2]
    node = NodeTree(key1, key2)
    nodes.append((node, c1 + c2))

    nodes = sorted(nodes, key=lambda x: x[1], reverse=True)

huffman_code_tree = huffman_code_tree(nodes[0][0])
print(' Char | Huffman code ')
print('----------------------')
for (char, frequency) in freq:
    print(' %-4r |%12s' % (char, huffman_code_tree[char]))



