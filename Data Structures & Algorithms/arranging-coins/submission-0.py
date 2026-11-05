class Solution:
    def arrangeCoins(self, n: int) -> int:
        base = 1
        while True:
            if base * (base + 1) // 2 > n:
                break
            base += 1

        return base - 1