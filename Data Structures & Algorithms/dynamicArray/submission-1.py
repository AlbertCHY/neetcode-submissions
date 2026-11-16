class DynamicArray:
    
    def __init__(self, capacity: int):
        self.cap = capacity
        self.arr = [None] * self.cap
        self.count = 0

    def get(self, i: int) -> int:
        return self.arr[i]

    def set(self, i: int, n: int) -> None:
        self.arr[i] = n

    def pushback(self, n: int) -> None:
        if self.cap == self.count:
            self.resize()
        self.arr[self.count] = n
        self.count += 1

    def popback(self) -> int:
        self.count -= 1
        return self.arr[self.count]

    def resize(self) -> None:
        self.arr.extend([None] * self.cap)
        self.cap += self.cap

    def getSize(self) -> int:
        return self.count
    
    def getCapacity(self) -> int:
        return self.cap
