class Node:
    def __init__(self, key) -> None:
        self.key = key 
        self.left = None
        self.right = None

def in_order(root):
    if root is not None:
        in_order(root.left)
        print(str(root.key) + '-.', end=' ')
        in_order(root.right)

def insert(node, key):
    if node is None:
        return Node(key)
    
    if key < node.key:
        node.left = insert(node.left, key)
    else:
        node.right = insert(node.right, key)
    return node

def min_value_node(node):
    current = node

    while(current.left is not None):
        current = current.left

    return current

def delete_node(root, key):
    if root is None:
        return root
    if key < root.key:
        root.left = delete_node(root.left, key)
    elif (key > root.key):
        root.right = delete_node(root.right, key)
    else:
        if root.left is None:
            tmp = root.right
            root = None
            return tmp
        elif root.right is None:
            tmp = root.left
            root = None
            return tmp
        tmp = min_value_node(root.right)
        root.key = tmp.key
        root.right = delete_node(root.right, tmp.key)
    return root

root = None
root = insert(root, 8)
root = insert(root, 3)
root = insert(root, 1)
root = insert(root, 6)
root = insert(root, 7)
root = insert(root, 10)
root = insert(root, 14)
root = insert(root, 4)

print("Inorder traversal: ", end=' ')
in_order(root)

print("\nDelete 10")
root = delete_node(root, 10)
print("Inorder traversal: ", end=' ')
in_order(root)