class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "qprs",
            "8": "tuv",
            "9": "wxyz",
        }
        result = []

        def dfs(i, arr):
            if i == len(digits):
                result.append("".join(arr.copy()))
                return

            s = table.get(digits[i])
            for j in range(len(s)):
                arr.append(s[j])
                dfs(i + 1, arr)
                arr.pop()


        dfs(0, [])
        return result