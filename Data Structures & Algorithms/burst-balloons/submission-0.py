class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        n = len(nums)
        nums = [1] + nums + [1]
        memo = {}

        def dfs(arr):
            if len(arr) == 2:
                return 0

            if str(arr) in memo:
                return memo[str(arr)]

            result = 0
            for i in range(1, len(arr) - 1):
                curr = arr[i - 1] * arr[i] * arr[i + 1]
                curr += dfs(arr[:i] + arr[i + 1:])
                result = max(result, curr)
            
            memo[str(arr)] = result
            return result

        return dfs(nums)