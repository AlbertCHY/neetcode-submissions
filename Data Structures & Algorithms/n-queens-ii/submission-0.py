class Solution:
    def totalNQueens(self, n: int) -> int:
        result = 0
        colset = set()
        posDiag = set()
        negDiag = set()

        def dfs(i):
            nonlocal result
            if i == n:
                result += 1
                return

            for j in range(n):
                if j in colset or (i + j) in posDiag or (i - j) in negDiag:
                    continue
                colset.add(j)
                posDiag.add(i + j)
                negDiag.add(i - j)
                dfs(i + 1)
                colset.remove(j)
                posDiag.remove(i + j)
                negDiag.remove(i - j)        

        dfs(0)
        return result
