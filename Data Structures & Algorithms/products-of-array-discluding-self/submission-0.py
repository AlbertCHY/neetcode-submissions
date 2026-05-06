class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        fromLeft, fromRight = [1] * n, [1] * n
        for i in range(1, n):
            fromLeft[i] = nums[i - 1] * fromLeft[i - 1]
        for i in range(n - 2, -1, -1):
            fromRight[i] = nums[i + 1] * fromRight[i + 1]
        
        result = []
        for i in range(n):
            result.append(fromLeft[i] * fromRight[i])
        
        return result