class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        result = float("inf")
        left = 0
        curr = 0
        
        for i in range(len(nums)):
            curr += nums[i]
            if curr >= target:
                while curr >= target:
                    result = min(result, i - left + 1)
                    curr -= nums[left]
                    left += 1

        return 0 if result == float("inf") else result