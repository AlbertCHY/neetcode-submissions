class Solution:
    def minEnd(self, n: int, x: int) -> int:
        target = n - 1
        result = x
        j = 0

        while target != 0:
            if (result & (1 << j)) == 0:
                if target & 1:
                    result |= 1 << j
                target >>= 1
            j += 1

        return result