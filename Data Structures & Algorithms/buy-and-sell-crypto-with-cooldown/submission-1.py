class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = {}

        def dfs(i, canBuy):
            if i >= n:
                return 0

            if (i, canBuy) in dp:
                return dp[(i, canBuy)]

            skip = dfs(i + 1, canBuy)

            if canBuy:
                buy = dfs(i + 1, False) - prices[i]
                dp[(i, canBuy)] = max(buy, skip)
            else:
                sell = dfs(i + 2, True) + prices[i]
                dp[(i, canBuy)] = max(sell, skip)

            return dp[(i, canBuy)]

        return dfs(0, True)



        