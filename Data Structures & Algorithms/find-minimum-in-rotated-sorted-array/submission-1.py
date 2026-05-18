class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = 0, n - 1
        result = float("inf")

        if nums[right] > nums[left]:
            return nums[left]

        while left < right:
            mid = left + (right - left) // 2
            print(left, right)
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
            


        return nums[right]