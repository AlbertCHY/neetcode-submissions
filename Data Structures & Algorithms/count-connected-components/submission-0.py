class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visited = set()
        loop = set()
        result = 0
        table = defaultdict(list)

        for a, b in edges:
            table[a].append(b)
            table[b].append(a)

        def dfs(curr, prev):
            if curr in visited:
                return
            if curr in loop:
                return

            visited.add(curr)
            loop.add(curr)
            for target in table[curr]:
                if target == prev:
                    continue
                dfs(target, curr)
            loop.remove(curr)
            return


        for i in range(n):
            if i in visited:
                continue
            dfs(i, -1)
            result += 1

        return result