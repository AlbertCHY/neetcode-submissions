class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        result = 0

        def helper(i, curr):
            nonlocal result
            if i == len(nums):
                result += curr
                return

            helper(i + 1, curr ^ nums[i])
            helper(i + 1, curr)

        helper(0, 0)
        return result