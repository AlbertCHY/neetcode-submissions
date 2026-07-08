class CountSquares:

    def __init__(self):
        self.table = {}

    def add(self, point: List[int]) -> None:
        self.table[(point[0], point[1])] = self.table.get((point[0], point[1]), 0) + 1

    def count(self, point: List[int]) -> int:
        result = 0
        x1, y1 = point[0], point[1]
        for key in self.table.keys():
            x2, y2 = key[0], key[1]
            if abs(x1 - x2) == abs(y1 - y2) != 0:
                result += self.table.get((x2, y1), 0) * self.table.get((x1, y2), 0) * self.table.get((x2, y2), 0)
        return result
