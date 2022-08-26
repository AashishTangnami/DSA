from hashlib import new


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    # insert at the begining
    def insert_at_begining(self, new_val):
        new_node = Node(new_val)

        new_node.next = self.head
        self.head = new_node

    # insert after a node
    def insert_after(self, prev_node, new_val):
        if prev_node is None:
            return 'No value'
        
        new_node = Node(new_val)
        new_node.next = prev_node.next
        prev_node.next = new_node

    # insert at the end.
    def insert_at_end(self, new_val):
        new_node = Node(new_val)
        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while(last.next):
            last = last.next
        last.next = new_node

    # delete a node
    def delete_node(self, idx):
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
        # 
        if tmp_head is None:
            return
        if tmp_head.next is None:
            return
        
        next = tmp_head.next.next
        tmp_head.next = None
        tmp_head.next = next
    
    def search(self, key):
        current = self.head
        while current is not None:
            if current.val == key:
                return True
            current = current.next
        return False
    
    def sort_linked_list(self, head):
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
    
    def print_list(self):
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
    if llist.search(item_to_find):
        print(str(item_to_find) + " is found")
    else:
        print(str(item_to_find) + " is not found")

    llist.sort_linked_list(llist.head)
    print("Sorted List: ")
    llist.print_list() 
