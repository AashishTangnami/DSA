# checking if a binary tree is a perfect binary tree.

class Node:
    def __init__(self, ele) -> None:
        self.key = ele
        self.right = self.left = None

# calculate the depth of the tree.
def calc_depth_tree(node):
    depth = 0
    while (node is not None):
        depth +=1 
        node = node.left
    return depth

def is_tree_perfect(root, depth, level=0):
    #check if the tree is empty
    if (root is None):
        return True
    # check the presence of trees
    if (root.left is None and root.right is None):
        return(depth == level + 1)

    if (root.left is None or root.right is None):
        return False
    
    return (is_tree_perfect(root.left, depth, level+1) and is_tree_perfect(root.right, depth,  level+1))


root = None
root = Node(1)
root.left = Node(2)

root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)

root.right.left = Node(7)
# root.right.right = Node(5)

#uncomment to see the perfect binary

if (is_tree_perfect(root, calc_depth_tree(root))):
    print("The tree is a perfect binary tree")
else:
    print("The tree is not a perfect binary tree")