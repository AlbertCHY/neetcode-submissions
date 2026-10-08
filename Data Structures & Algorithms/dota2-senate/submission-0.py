class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        dque, rque = deque(), deque()
        n = len(senate)

        for i, c in enumerate(senate):
            if c == "R":
                rque.append(i)
            else:
                dque.append(i)

        while dque and rque:
            d = dque.popleft()
            r = rque.popleft()

            if d > r:
                rque.append(r + n)
            else:
                dque.append(d + n)

        return "Radiant" if rque else "Dire"

        