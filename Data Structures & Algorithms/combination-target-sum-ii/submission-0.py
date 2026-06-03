class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        n = len(candidates)

        def dfs(i, arr, curr):
            if curr == target:
                result.append(arr.copy())
                return
            if i >= n or curr > target:
                return

            arr.append(candidates[i])
            dfs(i + 1, arr, curr + candidates[i])
            arr.pop()
            while i + 1 < n and candidates[i] == candidates[i + 1]:
                i += 1
            dfs(i + 1, arr, curr)


        dfs(0, [], 0)

        return result