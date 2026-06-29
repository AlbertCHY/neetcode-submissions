class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(s), len(p)
        memo = {}

        def dfs(i, j):
            if i == m:
                if j >= n or j == n - 2 and p[-1] == "*":
                    return True
                else:
                    return False

            if j >= n:
                return False

            if (i, j) in memo:
                return memo[(i, j)]

            if j + 1 < n:
                nxt = p[j + 1]
            else:
                nxt = "0"

            if nxt != "*":
                if p[j] == s[i] or p[j] == ".":
                    memo[(i, j)] = dfs(i + 1, j + 1)
                else:
                    return False
            else:
                if p[j] == s[i] or p[j] == ".":
                    memo[(i, j)] = dfs(i + 1, j) or dfs(i, j + 2)
                else:
                    return dfs(i, j + 2)
            return memo[(i, j)]

        return dfs(0, 0)




        