class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)

        dp[0] = 0
        for coin in coins:
            if coin <= amount:
                dp[coin] = 1
        
        for i in range(1, len(dp)):
            curr = dp[i]
            for coin in coins:
                if i - coin >= 1:
                    curr = min(curr, dp[i - coin] + 1)
            dp[i] = curr

        print(dp)

        return -1 if dp[amount] == float("inf") else dp[amount]