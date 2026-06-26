class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [[0] * 2 for _ in range(n)]
        dp[0][0] = dp[0][1] = nums[0]
       
        for i in range(1, n):
            dp[i][0] = max(nums[i], nums[i] + dp[i - 1][0])
            dp[i][1] = max(dp[i - 1][1], dp[i][0])

        return dp[n - 1][1]