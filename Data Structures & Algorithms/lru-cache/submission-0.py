class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = self.right = None

class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.size = capacity

        self.lhead, self.rhead = Node(0, 0), Node(0, 0)
        self.lhead.right = self.rhead
        self.rhead.left = self.lhead

    def remove(self, node):
        nodeleft, noderight = node.left, node.right
        nodeleft.right, noderight.left = noderight, nodeleft

    def insert(self, node):
        tailleft, tail = self.rhead.left, self.rhead
        tailleft.right = tail.left = node
        node.left, node.right = tailleft, tail    

    def get(self, key: int) -> int:
        if key in self.table:
            self.remove(self.table[key])
            self.insert(self.table[key])
            return self.table[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.remove(self.table[key])
        self.table[key] = Node(key, value)
        self.insert(self.table[key])

        if len(self.table) > self.size:
            tmp = self.lhead.right
            self.remove(tmp)
            del self.table[tmp.key]
