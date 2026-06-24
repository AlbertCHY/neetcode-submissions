class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = {}

        def dfs(i, curr):
            if i == n:
                return 1 if curr == target else 0
            if (i, curr) in dp:
                return dp[(i, curr)]

            dp[(i, curr)] = dfs(i + 1, curr + nums[i]) + dfs(i + 1, curr - nums[i])
            return dp[(i, curr)]

        return dfs(0, 0)