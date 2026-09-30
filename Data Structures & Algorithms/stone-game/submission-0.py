class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        n = len(piles) - 1
        memo = {}

        def dfs(l, r):
            if l > r:
                return 0
            if (l, r) in memo:
                return memo[(l, r)]
            
            even = (r - l) % 2 == 0
            left = piles[l] if even else 0
            right = piles[r] if even else 0
            memo[(l, r)] = max(dfs(l + 1, r) + left, dfs(l, r - 1) + right)
            return memo[(l, r)]
        
        result = dfs(0, n)
        return result > total - result