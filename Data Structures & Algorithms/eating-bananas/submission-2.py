class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        def checker(k):
            tmp = 0
            for i in range(n):
                tmp += (piles[i] + k - 1) // k
            return tmp <= h

        left, right = 1, 1000000000
        while left < right:
            mid = left + (right - left) // 2
            if checker(mid):
                right = mid
            else:
                left = mid + 1

        return left