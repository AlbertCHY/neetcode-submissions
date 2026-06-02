class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for i in range(len(nums)):
            n = len(result)
            for j in range(n):
                result.append(result[j] + [nums[i]])

        return result