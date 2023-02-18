# checking if a binary tree is full binary tree.

class Node:
    def __init__(self, elem) -> None:
        self.elem = elem
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f'{self.elem}'

def is_full_tree(root):
    # tree in an empty case.
    if root is None:
        return True
    
    # checking whether child is present.
    if root.left_child is None and root.right_child is None:
        return True
    
    if root.left_child is not None and root.right_child is not None:
        return (is_full_tree(root.left_child)) and is_full_tree((root.right_child))
    
    return False

root = Node(2)

root.right_child = Node(3)
root.left_child = Node(2)

root.left_child.left_child = Node(4)
root.left_child.right_child = Node(5)

print(repr(root))

root.left_child.right_child.left_child = Node(6)
root.left_child.right_child.right_child = Node(7)

if is_full_tree(root):
    print("The tree is a full binary tree")
else:
    print("The tree is not a full binary tree")