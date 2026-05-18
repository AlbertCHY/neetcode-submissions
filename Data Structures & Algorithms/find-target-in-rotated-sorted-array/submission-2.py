class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        if nums[left] > nums[right]:
            while left < right:
                mid = left + (right - left) // 2
                if nums[mid] < nums[right]:
                    right = mid
                else:
                    left = mid + 1
            left = right

        if nums[left] <= target <= nums[-1]:
            right = n - 1
        else:
            right = left - 1
            left = 0

        return self.helper(nums, left, right, target)

    def helper(self, nums, left, right, target):
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return -1