import copy
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = [[]]

        for i in range(len(nums)):
            n = len(result)
            for j in range(n):
                if result[j]:
                    tmp = copy.deepcopy(result[j])
                    tmp.append(nums[i])
                else:
                    tmp = [nums[i]]
                result.append(tmp)
            print(result)

        return result