class MinStack:

    def __init__(self):
        self.stack = []
        self.smallest = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.smallest:
            self.smallest.append(val)
        else:
            self.smallest.append(min(self.smallest[-1], val))

    def pop(self) -> None:
        self.stack.pop()
        self.smallest.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.smallest[-1]
