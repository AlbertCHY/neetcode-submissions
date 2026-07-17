class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        left, right = 0, 0
        while left < len(word1) and right < len(word2):
            result.append(word1[left])
            result.append(word2[right])
            left, right = left + 1, right + 1

        while left < len(word1):
            result.append(word1[left])
            left += 1
        while right < len(word2):
            result.append(word2[right])
            right += 1

        return "".join(result)