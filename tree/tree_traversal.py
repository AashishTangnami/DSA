# Tree traversal in Python

class Node:
    def __init__(self, item):
        self.left = None
        self.right = None
        self.val = item


def in_order(root):

    if root:
        # Traverse left
        in_order(root.left)
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse right
        in_order(root.right)


def post_order(root):

    if root:
        # Traverse left
        post_order(root.left)
        # Traverse right
        post_order(root.right)
        # Traverse root
        print(str(root.val) + "->", end='')


def pre_order(root):

    if root:
        # Traverse root
        print(str(root.val) + "->", end='')
        # Traverse left
        pre_order(root.left)
        # Traverse right
        pre_order(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("in_order traversal ")
in_order(root)

print("\npre_order traversal ")
pre_order(root)

print("\npost_order traversal ")
post_order(root)