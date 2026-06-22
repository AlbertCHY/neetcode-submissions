class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)

        if s[0] == "0":
            return 0

        tmp1 = 1
        tmp2 = 1
        curr = 1
        for i in range(2, n + 1):
            curr = 0
            if int(s[i - 1 : i]) != 0:
                curr += tmp2

            if 10 <= int(s[i - 2 : i]) <= 26:
                curr += tmp1

            tmp1 = tmp2
            tmp2 = curr

        return curr
