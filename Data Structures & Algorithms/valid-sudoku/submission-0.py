class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def checker(arr):
            tmp = set()
            for c in arr:
                if c == ".":
                    continue
                if c in tmp:
                    return False
                tmp.add(c)
            return True

        for i in range(9):
            if not checker(board[i]):
                return False
        
        for i in range(9):
            if not checker([board[j][i] for j in range(9)]):
                return False

        for offsetX in range(3):
            for offsetY in range(3):
                tmp = []
                for i in range(3):
                    for j in range(3):
                        tmp.append(board[i + 3 * offsetX][j + 3 * offsetY])
                if not checker(tmp):
                    return False

        return True