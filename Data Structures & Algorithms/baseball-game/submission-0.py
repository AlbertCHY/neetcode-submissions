class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        board = []

        for operation in operations:
            if operation == "+":
                num2 = board.pop()
                num1 = board.pop()
                num3 = num1 + num2
                board.append(num1)
                board.append(num2)
                board.append(num3)
            elif operation == "C":
                board.pop()
            elif operation == "D":
                board.append(board[-1] * 2)
            else:
                board.append(int(operation))

        result = 0
        for num in board:
            result += num

        return result