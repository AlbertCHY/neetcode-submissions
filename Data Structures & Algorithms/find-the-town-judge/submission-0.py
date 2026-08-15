class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        degree = [0] * (n + 1)

        for a, b in trust:
            degree[a] -= 1
            degree[b] += 1

        judge = -1
        for i in range(len(degree)):
            if degree[i] == n - 1 and judge == -1:
                judge = i
            elif degree[i] == n - 1 and judge != -1:
                return -1

        return judge if judge != -1 else -1