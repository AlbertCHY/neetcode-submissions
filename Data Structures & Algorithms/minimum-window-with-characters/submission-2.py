class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        t_map = {}
        for c in t:
            t_map[c] = t_map.get(c, 0) + 1
        
        result = "0" * 1001
        matches = 0
        s_map = {}
        left = 0
        while s[left] not in t_map:
            left += 1
            if left == len(s):
                return ""

        for right in range(left, len(s)):
            if s[right] not in t_map:
                continue
            s_map[s[right]] = s_map.get(s[right], 0) + 1
            if s_map[s[right]] == t_map[s[right]]:
                matches += 1
                while matches == len(t_map.keys()) or s[left] not in t_map:
                    if s[left] not in t_map:
                        left += 1
                        continue
                    result = s[left:right + 1] if len(result) > right + 1 - left else result
                    s_map[s[left]] -= 1
                    if s_map[s[left]] < t_map[s[left]]:
                        matches -=1
                    left += 1
                    if left >= right:
                        break
                    

        return result if len(result) < 1001 else ""
