class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hasStock = [-float("inf")] * n
        noStock = [-float("inf")] * n
        hasStock[0] = -prices[0]
        noStock[0] = 0

        for i in range(1, n):
            noStock[i] = max(hasStock[i - 1] + prices[i], noStock[i - 1])
            if i >= 2:
                hasStock[i] = max(hasStock[i - 1], noStock[i - 2] - prices[i])
            else:
                hasStock[i] = max(hasStock[i - 1], -prices[i])

        return noStock[n - 1]



        