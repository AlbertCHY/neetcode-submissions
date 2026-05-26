# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.target = None
        def dfs(node, p, q):
            if not node:
                return False

            left = dfs(node.left, p, q)
            right = dfs(node.right, p, q)
            if node.val != p.val and node.val != q.val:
                if left and right:
                    self.target = node
                return left or right
            else:
                if left or right:
                    if not self.target:
                        self.target = node
                return True


        dfs(root, p, q)

        return self.target
            
