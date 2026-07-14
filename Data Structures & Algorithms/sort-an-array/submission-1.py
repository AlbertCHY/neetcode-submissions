import random
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def quicksort(left, right):
            if left >= right:
                return

            pivot = random.randint(left, right)
            nums[pivot], nums[right] = nums[right], nums[pivot]
            i = left
            for j in range(left, right):
                if nums[j] <= nums[right]:
                    nums[i], nums[j] = nums[j], nums[i]
                    i += 1
            nums[i], nums[right] = nums[right], nums[i]
            quicksort(left, i - 1)
            quicksort(i + 1, right)

        
        quicksort(0, len(nums) - 1)
        return nums

        