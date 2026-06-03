class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        result = []
        tmp = []
        
        def dfs(curr, left, right):
            if curr < 0:
                return
            if curr == 0:
                if tmp != []:
                    result.append(tmp.copy())
                return

            for i in range(left, right):
                if nums[i] > curr:
                    continue
                tmp.append(nums[i])
                dfs(curr - nums[i], i, right)
                tmp.pop()
            return
            
        dfs(target, 0, len(nums))
        return result