class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1

        def helper(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        while left < right:
            if s[left] != s[right]:
                return helper(left, right - 1) or helper(left + 1, right)
            left += 1
            right -= 1

        return True