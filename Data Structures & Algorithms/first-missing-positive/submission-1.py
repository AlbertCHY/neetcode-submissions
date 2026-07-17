class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        nums.append(0)

        def helper(idx, num):
            tmp = nums[idx]
            nums[idx] = num
            if tmp < 0 or tmp >= len(nums) or tmp == idx:
                return
            helper(tmp, tmp)
        
        for i in range(len(nums)):
            if nums[i] < 0 or nums[i] >= len(nums) or nums[i] == i:
                continue
            helper(nums[i], nums[i])

        
        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)