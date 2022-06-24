class Node:
    def __init__(self, data, nxt=None):
        self.data = data
        self.nxt = nxt

    def __str__(self):
        return f"[{self.data}]"

    def add_to_end(self, data):
        n = self  # n = root
        while not n.is_last():
            n = n.nxt  # n == Node(30)

        n.nxt = Node(data)

    def is_last(self):
        if self.nxt is None:
            return True
        else:
            return False


class LinkedList:
    root: Node

    def __init__(self, data, _root=None):
        if not _root:
            self.root = Node(data)

    def add_to_end(self, data):
        self.root.add_to_end(data)

    def add_to_beginning(self, data):
        new_node = Node(data)
        second_node = self.root
        self.root = new_node
        new_node.nxt = second_node

    def add_to_index(self, index, data):
        new_node = Node(data)
        n = self.root
        for i in range(index - 1):
            n = n.nxt  # [5]
        old_next = n.nxt  # [10]
        n.nxt = new_node  # [5] -> [7]
        new_node.nxt = old_next  # [7] -> [10]

    def get_at_index(self, index):

        n = self.root
        for i in range(index):
            n = n.nxt
        return n.data

    def __str__(self):
        linked_arr = []
        n = self.root
        while not n.is_last():
            linked_arr.append(str(n))
            n = n.nxt
        linked_arr.append(str(n))

        return " -> ".join(linked_arr)

    def append(self, data):
        self.add_to_end(data)

    def __getitem__(self, index):
        return self.get_at_index(index)

    def __setitem__(self, index, value):
        self.add_to_index(index, value)

    def __iter__(self):
        return self

    def __next__(self):
        if self.root is None:
            raise StopIteration
        else:
            current = self.root
            self.root = self.root.nxt
            return current

l = LinkedList(0)
l.append(1)
l.append(2)
l.append(4)
for el in l:
    print(el)