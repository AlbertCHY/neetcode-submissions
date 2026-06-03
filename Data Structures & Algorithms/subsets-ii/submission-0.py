class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []

        def dfs(index, arr):
            if index == n:
                result.append(arr.copy())
                return
            
            arr.append(nums[index])
            dfs(index + 1, arr)
            arr.pop()
            while index + 1 < n and nums[index] == nums[index + 1]:
                index += 1
            dfs(index + 1, arr)




        dfs(0, [])
        return result