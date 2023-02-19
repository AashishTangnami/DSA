class Node:
    def __init__(self, item):
        self.item =item
        self.left = None
        self.right = None

def count_nodes(root):
    if root is None:
        return 0
    return (1+ count_nodes(root.left) + count_nodes(root.right))

def is_complete_tree(root, idx, num_root):
    if root is None:
        return True
    if idx >= num_root:
        return False
    return (is_complete_tree(root.left, 2  * idx + 1, num_root)
            and is_complete_tree(root.right, 2 * idx + 2, num_root))



root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)

node_count = count_nodes(root)
idx = 0

if is_complete_tree(root, idx, node_count):
    print("The tree is a complete binary tree")
else:
    print("The tree is not a complete binary tree")