class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        left, right = n, 0
        def dfs(left, right, arr):
            if left == 0 and right == 0:
                result.append("".join(arr))
                return
            
            if left > 0:
                arr.append("(")
                dfs(left - 1, right + 1, arr)
                arr.pop()
            if right > 0:
                arr.append(")")
                dfs(left, right - 1, arr)
                arr.pop()




        dfs(n, 0, [])

        return result