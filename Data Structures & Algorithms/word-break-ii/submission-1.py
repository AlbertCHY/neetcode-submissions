class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        result = []
        words = set(wordDict)

        def dfs(start, arr):
            if start == len(s):
                result.append(" ".join(arr))
                return
            
            for j in range(start, len(s)):
                if s[start : j + 1] not in words:
                    continue
                arr.append(s[start : j + 1])
                dfs(j + 1, arr)
                arr.pop()
            return

        dfs(0, [])
        return result