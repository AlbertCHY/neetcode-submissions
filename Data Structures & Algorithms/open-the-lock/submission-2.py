class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if target == "0000":
            return 0
        
        visited = set(deadends)
        if "0000" in visited:
            return -1

        queue = deque(["0000"])
        visited.add("0000")
        steps = 0

        while queue:
            for _ in range(len(queue)):
                curr = queue.popleft()
                if curr == target:
                    return steps
                for i in range(4):
                    digit = int(curr[i])
                    for change in (1, -1):
                        newDigit = (digit + change) % 10
                        nextCombine = curr[:i] + str(newDigit) + curr[i + 1:]

                        if nextCombine not in visited:
                            visited.add(nextCombine)
                            queue.append(nextCombine)
            steps += 1


        return -1