class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == "0" or num2 == "0":
            return "0"

        if len(num1) < len(num2):
            num1, num2 = num2, num1

        def multiply(num: str, digit: str, offset: int):
            i, carry = len(num) - 1, 0
            digit2 = int(digit)
            result = []

            while i >= 0 or carry:
                digit1 = int(num1[i]) if i >= 0 else 0
                total = digit1 * digit2 + carry
                result.append(str(total % 10))
                carry = total // 10
                i -= 1

            return "".join(result[::-1]) + "0" * offset

        def add(num1: str, num2: str):
            i, j, carry = len(num1) - 1, len(num2) - 1, 0
            result = []

            while i >= 0 or j >= 0 or carry:
                digit1 = int(num1[i]) if i >= 0 else 0
                digit2 = int(num2[j]) if j >= 0 else 0
                total = digit1 + digit2 + carry
                result.append(str(total % 10))
                carry = total // 10
                i -= 1
                j -= 1

            return "".join(result[::-1])
        
        result, offset = "", 0
        for i in range(len(num2) - 1, -1, -1):
            curr = multiply(num1, num2[i], offset)
            result = add(result, curr)
            offset += 1

        return result