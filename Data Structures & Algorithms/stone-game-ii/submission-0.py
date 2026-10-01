class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        dp = {}
        
        def dfs(aTurn, i, M):
            if i == len(piles):
                return 0
            if (aTurn, i, M) in dp:
                return dp[(aTurn, i, M)]

            result = 0 if aTurn else float("inf")
            total = 0
            for X in range(1, 2 * M + 1):
                if i + X > len(piles):
                    break
                total += piles[i + X - 1]
                if aTurn:
                    result = max(result, total + dfs(not aTurn, i + X, max(M, X)))
                else:
                    result = min(result, dfs(not aTurn, i + X, max(M, X)))

            dp[(aTurn, i, M)] = result
            return result  

        return dfs(True, 0, 1)