class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(n):
            nxt = defaultdict(int)
            for total, ways in dp.items():
                nxt[total + nums[i]] += ways
                nxt[total - nums[i]] += ways
            dp = nxt

        return dp[target]