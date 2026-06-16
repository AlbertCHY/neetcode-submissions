class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        n = len(tickets)
        counts = {}

        for u, v in tickets:
            adj[u].append(v)
            counts[(u, v)] = counts.get((u, v), 0) + 1

        for arr in adj.values():
            arr.sort()

        def dfs(curr, prev, path):
            if len(path) == n + 1:
                result.append(path.copy())
                return
            
            for nei in adj[curr]:
                if result:
                    break
                if counts.get((curr, nei), 0) >= 1:
                    path.append(nei)
                    counts[(curr, nei)] -= 1
                    dfs(nei, curr, path)
                    path.pop()
                    counts[(curr, nei)] += 1

        
        result = []
        dfs("JFK", "", ["JFK"])
        
        return result[0]