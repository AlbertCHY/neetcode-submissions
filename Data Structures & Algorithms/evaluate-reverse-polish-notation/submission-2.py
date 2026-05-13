class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {"+", "-", "*", "/"}
        result = 0
        for s in tokens:
            if s not in operators:
                stack.append(int(s))
            else:
                tmp1 = stack.pop()
                tmp2 = stack.pop()
                print(tmp2, s, tmp1)
                if s == "+":
                    stack.append(tmp2 + tmp1)
                elif s == "-":
                    stack.append(tmp2 - tmp1)
                elif s == "*":
                    stack.append(tmp2 * tmp1)
                else:
                    stack.append(int(tmp2 / tmp1))

        return stack[-1]