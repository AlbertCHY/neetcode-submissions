class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort()
        res = [0] * len(deck)
        queue = deque(range(len(deck)))
        
        for num in deck:
            i = queue.popleft()
            res[i] = num
            if queue:
                queue.append(queue.popleft())

        return res
