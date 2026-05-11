class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_set = set(s)
        result = 0

        for c in my_set:
            left = count = 0
            for j in range(len(s)):
                if s[j] == c:
                    count += 1
                while j - left + 1 - count > k:
                    if s[left] == c:
                        count -= 1
                    left += 1
                result = max(result, j - left + 1)

        return result