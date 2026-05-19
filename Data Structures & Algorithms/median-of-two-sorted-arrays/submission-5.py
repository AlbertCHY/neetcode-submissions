class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)

        if not nums1:
            return nums2[n // 2] if n % 2 == 1 else (nums2[n // 2] + nums2[n // 2 - 1]) / 2
        if not nums2:
            return nums1[m // 2] if m % 2 == 1 else (nums1[m // 2] + nums1[m // 2 - 1]) / 2

        def helper(arr, target):
            left, right = 0, len(arr)
            while left < right:
                mid = (left + right) // 2
                if arr[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left

        def findKth(k):
            low, high = -1000000, 1000000
            while low < high:
                middle = (low + high + 1) // 2
                count1 = helper(nums1, middle)
                count2 = helper(nums2, middle)
                if count1 + count2 >= k:
                    high = middle - 1
                else:
                    low = middle
            return low

        if (m + n) % 2 == 1:
            return findKth((m + n) // 2 + 1)
        else:
            return (findKth((m + n) // 2) + findKth((m + n) // 2 + 1)) / 2

        # nums1.append(float("inf"))
        # nums2.append(float("inf"))
        # low, high = -1000000, 1000000
        # left1, left2, right1, right2 = 0, 0, m, n
        # idx1, idx2 = 0, 0
        # while low < high:
        #     middle = (low + high) // 2
        #     idx1 = helper(left1, right1, nums1, middle)
        #     idx2 = helper(left2, right2, nums2, middle)
        #     if idx1 + idx2 > median:
        #         high = middle
        #     else:
        #         low = middle + 1
            
        # print(idx1, idx2, middle)

        # if median % 1 == 0:
        #     if idx1 == 0:
        #         return nums2[idx2 - 1]
        #     if idx2 == 0:
        #         return nums1[idx1 - 1]
        #     return max(nums1[idx1 - 1], nums2[idx2 - 1])
        # else:
        #     if idx1 == 0:
        #         return (min(nums1[idx1], nums2[idx2]) + nums2[idx2 - 1]) / 2
        #     if idx2 == 0:
        #         return (min(nums1[idx1], nums2[idx2]) + nums1[idx1 - 1]) / 2
        #     if idx1 == m and idx2 == n:
        #         nums1[idx1] = nums1[idx1 - 1]
        #         nums2[idx2] = nums2[idx2 - 1]
        #     return (min(nums1[idx1], nums2[idx2]) + max(nums1[idx1 - 1], nums2[idx2 - 1])) / 2
