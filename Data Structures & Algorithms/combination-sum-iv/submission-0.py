class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        memo = {}

        def dfs(curr):
            if curr == target:
                return 1

            if curr in memo:
                return memo[curr]

            result = 0
            for i in range(len(nums)):
                if target - curr < nums[i]:
                    break
                result += dfs(curr + nums[i])
            memo[curr] = result
            return result
        
        return dfs(0)


