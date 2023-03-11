from typing import Optional

class Node:
    def __init__(self, val: int) -> None:
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self) -> None:
        self.head: Optional[Node] = None
    
    # insert at the beginning
    # Time complexity: O(1)
    def insert_at_begining(self, new_val: int) -> None:
        new_node = Node(new_val)

        new_node.next = self.head
        self.head = new_node

    # insert after a node
    # Time complexity: O(1) if prev_node is given, O(n) otherwise
    def insert_after(self, prev_node: Node, new_val: int) -> None:
        if prev_node is None:
            return
        
        new_node = Node(new_val)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # insert at the end.
    # Time complexity: O(n)
    def insert_at_end(self, new_val: int) -> None:
        new_node = Node(new_val)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    # delete a node
    # Time complexity: O(n)
    def delete_node(self, idx: int) -> None:
        if self.head is None:
            return
        tmp_head = self.head

        if idx == 0:
            self.head = tmp_head.next
            tmp_head = None
            return
        
        # find the key to be deleted.
        for _ in range(idx - 1):
            tmp_head = tmp_head.next
            if tmp_head is None:
                break
        
        if tmp_head is None:
            return
        if tmp_head.next is None:
            return
        
        next = tmp_head.next.next
        tmp_head.next = None
        tmp_head.next = next
    
    # search for a node with the given key
    # Time complexity: O(n)
    def search(self, key: int) -> bool:
        current = self.head
        while current is not None:
            if current.val == key:
                return True
            current = current.next
        return False
    
    # sort the linked list in ascending order
    # Time complexity: O(n^2)
    def sort_linked_list(self, head: Optional[Node]) -> None:
        current = head
        index = Node(None)
        if head is None:
            return
        else:
            while current is not None:
                index = current.next
                while index is not None:
                    if current.val > index.val:
                        current.val, index.val = index.val, current.val
                    index = index.next
                current = current.next
    
    # print the linked list
    def print_list(self) -> None:
        tmp = self.head
        while(tmp):
            print(str(tmp.val) + " ", end="")
            tmp = tmp.next

if __name__ == '__main__':
    llist = LinkedList()
    llist.insert_at_end(1)
    llist.insert_at_begining(2)
    llist.insert_at_begining(3)
    llist.insert_at_end(4)
    llist.insert_after(llist.head.next, 5)

    print('linked list:')
    llist.print_list()

    print("\nAfter deleting an element:")
    llist.delete_node(3)
    llist.print_list()

    print()
    item_to_find = 3
