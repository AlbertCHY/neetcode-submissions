class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        table = defaultdict(list)
        for u, v in edges:
            table[u].append(v)
            table[v].append(u)

        def dfs(curr, prev):
            if curr in visited:
                return False

            visited.add(curr)
            for nei in table[curr]:
                if nei == prev:
                    continue
                if not dfs(nei, curr):
                    return False
            return True


        visited = set()
        if not dfs(0, -1):
            return False

        return len(visited) == n