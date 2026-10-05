class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        suffix_sum = [0] * n
        suffix_sum[-1] = nums[-1]
        curr = nums[-1]

        for i in range(n - 2, -1, -1):
            curr += nums[i]
            suffix_sum[i] = max(suffix_sum[i + 1], curr)

        wrap_max = 0
        result = nums[0]
        prefix_sum = 0

        for i in range(n):
            wrap_max = max(wrap_max, 0) + nums[i]    
            result = max(result, wrap_max)
            prefix_sum += nums[i]
            if i + 1 < n:
                result = max(result, prefix_sum + suffix_sum[i + 1])

        return result