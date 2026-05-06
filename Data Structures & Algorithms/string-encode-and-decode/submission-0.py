class Solution:

    def encode(self, strs: List[str]) -> str:
        arr = []
        for s in strs:
            arr.append(str(len(s)))
            arr.append(" ")
            arr.append(s)
        return "".join(arr)

    def decode(self, s: str) -> List[str]:
        result = []
        i = 0
        while i < len(s):
            num = []
            while s[i] != " ":
                num.append(s[i])
                i += 1
            i += 1
            n = int("".join(num))
            tmp = []
            for j in range(n):
                tmp.append(s[i])
                i += 1
            result.append("".join(tmp))

        return result