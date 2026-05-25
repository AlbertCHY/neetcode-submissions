# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def counter(root, depth):
            if not root:
                return depth
            return max(counter(root.left, depth + 1), counter(root.right, depth + 1))
            

        return counter(root, 0)