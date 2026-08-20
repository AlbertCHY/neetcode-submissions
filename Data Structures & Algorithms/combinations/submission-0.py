class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(i, arr):
            if arr and len(arr) == k:
                result.append(arr.copy())
                return
                
            if i > n:
                return

            arr.append(i)
            dfs(i + 1, arr)
            arr.pop()
            dfs(i + 1, arr)

        dfs(1, [])
        return result