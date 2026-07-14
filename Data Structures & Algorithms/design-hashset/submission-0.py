class MyHashSet:

    def __init__(self):
        self.table = [[] for _ in range(10000)]

    def add(self, key: int) -> None:
        idx = key % 10000
        if key not in self.table[idx]:
            self.table[idx].append(key)

    def remove(self, key: int) -> None:
        idx = key % 10000
        if key in self.table[idx]:
            self.table[idx].remove(key)

    def contains(self, key: int) -> bool:
        idx = key % 10000
        return key in self.table[idx]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)