class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        xset, yset = set(), set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    xset.add(i)
                    yset.add(j)

        for i in range(m):
            for j in range(n):
                if i in xset or j in yset:
                    matrix[i][j] = 0

