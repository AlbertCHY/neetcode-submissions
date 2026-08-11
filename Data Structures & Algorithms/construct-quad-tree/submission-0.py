"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def helper(n, x, y):
            flag = True
            for i in range(n):
                for j in range(n):
                    if grid[x][y] != grid[x + i][y + j]:
                        flag = False
                        break
            if flag:
                return Node(grid[x][y], True)

            n //= 2
            topleft = helper(n, x, y)
            topright = helper(n, x, y + n)
            bottomleft = helper(n, x + n, y)
            bottomright = helper(n, x + n, y + n)

            return Node(0, False, topleft, topright, bottomleft, bottomright)

        return helper(len(grid), 0, 0)