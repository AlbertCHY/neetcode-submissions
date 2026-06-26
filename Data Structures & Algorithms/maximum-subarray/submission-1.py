class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        def dfs(l, r):
            if l > r:
                return float("-inf")

            m = (l + r) // 2
            lsum = rsum = curr = 0
            for i in range(m - 1, l - 1, -1):
                curr += nums[i]
                lsum = max(lsum, curr)

            curr = 0
            for i in range(m + 1, r + 1):
                curr += nums[i]
                rsum = max(rsum, curr)

            return (max(dfs(l, m - 1), dfs(m + 1, r), lsum + nums[m] + rsum))



        return dfs(0, len(nums) - 1)