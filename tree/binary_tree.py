class Node:
    def __init__(self, key) -> None:
        self.left = None
        self.right = None
        self.val = key

    def traverse_pre_order(self):
        print(self.val, end= ' ')
        if self.left:
            self.left.traverse_pre_order()
        if self.right:
            self.right.traverse_pre_order()

    def traverse_in_order(self):
        if self.left:
            self.left.traverse_in_order()
        print(self.val, end=' ')
        if self.right:
            self.traverse_in_order()

    def traverse_post_order(self):
        if self.left:
            self.left.traverse_post_order()
        if self.right:
            self.right.traverse_post_order()
        print(self.val, end='')

root = Node(1)

root.left = Node(2)
root.right = Node(3)

root.left.left = Node(4)
root.left.right = Node(4)
print("Pre order Traversal: ", end="")
root.traverse_pre_order()
print("\nIn order Traversal: ", end="")
root.traverse_in_order()
print("\nPost order Traversal: ", end="")
root.traverse_post_order()