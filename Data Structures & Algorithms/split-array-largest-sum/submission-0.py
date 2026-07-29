class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        left = max(nums)
        right = sum(nums)
        result = right

        def helper(target):
            curr = 0
            count = 0
            for num in nums:
                if curr + num <= target:
                    curr += num
                else:
                    curr = num
                    count += 1
                    if count > k:
                        return False
            if curr != 0:
                count += 1
            return count <= k

        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result