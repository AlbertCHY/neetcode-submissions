class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        haveStock = [0] * n
        noStock = [0] * n
        haveStock[0] = -prices[0]
        noStock[0] = 0

        for i in range(1, n):
            haveStock[i] = max(noStock[i - 1] - prices[i], haveStock[i - 1])
            noStock[i] = max(noStock[i - 1], haveStock[i - 1] + prices[i])

        return noStock[n - 1]