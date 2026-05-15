class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        leftBound = [0] * n
        rightBound = [0] * n
        

        stack = []
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                leftBound[i] = -1
            else:
                leftBound[i] = stack[-1]
            stack.append(i) 

        stack = []
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if not stack:
                rightBound[i] = n
            else:
                rightBound[i] = stack[-1]
            stack.append(i) 

        result = 0
        for i in range(n):
            result = max(result, heights[i] * (rightBound[i] - leftBound[i] - 1))

        return result
