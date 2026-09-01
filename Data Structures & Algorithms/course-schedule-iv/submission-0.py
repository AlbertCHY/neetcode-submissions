class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        adj = [set() for _ in range(numCourses)]
        indegree = [0] * numCourses
        allPrev = [set() for _ in range(numCourses)]

        for before, after in prerequisites:
            adj[before].add(after)
            indegree[after] += 1

        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)

        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                allPrev[neighbor].add(curr)
                allPrev[neighbor].update(allPrev[curr])
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return [u in allPrev[v] for u, v in queries]