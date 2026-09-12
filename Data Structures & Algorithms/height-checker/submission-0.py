class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        result = 0
        expect = sorted(heights)
        for i in range(len(heights)):
            if expect[i] != heights[i]:
                result += 1

        return result