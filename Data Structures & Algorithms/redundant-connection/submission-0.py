class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        table = defaultdict(list)
        for u, v in edges:
            table[u].append(v)
            table[v].append(u)

        def dfs(curr, prev):
            if curr in visited:
                return True
            
            visited.add(curr)
            for nei in table[curr]:
                if nei == prev:
                    continue
                if dfs(nei, curr):
                    return True
            return False

        
        table = defaultdict(list)
        for u, v in edges:
            table[u].append(v)
            table[v].append(u)
            visited = set()

            if dfs(u, -1):
                return [u, v]

        return []



        