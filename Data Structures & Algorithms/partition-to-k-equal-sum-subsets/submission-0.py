class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        target = total // k
        nums.sort(reverse = True)
        if nums[0] > target:
            return False

        visited = [False] * len(nums)

        def backtrack(index, ith, curr):
            if ith == k:
                return True
            if curr == target:
                return backtrack(0, ith + 1, 0)
            
            for i in range(index, len(nums)):
                if visited[i] or curr + nums[i] > target:
                    continue
                visited[i] = True
                if backtrack(i + 1, ith, curr + nums[i]):
                    return True
                visited[i] = False

            return False

        return backtrack(0, 0, 0)