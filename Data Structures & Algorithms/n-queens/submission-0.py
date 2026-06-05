class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        table = [["."] * n for i in range(n)]
        visited = [[0] * n for i in range(n)]

        def dfs(row):
            if row == n:
                tmp = [""] * n
                for i in range(n):
                    tmp[i] = "".join(table[i].copy())
                print(tmp)
                result.append(tmp)
                return

            for col in range(n):
                if not visited[row][col]:
                    table[row][col] = "Q"
                    label(row, col, 1)
                    dfs(row + 1)
                    table[row][col] = "."
                    label(row, col, -1)

        def label(a, b, change):
            for i in range(n):
                for j in range(n):
                    if i == a or j == b or (i + j) == (a + b) or (j - i) == (b - a):
                        visited[i][j] += change



        dfs(0)
        
        return result