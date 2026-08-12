# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        cache = {None: 0}

        def helper(node):
            if node in cache:
                return cache[node]

            tmp = node.val
            if node.left:
                tmp += helper(node.left.left) + helper(node.left.right)
            if node.right:
                tmp += helper(node.right.right) + helper(node.right.left)

            cache[node] = max(tmp, helper(node.left) + helper(node.right))
            return cache[node]

        return helper(root)