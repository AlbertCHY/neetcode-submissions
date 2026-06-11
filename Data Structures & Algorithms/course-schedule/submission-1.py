class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n = len(prerequisites)
        table = defaultdict(list)
        for a, b in prerequisites:
            table[a].append(b)
        
        def dfs(curr):
            if curr in visited:
                return False
            if table[curr] == []:
                return True

            visited.add(curr)
            for target in table[curr]:
                if not dfs(target):
                    return False
            visited.remove(curr)
            return True

        visited = set()
        for i in range(numCourses):
            if not dfs(i):
                return False
            
        return True

