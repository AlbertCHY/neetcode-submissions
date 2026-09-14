class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1
            offset = columnNumber % 26
            result += chr(ord('A') + offset)
            columnNumber //= 26

        return "".join(reversed(result))
