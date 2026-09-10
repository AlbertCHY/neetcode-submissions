class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return [i for i in range(n)]

        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        queue = deque([i for i in range(n) if len(adj[i]) == 1])

        while n > 2:
            curr_leaves = len(queue)
            n -= curr_leaves

            for _ in range(curr_leaves):
                leaf = queue.popleft()
                neighbor = adj[leaf].pop()
                adj[neighbor].remove(leaf)

                if len(adj[neighbor]) == 1:
                    queue.append(neighbor)

        return list(queue)