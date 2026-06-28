class Solution:
    def jump(self, nums: List[int]) -> int:
        reachable = 0
        nextReachable = 0
        steps = 0

        if len(nums) <= 1:
            return 0
        
        for i in range(len(nums) - 1):
            nextReachable = max(nextReachable, i + nums[i])
            if i == reachable:
                steps += 1
                reachable = nextReachable
                if reachable >= len(nums):
                    break

        return steps