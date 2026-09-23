class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[1] * n  for _ in range(m)]

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        checker = False
        for i in range(m):
            if obstacleGrid[i][0]:
                checker = True
            if checker:
                dp[i][0] = 0
        checker = False
        for j in range(n):
            if obstacleGrid[0][j]:
                checker = True
            if checker:
                dp[0][j] = 0


        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1] if not obstacleGrid[i][j] else 0

        print(dp)
        return dp[m - 1][n - 1]