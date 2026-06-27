class Solution:
    def canJump(self, nums: List[int]) -> bool:
        visited = set()
        visited.add(0)

        for i in range(len(nums)):
            if i == len(nums) - 1:
                return i in visited
            if i not in visited:
                continue
            
            for j in range(i + 1, i + nums[i] + 1):
                visited.add(j)
