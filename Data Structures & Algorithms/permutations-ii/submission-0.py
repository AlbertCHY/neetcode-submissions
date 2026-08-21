class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        result = []
        def dfs(arr):
            if len(arr) == len(nums):
                result.append(arr.copy())
                return
            
            for num in freq:
                if freq[num] > 0:
                    arr.append(num)
                    freq[num] -= 1
                    dfs(arr)
                    arr.pop()
                    freq[num] += 1

        dfs([])
        return result