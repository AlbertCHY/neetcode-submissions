class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}

        def dfs(i):
            if i == n - 1:
                return 0

            if i in memo:
                return memo[i]

            end = min(n - 1, i + nums[i])
            tmp = float("inf")
            for j in range(i + 1, end + 1):
                tmp = min(tmp, 1 + dfs(j))
            memo[i] = tmp
            return tmp

        return dfs(0)