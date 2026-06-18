class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        prerequest = set()
        for i in range(1, len(words)):
            c = 0
            while c < len(words[i]) and c < len(words[i - 1]) and words[i][c] == words[i - 1][c]:
                c += 1
            if c != len(words[i - 1]) and c == len(words[i]):
                return ""
            elif c != len(words[i - 1]) and c != len(words[i]):
                prerequest.add((words[i - 1][c] , words[i][c]))

        degree = {}
        for word in words:
            for c in word:
                degree[c] = 0
                
        adj = defaultdict(list)
        for u, v in prerequest:
            degree[v] = degree.get(v, 0) + 1
            adj[u].append(v)

        queue = deque()
        for key in degree.keys():
            if degree[key] == 0:
                queue.append(key)
        
        result = []
        checker = 0
        while queue:
            curr = queue.popleft()
            result.append(curr)
            checker += 1
            for nei in adj[curr]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)

        return "".join(result) if checker == len(degree) else ""