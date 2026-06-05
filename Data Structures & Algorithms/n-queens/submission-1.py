class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        result = []
        table = [["."] * n for i in range(n)]
        used_colum = set()
        used_slash = set()
        used_bslash = set()



        def dfs(row):
            if row == n:
                tmp = ["".join(i) for i in table]
                result.append(tmp)
                return

            for col in range(n):
                if col in used_colum or (row + col) in used_slash or (row - col) in used_bslash:
                    continue
                table[row][col] = "Q"
                used_colum.add(col)
                used_slash.add(row + col)
                used_bslash.add(row - col)
                dfs(row + 1)
                table[row][col] = "."
                used_colum.remove(col)
                used_slash.remove(row + col)
                used_bslash.remove(row - col)

        dfs(0)
        
        return result