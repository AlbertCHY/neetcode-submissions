class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        queue = deque()
        queue.append(0)
        visited = set()

        dist = 0
        while queue:
            dist += 1
            for _ in range(len(queue)):
                curr = queue.popleft()
                for coin in coins:
                    nxt = curr + coin
                    if nxt == amount:
                        return dist
                    elif nxt > amount or nxt in visited:
                        continue
                    visited.add(nxt)
                    queue.append(nxt)
        
        return -1