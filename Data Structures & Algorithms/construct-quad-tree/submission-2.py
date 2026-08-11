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
            if n == 1:
                return Node(grid[x][y] == 1, True)
            
            n //= 2
            tl = helper(n, x, y)
            tr = helper(n, x, y + n)
            bl = helper(n, x + n, y)
            br = helper(n, x + n, y + n)

            if tl.val == tr.val == bl.val == br.val and tl.isLeaf and tr.isLeaf and bl.isLeaf and br.isLeaf:
                return Node(tl.val, True)
            else:
                return Node(False, False, tl, tr, bl, br)

        return helper(len(grid), 0, 0)