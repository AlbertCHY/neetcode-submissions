class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        left, right = 0, m
        
        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i
            
            A_left = float("-inf") if i == 0 else nums1[i - 1]
            A_right = float("inf") if i == m else nums1[i]
            B_left = float("-inf") if j == 0 else nums2[j - 1]
            B_right = float("inf") if j == n else nums2[j]
            
            if A_left > B_right:
                right = i - 1
            elif B_left > A_right:
                left = i + 1
            else:
                if (m + n) % 2 == 1:
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2