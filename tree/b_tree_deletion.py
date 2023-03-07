# B+ tee in python


import math

# Node creation
class Node:
    def __init__(self, order):
        self.order = order
        self.values = []
        self.keys = []
        self.next_key = None
        self.parent = None
        self.check_leaf = False

    # Insert at the leaf
    def insert_at_leaf(self, leaf, value, key):
        if (self.values):
            temp1 = self.values
            for i in range(len(temp1)):
                if (value == temp1[i]):
                    self.keys[i].append(key)
                    break
                elif (value < temp1[i]):
                    self.values = self.values[:i] + [value] + self.values[i:]
                    self.keys = self.keys[:i] + [[key]] + self.keys[i:]
                    break
                elif (i + 1 == len(temp1)):
                    self.values.append(value)
                    self.keys.append([key])
                    break
        else:
            self.values = [value]
            self.keys = [[key]]


# B plus tree
class b_plus_tree:
    def __init__(self, order):
        self.root = Node(order)
        self.root.check_leaf = True

    # Insert operation
    def insert(self, value, key):
        value = str(value)
        old_node = self.search(value)
        old_node.insert_at_leaf(old_node, value, key)

        if (len(old_node.values) == old_node.order):
            node1 = Node(old_node.order)
            node1.check_leaf = True
            node1.parent = old_node.parent
            mid = int(math.ceil(old_node.order / 2)) - 1
            node1.values = old_node.values[mid + 1:]
            node1.keys = old_node.keys[mid + 1:]
            node1.next_key = old_node.next_key
            old_node.values = old_node.values[:mid + 1]
            old_node.keys = old_node.keys[:mid + 1]
            old_node.next_key = node1
            self.insert_in_parent(old_node, node1.values[0], node1)

    # Search operation for different operations
    def search(self, value):
        current_node = self.root
        while(current_node.check_leaf == False):
            temp2 = current_node.values
            for i in range(len(temp2)):
                if (value == temp2[i]):
                    current_node = current_node.keys[i + 1]
                    break
                elif (value < temp2[i]):
                    current_node = current_node.keys[i]
                    break
                elif (i + 1 == len(current_node.values)):
                    current_node = current_node.keys[i + 1]
                    break
        return current_node

    # Find the node
    def find(self, value, key):
        l = self.search(value)
        for i, item in enumerate(l.values):
            if item == value:
                if key in l.keys[i]:
                    return True
                else:
                    return False
        return False

    # Inserting at the parent
    def insert_in_parent(self, n, value, n_dash):
        if (self.root == n):
            root_node = Node(n.order)
            root_node.values = [value]
            root_node.keys = [n, n_dash]
            self.root = root_node
            n.parent = root_node
            n_dash.parent = root_node
            return

        parent_node = n.parent
        temp3 = parent_node.keys
        for i in range(len(temp3)):
            if (temp3[i] == n):
                parent_node.values = parent_node.values[:i] + \
                    [value] + parent_node.values[i:]
                parent_node.keys = parent_node.keys[:i +
                                                  1] + [n_dash] + parent_node.keys[i + 1:]
                if (len(parent_node.keys) > parent_node.order):
                    parent_dash = Node(parent_node.order)
                    parent_dash.parent = parent_node.parent
                    mid = int(math.ceil(parent_node.order / 2)) - 1
                    parent_dash.values = parent_node.values[mid + 1:]
                    parent_dash.keys = parent_node.keys[mid + 1:]
                    value_ = parent_node.values[mid]
                    if (mid == 0):
                        parent_node.values = parent_node.values[:mid + 1]
                    else:
                        parent_node.values = parent_node.values[:mid]
                    parent_node.keys = parent_node.keys[:mid + 1]
                    for j in parent_node.keys:
                        j.parent = parent_node
                    for j in parent_dash.keys:
                        j.parent = parent_dash
                    self.insert_in_parent(parent_node, value_, parent_dash)

    # Delete a node
    def delete(self, value, key):
        node_ = self.search(value)

        temp = 0
        for i, item in enumerate(node_.values):
            if item == value:
                temp = 1

                if key in node_.keys[i]:
                    if len(node_.keys[i]) > 1:
                        node_.keys[i].pop(node_.keys[i].index(key))
                    elif node_ == self.root:
                        node_.values.pop(i)
                        node_.keys.pop(i)
                    else:
                        node_.keys[i].pop(node_.keys[i].index(key))
                        del node_.keys[i]
                        node_.values.pop(node_.values.index(value))
                        self.delete_entry(node_, value, key)
                else:
                    print("Value not in Key")
                    return
        if temp == 0:
            print("Value not in Tree")
            return

    # Delete an entry
    def delete_entry(self, node_, value, key):

        if not node_.check_leaf:
            for i, item in enumerate(node_.keys):
                if item == key:
                    node_.keys.pop(i)
                    break
            for i, item in enumerate(node_.values):
                if item == value:
                    node_.values.pop(i)
                    break

        if self.root == node_ and len(node_.keys) == 1:
            self.root = node_.keys[0]
            node_.keys[0].parent = None
            del node_
            return
        elif (len(node_.keys) < int(math.ceil(node_.order / 2)) \
              and node_.check_leaf == False) \
                or (len(node_.values) < int(math.ceil((node_.order - 1) / 2)) \
                    and node_.check_leaf == True):

            is_predecessor = 0
            parent_node = node_.parent
            prev_node = -1
            next_node = -1
            prev_K = -1
            post_K = -1
            for i, item in enumerate(parent_node.keys):

                if item == node_:
                    if i > 0:
                        prev_node = parent_node.keys[i - 1]
                        prev_K = parent_node.values[i - 1]

                    if i < len(parent_node.keys) - 1:
                        next_node = parent_node.keys[i + 1]
                        post_K = parent_node.values[i]

            if prev_node == -1:
                n_dash = next_node
                value_ = post_K
            elif next_node == -1:
                is_predecessor = 1
                n_dash = prev_node
                value_ = prev_K
            else:
                if len(node_.values) + len(next_node.values) < node_.order:
                    n_dash = next_node
                    value_ = post_K
                else:
                    is_predecessor = 1
                    n_dash = prev_node
                    value_ = prev_K

            if len(node_.values) + len(n_dash.values) < node_.order:
                if is_predecessor == 0:
                    node_, n_dash = n_dash, node_
                n_dash.keys += node_.keys
                if not node_.check_leaf:
                    n_dash.values.append(value_)
                else:
                    n_dash.next_key = node_.next_key
                n_dash.values += node_.values

                if not n_dash.check_leaf:
                    for j in n_dash.keys:
                        j.parent = n_dash

                self.delete_entry(node_.parent, value_, node_)
                del node_
            else:
                if is_predecessor == 1:
                    if not node_.check_leaf:
                        n_dash_pm = n_dash.keys.pop(-1)
                        n_dash_km_1 = n_dash.values.pop(-1)
                        node_.keys = [n_dash_pm] + node_.keys
                        node_.values = [value_] + node_.values
                        parent_node = node_.parent
                        for i, item in enumerate(parent_node.values):
                            if item == value_:
                                p.values[i] = n_dash_km_1
                                break
                    else:
                        n_dash_pm = n_dash.keys.pop(-1)
                        n_dash_km = n_dash.values.pop(-1)
                        node_.keys = [n_dash_pm] + node_.keys
                        node_.values = [n_dash_km] + node_.values
                        parent_node = node_.parent
                        for i, item in enumerate(p.values):
                            if item == value_:
                                parent_node.values[i] = n_dash_km
                                break
                else:
                    if not node_.check_leaf:
                        n_dash_p_0 = n_dash.keys.pop(0)
                        n_dash_k_0 = n_dash.values.pop(0)
                        node_.keys = node_.keys + [n_dash_p_0]
                        node_.values = node_.values + [value_]
                        parent_node = node_.parent
                        for i, item in enumerate(parent_node.values):
                            if item == value_:
                                parent_node.values[i] = n_dash_k_0
                                break
                    else:
                        n_dash_p_0 = n_dash.keys.pop(0)
                        n_dash_k_0 = n_dash.values.pop(0)
                        node_.keys = node_.keys + [n_dash_p_0]
                        node_.values = node_.values + [n_dash_k_0]
                        parent_node = node_.parent
                        for i, item in enumerate(parent_node.values):
                            if item == value_:
                                parent_node.values[i] = n_dash.values[0]
                                break

                if not n_dash.check_leaf:
                    for j in n_dash.keys:
                        j.parent = n_dash
                if not node_.check_leaf:
                    for j in node_.keys:
                        j.parent = node_
                if not parent_node.check_leaf:
                    for j in parent_node.keys:
                        j.parent = parent_node


# Print the tree
def print_tree(tree):
    lst = [tree.root]
    level = [0]
    leaf = None
    flag = 0
    lev_leaf = 0

    node1 = Node(str(level[0]) + str(tree.root.values))

    while (len(lst) != 0):
        x = lst.pop(0)
        lev = level.pop(0)
        if (x.check_leaf == False):
            for i, item in enumerate(x.keys):
                print(item.values)
        else:
            for i, item in enumerate(x.keys):
                print(item.values)
            if (flag == 0):
                lev_leaf = lev
                leaf = x
                flag = 1


record_len = 3
b_plus_tree = b_plus_tree(record_len)
b_plus_tree.insert('5', '33')
b_plus_tree.insert('15', '21')
b_plus_tree.insert('25', '31')
b_plus_tree.insert('35', '41')
b_plus_tree.insert('45', '10')

print_tree(b_plus_tree)

if(b_plus_tree.find('5', '31')):
    print("Found")
else:
    print("Not found")