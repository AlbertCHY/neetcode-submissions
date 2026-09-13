class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = Counter(arr)
        result = -1

        for num in freq:
            if num == freq[num]:
                result = max(num, result)

        return result