class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        result = float("inf")

        def helper(target):
            count, curr = 1, target
            for w in weights:
                if curr - w < 0:
                    count += 1
                    if count > days:
                        return False
                    curr = target
                curr -= w
            return True

        
        while left <= right:
            mid = (left + right) // 2
            if helper(mid):
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1

        return result