class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])

        def checker(i, j, visited, curr):
            if i < 0 or j < 0 or i >= m or j >= n:
                return False
            if board[i][j] != word[curr]:
                return False
            if curr == len(word) - 1:
                return True

            visited.add((i, j))
            up = ((i - 1, j) not in visited) and checker(i - 1, j, visited, curr + 1)
            down = ((i + 1, j) not in visited) and checker(i + 1, j, visited, curr + 1)
            left = ((i, j - 1) not in visited) and checker(i, j - 1, visited, curr + 1)
            right = ((i, j + 1) not in visited) and checker(i, j + 1, visited, curr + 1)
            visited.remove((i, j))

            return up or down or left or right

        for i in range(m):
            for j in range(n):
                if checker(i, j, set(), 0):
                    return True

        return False