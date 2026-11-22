class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        n = len(s)
        s = list(s)

        i = 0
        while i < n:
            if i == 0 or s[i] != s[i - 1]:
                stack.append(1)
            else:
                stack[-1] += 1
                if stack[-1] == k:
                    stack.pop()
                    del s[i - k + 1:i + 1]
                    i -= k
                    n -= k

            i += 1

        return "".join(s)