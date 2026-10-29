class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        zeros = 0
        for c in s:
            if c == "1":
                ones += 1
            else:
                zeros += 1

        result = []
        ones -= 1
        while ones > 0:
            result.append("1")
            ones -= 1
        while zeros > 0:
            result.append("0")
            zeros -= 1
        result.append("1")

        return "".join(result)