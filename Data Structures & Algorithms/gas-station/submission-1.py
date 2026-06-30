class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)

        index = 0
        total = 0
        for i in range(n):
            gain = gas[i] - cost[i]
            total += gain
            if total < 0:
                total = 0
                index = i + 1
                

        return index if sum(gas) >= sum(cost) else -1