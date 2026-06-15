class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = [-1] * len(nums)

        def dfs(i):
            if i >= len(nums):
                return 0
            if dp[i] != -1:
                return dp[i]

            dp[i] = max(dfs(i + 1), dfs(i + 2) + nums[i])
            return dp[i]

            


        return dfs(0)