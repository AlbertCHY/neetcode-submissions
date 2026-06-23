class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)
        if target % 2 != 0:
            return False
        target //= 2
        
        n = len(nums)
        dp = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, curr):
            if curr == 0:
                return True
            if i >= n or curr < 0:
                return False

            if dp[i][curr] != -1:
                return dp[i][curr]

            dp[i][curr] = dfs(i + 1, curr) or dfs(i + 1, curr - nums[i])
            return dp[i][curr]


        return dfs(0, target)