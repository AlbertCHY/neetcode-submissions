class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        import bisect
        idx = bisect.bisect_left(arr, x)
        left, right = idx - 1, idx

        while right - left - 1 < k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            elif abs(arr[left] - x) <=  abs(arr[right] - x):
                left -= 1
            else:
                right += 1
        
        return arr[left + 1: right]