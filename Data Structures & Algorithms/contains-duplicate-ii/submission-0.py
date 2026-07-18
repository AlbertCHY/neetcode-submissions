class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        idx = 0
        table = set()

        for i in range(k):
            if nums[i] in table:
                return True
            table.add(nums[i])
        for i in range(k, len(nums)):
            
            if nums[i] in table:
                return True
            table.add(nums[i])
            table.remove(nums[idx])
            idx += 1

        return False
