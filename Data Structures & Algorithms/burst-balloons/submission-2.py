class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in range(n)]

        for length in range(3, n + 1):
            for l in range(0, n - length + 1):
                r = l + length - 1
                for i in range(l + 1, r):
                    coins = nums[l] * nums[i] * nums[r]
                    total = coins + dp[l][i] + dp[i][r]
                    dp[l][r] = max(dp[l][r], total)

        return dp[0][n - 1]