class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        my_set = set(s)
        result = 0

        for c in my_set:
            left = count = 0
            for right in range(len(s)):
                if s[right] == c:
                    count += 1
                
                while right - left - count >= k:
                    if s[left] == c:
                        count -= 1
                    left += 1
                
                result = max(result, right - left + 1)

        return result