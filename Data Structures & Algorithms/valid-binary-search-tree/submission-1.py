# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, maximum, minimum):
            if not node:
                return True

            if node.val >= maximum or node.val <= minimum:
                return False
            
            return dfs(node.left, node.val, minimum) and dfs(node.right, maximum, node.val)


        return dfs(root.left, root.val, -float("inf")) and dfs(root.right, float("inf"), root.val)