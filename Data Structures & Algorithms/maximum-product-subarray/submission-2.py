class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        result = -float("inf")
        left, right = 0, 0

        curr = 1
        while right < n:
            while right < n and nums[right] == 0:
                result = max(result, 0)
                right += 1
            left = right
            curr = 1
            countNeg = 0
            while right < n and nums[right] != 0:
                if nums[right] < 0:
                    countNeg += 1
                curr *= nums[right]
                result = max(result, curr)
                right += 1
            if countNeg % 2 == 1 and right - left != 1:
                while left < right and nums[left] > 0:
                    curr /= nums[left]
                    left += 1
                curr /= nums[left]
                result = max(result, curr)
            


        return int(result)
