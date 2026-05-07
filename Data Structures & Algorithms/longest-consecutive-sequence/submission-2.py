class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        minimum, maximum = nums[0], nums[0]
        sequence = set()

        for n in nums:
            minimum = min(minimum, n)
            maximum = max(maximum, n)
            sequence.add(n)

        count = 1
        result = 1
        for i in range(minimum + 1, maximum + 1):
            if i in sequence:
                count += 1
                result = max(result, count)
            else:
                count = 0
        
        return result
