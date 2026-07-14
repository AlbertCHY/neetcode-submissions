class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        table = defaultdict(int)
        for num in nums:
            table[num] += 1

        idx = 0
        for i in range(3):
            while table[i] > 0:
                nums[idx] = i
                table[i] -= 1
                idx += 1

        