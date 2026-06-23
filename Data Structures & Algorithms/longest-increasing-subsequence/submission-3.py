class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        dp[0] = 1
        result = 1

        for i in range(1, n):
            tmp = -float("inf")
            for j in range(i):
                if nums[j] < nums[i]:
                    tmp = max(tmp, dp[j])
            if tmp == -float("inf"):
                dp[i] = 1
            else:
                dp[i] = tmp + 1
            result = max(result, dp[i])
        print(dp)
        return result

        