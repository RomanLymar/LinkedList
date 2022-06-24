class Node:

    def __init__(self, data, nxt = None):
        self.data = data
        self.nxt = nxt

    def __str__(self):
        return str(self.data)


class LinkedList:

    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            for cur in self:
                pass
            cur.nxt = Node(data)
        return self

    def get_node(self, node_index):
        for index, node in enumerate(self):
            if index == node_index:
                break
        else:
            return None
        return node

    def __str__(self):
        return " -> ".join(map(str, self))

    def __iter__(self):
        return self

    def __next__(self):
        if self.root is None:
            raise StopIteration
        else:
            current = self.root
            self.root = self.root.nxt
            return current


l = LinkedList()
l.add(2)
l.add(3)
l.add(4)

for el in l:
    print(el)
print(l)