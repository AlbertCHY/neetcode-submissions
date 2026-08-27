class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        cache = {}

        def dfs(i):
            if i == len(s):
                return 0

            if i in cache:
                return cache[i]

            result = 1 + dfs(i + 1)
            for j in range(i, len(s)):
                if s[i : j + 1] in words:
                    result = min(result, dfs(j + 1))
            cache[i] = result
            return result

        return dfs(0)