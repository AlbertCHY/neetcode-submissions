class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        carrys = [False] * n
        for i in range(n):
            if digits[i] == 9:
                carrys[i] = True

        if digits[-1] != 9:
            digits[-1] += 1
            return digits

        index = n - 1
        while index >= 0 and carrys[index]:
            digits[index] = 0
            index -= 1

        if index == -1:
            return [1] + digits
        else:
            digits[index] += 1
            return digits


            