class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        adj = defaultdict(list)
        for (a,b), v in zip(equations, values):
            adj[a].append((b, v))
            adj[b].append((a, 1 / v))

        def dfs(node, target, visited):
            if node not in adj:
                return -1.0

            if node == target:
                return 1.0

            visited.add(node)
            for nei, v in adj[node]:
                if nei not in visited:
                    tmp = dfs(nei, target, visited)
                    if tmp != -1.0:
                        return tmp * v
            visited.remove(node)
            
            return -1.0

        result = []
        for node, target in queries:
            if node not in adj or target not in adj:
                result.append(-1.0)
            else:
                result.append(dfs(node, target, set()))

        return result