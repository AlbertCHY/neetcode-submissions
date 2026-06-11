class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        table = defaultdict(list)
        for a, b in prerequisites:
            table[a].append(b)


        def dfs(curr):
            if curr in visited:
                return False
            if curr in taken:
                return True

            visited.add(curr)
            for pre in table[curr]:
                if not dfs(pre):
                    return False
            visited.remove(curr)
            result.append(curr)
            taken.add(curr)

            return True



        result = []
        visited = set()
        taken = set()
        for i in range(numCourses):
            if not dfs(i):
                return []

        return result