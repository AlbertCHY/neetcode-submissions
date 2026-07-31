class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        cache = {}
        
        def helper(i):
            if i not in cache:
                cache[i] = mountainArr.get(i)
            return cache[i]

        n = mountainArr.length()
        left, right = 1, n - 2
        while left < right:
            mid = left + (right - left) // 2
            m, r = helper(mid), helper(mid + 1)
            if m < r:
                left = mid + 1
            else:
                right = mid
        peak = left

        left, right = 0, peak - 1
        while left <= right:
            mid = left + (right - left) // 2
            curr = helper(mid)
            if curr < target:
                left = mid + 1
            elif curr > target:
                right = mid - 1
            else:
                return mid

        left, right = peak, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            curr = helper(mid)
            if curr > target:
                left = mid + 1
            elif curr < target:
                right = mid - 1
            else:
                return mid

        return -1