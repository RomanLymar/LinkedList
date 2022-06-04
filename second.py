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
            for n in self:
                pass
            n.nxt = Node(data)
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
        n = self.head
        while n is not None:
            yield n
            n = n.nxt


l = LinkedList().add(1).add(2).add(3).add(4).add(5).add(6).add(7)
for el in l:
    print(el)
print(l)