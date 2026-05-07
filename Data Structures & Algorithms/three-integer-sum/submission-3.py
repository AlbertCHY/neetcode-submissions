class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = set()
        
        for i in range(1, len(nums) - 1):
            left, right = 0, len(nums) - 1
            target = -nums[i]
            
            while left < i and right > i:
                current_sum = nums[left] + nums[right]
                if current_sum == target:
                    result.add((nums[left], nums[i], nums[right]))
                    left += 1
                    right -= 1
                elif current_sum < target:
                    left += 1
                else:
                    right -= 1
                    
        return [list(triplet) for triplet in result]