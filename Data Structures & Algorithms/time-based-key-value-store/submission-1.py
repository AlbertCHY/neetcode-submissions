class TimeMap:

    def __init__(self):
        self.table = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.table[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.table.get(key)
        if not arr:
            return ""
        for i in range(len(arr) - 1, -1, -1):
            if arr[i][0] > timestamp:
                continue
            else:
                return arr[i][1]

        return ""
    