class MyCircularQueue:

    def __init__(self, k: int):
        self.size = k
        self.queue = [-1] * k
        self.start = None
        self.end = None

    def enQueue(self, value: int) -> bool:
        if self.isFull():
            return False
        if self.start == None:
            self.start = 0
            self.end = -1
        self.end = (self.end + 1) % self.size
        self.queue[self.end] = value
        return True

    def deQueue(self) -> bool:
        if self.isEmpty():
            return False
        if self.start == None:
            return False
        self.queue[self.start] = -1
        self.start = (self.start + 1) % self.size
        return True

    def Front(self) -> int:
        if self.start == None or self.isEmpty():
            return -1
        return self.queue[self.start]

    def Rear(self) -> int:
        if self.end == None or self.isEmpty():
            return -1
        return self.queue[self.end]

    def isEmpty(self) -> bool:
        if self.start == None:
            return True
        if (self.end + 1) % self.size == self.start:
            if self.queue[self.end] == -1:
                return True
        return False

    def isFull(self) -> bool:
        if self.start == None:
            return False
        if (self.end + 1) % self.size == self.start:
            if self.queue[self.end] == -1:
                return False
            else:
                return True


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()