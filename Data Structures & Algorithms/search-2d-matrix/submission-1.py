class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        
        left, right = 0, m
        while left < right:
            mid = (left + right) // 2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                right = mid - 1
            else:
                left = mid
                if right - mid == 1:
                    break
        
        idx = left
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[idx][mid] == target:
                return True
            elif matrix[idx][mid] > target:
                right = mid - 1
            else:
                left = mid + 1

        return False