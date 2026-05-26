# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        maximum = -float("inf")

        def dfs(node, maximum):
            if not node:
                return 0
            
            if node.val >= maximum:
                good = True
            else:
                good = False
            maximum = max(maximum, node.val)
            left = dfs(node.left, maximum)
            right = dfs(node.right, maximum)
            return left + right + 1 if good else left + right


        return dfs(root, maximum)

