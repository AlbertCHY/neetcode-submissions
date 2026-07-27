class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for c in s:
            if c != "]":
                stack.append(c)
            else:
                tmp = ""
                while stack[-1] != "[":
                    tmp = stack.pop() + tmp
                stack.pop()

                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                stack.append(int(num) * tmp)

        return "".join(stack)