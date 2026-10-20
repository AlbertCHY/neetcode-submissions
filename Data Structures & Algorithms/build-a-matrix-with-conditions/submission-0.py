class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topo_sort(k, conditions):
            adj = [[] for _ in range(k + 1)]
            in_degree = [0] * (k + 1)

            for u, v in conditions:
                adj[u].append(v)
                in_degree[v] += 1

            queue = deque()
            for i in range(1, k + 1):
                if in_degree[i] == 0:
                    queue.append(i)

            result = []
            while queue:
                curr = queue.popleft()
                result.append(curr)
                for nei in adj[curr]:
                    in_degree[nei] -= 1
                    if in_degree[nei] == 0:
                        queue.append(nei)

            if len(result) < k:
                return []
            return result

        sortedR = topo_sort(k, rowConditions)
        sortedC = topo_sort(k, colConditions)
        if not sortedR or not sortedC:
            return []

        result = [[0] * k for _ in range(k)]
        for i in range(k):
            num = sortedR[i]
            result[i][sortedC.index(num)] = num

        return result
