class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequence = {}

        for c in s:
            frequence[c] = frequence.get(c, 0) + 1

        for c in t:
            if c not in frequence:
                return False
            frequence[c] = frequence.get(c) - 1
            if frequence.get(c) == 0:
                frequence.pop(c)

        return not frequence