class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        n = mountainArr.length()
        left, right = 1, n - 2
        while left <= right:
            mid = left + (right - left) // 2
            l, m, r = mountainArr.get(mid - 1), mountainArr.get(mid), mountainArr.get(mid + 1)
            if l < m < r:
                left = mid + 1
            elif l > m > r:
                right = mid - 1
            else:
                break
        peak = mid

        left, right = 0, peak - 1
        while left <= right:
            mid = left + (right - left) // 2
            curr = mountainArr.get(mid)
            if curr < target:
                left = mid + 1
            elif curr > target:
                right = mid - 1
            else:
                return mid

        left, right = peak, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            curr = mountainArr.get(mid)
            if curr > target:
                left = mid + 1
            elif curr < target:
                right = mid - 1
            else:
                return mid

        return -1