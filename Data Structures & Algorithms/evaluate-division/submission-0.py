class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for (a,b), v in zip(equations, values):
            adj[a].append((b, v))
            adj[b].append((a, 1 / v))

        def dfs(node, target):
            if node == target:
                return 1.0

            if node not in adj:
                return -1

            tmp = -1
            for nei, v in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    tmp = dfs(nei, target) * v
                    visited.remove(nei)
            
            return float(-1) if tmp < 0 else tmp

        visited = set()
        result = []
        for node, target in queries:
            if node not in adj or target not in adj:
                result.append(-1.0)
            else:
                result.append(dfs(node, target))

        return result