class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        m, n = len(image), len(image[0])
        target = image[sr][sc]
        if target == color:
            return image

        def dfs(i, j):
            if i < 0 or j < 0 or i >= m or j >= n or image[i][j] != target:
                    return

            image[i][j] = color
            for di, dj in directions:
                ni, nj = i + di, j + dj
                dfs(ni, nj) 

        dfs(sr, sc)
        return image