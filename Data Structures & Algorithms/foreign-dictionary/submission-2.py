class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        prerequest = set()
        for i in range(1, len(words)):
            c = 0
            word1, word2 = words[i - 1], words[i]
            while c < len(word2) and c < len(word1) and word2[c] == word1[c]:
                c += 1
            if c != len(word1) and c == len(word2):
                return ""
            elif c != len(word1) and c != len(word2):
                prerequest.add((word1[c] , word2[c]))

        degree = {}
        for word in words:
            for c in word:
                degree[c] = 0
                
        adj = defaultdict(list)
        for u, v in prerequest:
            degree[v] += 1
            adj[u].append(v)

        queue = deque()
        for key in degree.keys():
            if degree[key] == 0:
                queue.append(key)
        
        result = []
        while queue:
            curr = queue.popleft()
            result.append(curr)
            for nei in adj[curr]:
                degree[nei] -= 1
                if degree[nei] == 0:
                    queue.append(nei)

        return "".join(result) if len(result) == len(degree) else ""