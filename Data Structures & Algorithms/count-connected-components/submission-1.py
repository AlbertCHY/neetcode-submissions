class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        result = 0
        table = defaultdict(list)

        for a, b in edges:
            table[a].append(b)
            table[b].append(a)

        def dfs(curr):
            for target in table[curr]:
                if target not in visited:
                    visited.add(target)
                    dfs(target)
            return


        for i in range(n):
            if i in visited:
                continue
            dfs(i)
            result += 1

        return result