class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n + 1)]
        dp[0][0] = 1

        for i in range(1, n + 1):
            for total, ways in dp[i - 1].items():
                dp[i][total + nums[i - 1]] += ways
                dp[i][total - nums[i - 1]] += ways

        return dp[n][target]