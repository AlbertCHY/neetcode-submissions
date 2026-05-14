class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        n = len(heights)

        for i in range(n):
            temp = float("inf")
            for j in range(i, n):
                temp = min(temp, heights[j])
                result = max(result, (j - i + 1) * temp)





        return result