class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n = len(coins)
        coins.sort()
        dp = {}

        def dfs(index, curr):
            if index >= n or curr > amount:
                return 0
            if curr == amount:
                return 1

            if (index, curr) in dp:
                return dp[(index, curr)]

            dp[(index, curr)] =  dfs(index, curr + coins[index]) + dfs(index + 1, curr)
            return dp[(index, curr)]

        return dfs(0, 0)