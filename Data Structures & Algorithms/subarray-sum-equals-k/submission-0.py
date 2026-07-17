class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        result = 0
        curr = 0
        prefix = {0 : 1}

        for num in nums:
            curr += num
            if (curr - k) in prefix:
                result += prefix[(curr - k)]
            prefix[curr] = 1 + prefix.get(curr, 0)

        return result