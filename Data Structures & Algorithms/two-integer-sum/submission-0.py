class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}

        for i in range(len(nums)):
            if target - nums[i] in my_dict.keys():
                return [my_dict.get(target - nums[i]), i]
            my_dict[nums[i]] = i

        return [-1, -1]
