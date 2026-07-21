class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        count = n - 1
        start = 0

        while count > 0:
            curr = (start + k) % n
            prev = nums[start]
            while True:
                count -= 1
                if curr == start:
                    nums[curr] = prev
                    break
                tmp = nums[curr]
                nums[curr] = prev
                prev = tmp
                print(nums[curr], prev)
                curr = (curr + k) % n
            start += 1

        
                

        