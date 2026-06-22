class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True

        for i in range(1, n + 1):
            for word in wordDict:
                m = len(word)
                if i >= m and  s[i - m : i] == word:
                    if dp[i - m]:
                        dp[i] = True
        return dp[n]