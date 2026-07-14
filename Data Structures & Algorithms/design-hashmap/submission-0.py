class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val

class MyHashMap:

    def __init__(self):
        self.table = [[] for _ in range(10000)]

    def put(self, key: int, value: int) -> None:
        idx = key % 10000
        for i in range(len(self.table[idx])):
            if key == self.table[idx][i].key:
                self.table[idx][i] = Node(key, value)
                return
        self.table[idx].append(Node(key, value))

    def get(self, key: int) -> int:
        idx = key % 10000
        for node in self.table[idx]:
            if key == node.key:
                return node.val
        return -1
        
    def remove(self, key: int) -> None:
        idx = key % 10000
        for node in self.table[idx]:
            if key == node.key:
                self.table[idx].remove(node)

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)