class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n, 0) + 1

        freq = list(freq.items())
        freq.sort(key=lambda x: x[1], reverse=True)
        result = []
        for i in range(k):
            result.append(freq[i][0])
        
        return result