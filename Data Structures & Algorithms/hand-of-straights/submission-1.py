class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        hand.sort()
        freq = defaultdict(int)
        for i in range(n):
            freq[hand[i]] = freq.get(hand[i], 0) + 1

        for card in hand:
            if freq[card]:
                for i in range(card, card + groupSize):
                    if not freq[i]:
                        return False
                    freq[i] -= 1


        return True

