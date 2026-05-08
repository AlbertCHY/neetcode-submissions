class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maximum = 0
        curr = 1000

        for i in range(len(prices)):
            if prices[i] <= curr:
                curr = prices[i]
            else:
                maximum = max(maximum, prices[i] - curr)

        return maximum
