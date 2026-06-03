class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        n = len(nums)

        def dfs(i, arr, my_set):
            if i == n:
                result.append(arr.copy())
                return
            
            for j in range(n):
                if nums[j] not in my_set:
                    arr.append(nums[j])
                    my_set.add(nums[j])
                    dfs(i + 1, arr, my_set)
                    arr.pop()
                    my_set.remove(nums[j])



        dfs(0, [], set())
        return result