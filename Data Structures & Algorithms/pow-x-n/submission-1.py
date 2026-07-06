class Solution:
    def myPow(self, x: float, n: int) -> float:
        exp = abs(n)
        curr = 1
        while exp != 0:
            curr *= x
            exp -= 1

        return 1/curr if n < 0 else curr