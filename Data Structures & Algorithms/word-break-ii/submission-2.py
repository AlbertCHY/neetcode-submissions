class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        words = set(wordDict)
        cache = {}

        def dfs(i):
            if i == len(s):
                return [""]

            if i in cache:
                return cache[i]

            result = []
            for j in range(i, len(s)):
                word = s[i:j + 1]
                if word not in words:
                    continue
                strings = dfs(j + 1)
                for substr in strings:
                    sentence = word
                    if substr:
                        sentence += " " + substr
                    result.append(sentence)
            cache[i] = result
            return result


        return dfs(0)